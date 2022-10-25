指定したタイムゾーンの日付型を作るクラス。

　UTC, ローカル, 指定タイムゾーン用クラス。さらにSQLite3(UTC標準時で`yyyy-MM-dd HH:mm:ss`形式)も作った。

<!-- more -->

# ブツ

* [リポジトリ][]

[リポジトリ]:https://github.com/ytyaru/Python.Python.DateTime.Native.Utc.Tz.20221022143840
[DEMO]:https://ytyaru.github.io/Python.Python.DateTime.Native.Utc.Tz.20221022143840/

## 実行

```sh
NAME='Python.Python.DateTime.Native.Utc.Tz.20221022143840'
git clone https://github.com/ytyaru/$NAME
cd $NAME/src
./test-aware-date-time.py
./test-time-zone.py
./test-zone-date-time.py
./test-local-date-time.py
./test-utc-date-time.py
./test-sqlite-date-time.py
```

## 概要

　タイムゾーンがないとき指定した各タイムゾーンとして解釈する。

```python
#!/usr/bin/env python3
# coding: utf8
import datetime, zoneinfo # Python3.9以上必須
import importlib  
UtcDateTime = importlib.import_module('utc-date-time').UtcDateTime
LocalDateTime = importlib.import_module('local-date-time').LocalDateTime
ZoneDateTime = importlib.import_module('zone-date-time').ZoneDateTime 
SQLiteDateTime = importlib.import_module('sqlite-date-time').SQLiteDateTime

native = '2000-01-01 00:00:00'
assert UtcDateTime(native) == datetime.datetime.fromisoformat('1999-12-31 15:00:00+00:00')
assert LocalDateTime(native) == datetime.datetime.fromisoformat(native).astimezone(tz=datetime.datetime.now().astimezone().tzinfo)
assert ZoneDateTime(native, zoneinfo.ZoneInfo('Asia/Tokyo')) == datetime.datetime.fromisoformat('2000-01-01 00:00:00+09:00')
assert SQLiteDateTime(native) == datetime.datetime.fromisoformat('2000-01-01 00:00:00+00:00')
```

　`native`はテキストの他`datetime`型インスタンスでもいい。`

　タイムゾーンがない`native`な日付をそれぞれのクラスに渡すと、それぞれのタイムゾーンで解釈した日付型クラスになる。

クラス|解釈|変換
------|----|----
`UtcDateTime`|実行環境のタイムゾーン|UTC
`LocalDateTime`|実行環境のタイムゾーン|実行環境のタイムゾーン
`ZoneDateTime`|指定したタイムゾーン|指定したタイムゾーン
`SQLiteDateTime`|UTC|UTC

　ふつうタイムゾーンがなければローカルのタイムゾーン、すなわち実行環境のタイムゾーンだと解釈するはず。なので基本的にはそうしている。

　タイムゾーンはUTCと実行環境のさえあれば十分。ただ、それ以外にもカバーできるよう指定したタイムゾーンで解釈・出力するクラスも作った。

　また、SQLite3はUTCとして解釈・出力するのでそうした。

### 相互変換

```python
l = LocalDateTime(SQLiteDateTime(native).to_datetime())
assert f"{l:%Y-%m-%dT%H:%M:%S%z}" == '2000-01-01T09:00:00+0900'
z = ZoneDateTime(SQLiteDateTime(native).to_datetime(), zoneinfo.ZoneInfo('Asia/Tokyo'))
assert f"{z:%Y-%m-%dT%H:%M:%S%z}" == '2000-01-01T09:00:00+0900'

s = SQLiteDateTime(LocalDateTime(native).to_datetime())
assert f"{s:%Y-%m-%dT%H:%M:%S%z}" == '1999-12-31T15:00:00+0000'
z = ZoneDateTime(LocalDateTime(native).to_datetime(), zoneinfo.ZoneInfo('Asia/Tokyo'))
assert f"{z:%Y-%m-%dT%H:%M:%S%z}" == '2000-01-01T00:00:00+0900'

s = SQLiteDateTime(ZoneDateTime(native, zoneinfo.ZoneInfo('Asia/Tokyo')).to_datetime())
assert f"{s:%Y-%m-%dT%H:%M:%S%z}" == '1999-12-31T15:00:00+0000'
l = LocalDateTime(ZoneDateTime(native, zoneinfo.ZoneInfo('Asia/Tokyo')).to_datetime())
assert f"{l:%Y-%m-%dT%H:%M:%S%z}" == '2000-01-01T00:00:00+0900'
```

　変換は以下の方法でも可能。

`AwareDateTime`|`datetime.datetime`|概要
---------------|-------------------|----
`to_utc(dt)`|`dt.astimezone(tz=datetime.timezone.utc)`|UTCに変換する
`to_local(dt)`|`dt.astimezone()`|ローカル時に変換する
`to_tz(dt, tz)`|`dt.astimezone(tz=datetime.timezone(datetime.timedelta(seconds=32400)))`|指定タイムゾーン時に変換する

### `datetime`用メソッドが直接参照できない

　各クラスは日付型`datetime`を継承している。なので`datetime`型のメソッドが使えるかと思いきや以下エラーがでる。

```python
TypeError: SQLiteDateTime.__new__() takes from 1 to 2 positional arguments but 9 were given
```
```python
TypeError: SQLiteDateTime.__new__() は 1 ～ 2 個の位置引数を取りますが、9 個が指定されました
```

　よくわからないが、一旦以下メソッド`to_datetime()`で`datetime`型に変換してから呼び出せば成功する。面倒くさい。

```python
def to_datetime(self): return datetime.datetime(self.year, self.month, self.day, self.hour, self.minute, self.second, self.microsecond, self.tzinfo)
```

　おそらく原因は以下の`datetime.__new__`で引数を9個使って呼び出している所だと思う。でもどう変更すれば対応できるかわからない。Python難しい。

```python
class ZoneDateTime(datetime.datetime):
    def __new__(cls, dt=None, tz=None, is_native_utc=False):
        d = cls._get_default_datetime(dt, tz, is_native_utc=is_native_utc)
        return datetime.datetime.__new__(cls, d.year, d.month, d.day, d.hour, d.minute, d.second, d.microsecond, d.tzinfo)
```

　以下のように変えてみたけど同じエラーになった。もうわからない。

```python
    def __new__(cls, *args, **kwargs):
        d = cls._get_default_datetime(kwargs['dt'], kwargs['tz'], is_native_utc=kwargs['is_native_utc'])
        return datetime.datetime.__new__(cls, args, kwargs)
```
```python
    return datetime.datetime.__new__(cls, args, kwargs)
TypeError: 'tuple' object cannot be interpreted as an integer
```

-------------------------------------------------------------------------------














　パターンとその網羅は以下。

解釈|出力|クラス
----|----|------
UTC|UTC|`SQLiteDateTime`
UTC|LOCAL|❌
UTC|指定タイムゾーン|❌
LOCAL|UTC|`UtcDateTime`
LOCAL|LOCAL|`LocalDateTime`
LOCAL|指定タイムゾーン|❌
指定タイムゾーン|UTC|❌
指定タイムゾーン|LOCAL|❌
指定タイムゾーン|指定タイムゾーン|`ZoneDateTime`

　実装していないもので使いそうなのは`UTC-LOCAL`パターン。SQLite3から読み取ってローカル日時に変換するときに使いそう。大抵は`yyyy-MM-dd`や`yyyy-MM-dd HH:MM:SS`のテキストだったりする。または`M月D日`のようなフォーマットかもしれない。あるいは現在日時からの差分で`D日前`などかもしれない。

LocalDateTime(SQLiteDateTime('2000-01-01 00:00:00'))

　相互変換は以下。

```python
l = LocalDateTime(SQLiteDateTime(native).to_datetime())
assert f"{l:%Y-%m-%dT%H:%M:%S%z}" == '2000-01-01T09:00:00+0900'
z = ZoneDateTime(SQLiteDateTime(native).to_datetime(), zoneinfo.ZoneInfo('Asia/Tokyo'))
assert f"{z:%Y-%m-%dT%H:%M:%S%z}" == '2000-01-01T09:00:00+0900'

s = SQLiteDateTime(LocalDateTime(native).to_datetime())
assert f"{s:%Y-%m-%dT%H:%M:%S%z}" == '1999-12-31T15:00:00+0000'
z = ZoneDateTime(LocalDateTime(native).to_datetime(), zoneinfo.ZoneInfo('Asia/Tokyo'))
assert f"{z:%Y-%m-%dT%H:%M:%S%z}" == '2000-01-01T00:00:00+0900'

s = SQLiteDateTime(ZoneDateTime(native, zoneinfo.ZoneInfo('Asia/Tokyo')).to_datetime())
assert f"{s:%Y-%m-%dT%H:%M:%S%z}" == '1999-12-31T15:00:00+0000'
l = LocalDateTime(ZoneDateTime(native, zoneinfo.ZoneInfo('Asia/Tokyo')).to_datetime())
assert f"{l:%Y-%m-%dT%H:%M:%S%z}" == '2000-01-01T00:00:00+0900'
```

SQLiteDateTime(native).astimezone()

　変換は以下の方法でも可能。

`AwareDateTime`|`datetime.datetime`|概要
---------------|-------------------|----
`to_utc(dt)`|`dt.astimezone(tz=datetime.timezone.utc)`|UTCに変換する
`to_local(dt)`|`dt.astimezone()`|ローカル時に変換する
`to_tz(dt, tz)`|`dt.astimezone(tz=datetime.timezone(datetime.timedelta(seconds=32400)))`|指定タイムゾーン時に変換する


　各クラスは日付型`datetime`を継承している。なので`datetime`型のメソッドが使えるかと思いきや以下エラーがでる。

```python
TypeError: SQLiteDateTime.__new__() takes from 1 to 2 positional arguments but 9 were given
```
```python
TypeError: SQLiteDateTime.__new__() は 1 ～ 2 個の位置引数を取りますが、9 個が指定されました
```

　よくわからないが、一旦以下メソッド`to_datetime()`で`datetime`型に変換してから呼び出せば成功する。面倒くさい。

```python
def to_datetime(self): return datetime.datetime(self.year, self.month, self.day, self.hour, self.minute, self.second, self.microsecond, self.tzinfo)
```

　おそらく原因は以下の`datetime.__new__`で引数を9個使って呼び出している所だと思う。でもどう変更すれば対応できるかわからない。Python難しい。

```python
class ZoneDateTime(datetime.datetime):
    def __new__(cls, dt=None, tz=None, is_native_utc=False):
        d = cls._get_default_datetime(dt, tz, is_native_utc=is_native_utc)
        return datetime.datetime.__new__(cls, d.year, d.month, d.day, d.hour, d.minute, d.second, d.microsecond, d.tzinfo)
```

　けど以下のように変えてみたけど同じエラーになった。もうわからない。

```python
class ZoneDateTime(datetime.datetime):
    def __new__(cls, *args, **kwargs):
        d = cls._get_default_datetime(kwargs['dt'], kwargs['tz'], is_native_utc=kwargs['is_native_utc'])
        return datetime.datetime.__new__(cls, d.year, d.month, d.day, d.hour, d.minute, d.second, d.microsecond, d.tzinfo)
```



　`to_datetime()`せず各クラスをそのままコンストラクタに渡すと以下エラーが出る。これがよくわからない。


　これを各クラスに


`dt.astimezone()`|
`dt.astimezone()`|
`dt.astimezone()`|


　`UtcToLocal`のような別クラスを作ってもよかったが面倒なので`SQLiteDateTime`クラスのメソッドとして実装した。単に`astimezone()`や`astimezone(tz=tz)`とすればいいだけだったのでオマケのようなもの。

　日付の変換さえできれば、あとはテキスト書式だけ。これは`f""`



# コード抜粋

ファイル|概要
--------|----
`aware-date-time.py`|タイムゾーンなし日付型にタイムゾーンをつけるメソッドを用意したクラス
`time-zone.py`|ローカルのタイムゾーンを返すメソッドなどを用意したクラス
`zone-date-time.py`|指定したタイムゾーンの日付型を作るクラス
`local-date-time.py`|ローカル・タイムゾーンの日付型を作るクラス
`utc-date-time.py`|UTCタイムゾーンの日付型を作るクラス
`sqlite-date-time.py`|SQLite3の日付型を作るクラス（タイムゾーンがないときUTCとして解釈する）

## `zone-date-time.py`

　指定したタイムゾーンの日付型を作るクラス。

```python
import datetime
import importlib  
AwareDateTime = importlib.import_module('aware-date-time').AwareDateTime 
TimeZone = importlib.import_module('time-zone').TimeZone
class ZoneDateTime(datetime.datetime):
    def __new__(cls, dt=None, tz=None, is_native_utc=False):
        d = cls._get_default_datetime(dt, tz, is_native_utc=is_native_utc)
        return datetime.datetime.__new__(cls, d.year, d.month, d.day, d.hour, d.minute, d.second, d.microsecond, d.tzinfo)
    @classmethod
    def _get_default_datetime(cls, dt, tz, is_native_utc=False):
        if tz is None: tz = TimeZone.local()
        if dt is None: return datetime.datetime.now(tz)
        if isinstance(dt, str): dt = AwareDateTime.from_iso(dt)
        if not isinstance(dt, datetime.datetime): return datetime.datetime.now(tz)
        if is_native_utc: return dt.replace(tzinfo=tz)
        return AwareDateTime.to_tz(dt if AwareDateTime.is_aware(dt) else AwareDateTime.to_utc(dt) if is_native_utc else AwareDateTime.to_local(dt), tz)
    def __init__(self, dt=None, tz=None): pass
    def to_iso(self): return f"{self:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(self)}"
    def to_sqlite(self): return f"{datetime.datetime(self.year, self.month, self.day, self.hour, self.minute, self.second, self.microsecond, self.tzinfo).astimezone(datetime.timezone.utc):%Y-%m-%d %H:%M:%S}"
    #def to_isoz(self): return f"{self:%Y-%m-%dT%H:%M:%SZ}"
    #TypeError: ZoneDateTime.__new__() takes from 1 to 3 positional arguments but 9 were given
    #def to_sqlite(self): return f"{AwareDateTime.to_utc(self):%Y-%m-%d %H:%M:%S}"
    #def to_sqlite(self): return f"{self.astimezone(datetime.timezone.utc):%Y-%m-%d %H:%M:%S}"
    #def to_sqlite(self): return f"{super().astimezone(datetime.timezone.utc):%Y-%m-%d %H:%M:%S}"

```

　これをベースにUTC,ローカル,SQLite3用の日付クラスを作る。

## `local-date-time.py`

```python
import datetime
import importlib  
AwareDateTime = importlib.import_module('aware-date-time').AwareDateTime 
TimeZone = importlib.import_module('time-zone').TimeZone
ZoneDateTime = importlib.import_module('zone-date-time').ZoneDateTime 
class LocalDateTime(ZoneDateTime):
    def __new__(cls, dt=None): return super().__new__(cls, dt=cls._get_default_datetime(dt, TimeZone.local()), tz=TimeZone.local())
```

## `utc-date-time.py`

```python
import datetime
import importlib  
AwareDateTime = importlib.import_module('aware-date-time').AwareDateTime 
TimeZone = importlib.import_module('time-zone').TimeZone
ZoneDateTime = importlib.import_module('zone-date-time').ZoneDateTime 
class UtcDateTime(ZoneDateTime):
    def __new__(cls, dt=None): return super().__new__(cls, dt=cls._get_default_datetime(dt, TimeZone.utc()), tz=TimeZone.utc())
    def to_isoz(self): return f"{self:%Y-%m-%dT%H:%M:%SZ}"
```

## `sqlite-date-time.py`

```python
import datetime
import importlib  
AwareDateTime = importlib.import_module('aware-date-time').AwareDateTime 
TimeZone = importlib.import_module('time-zone').TimeZone
ZoneDateTime = importlib.import_module('zone-date-time').ZoneDateTime 
class SQLiteDateTime(ZoneDateTime):
    def __new__(cls, dt=None): return super().__new__(cls, dt=cls._get_default_datetime(dt, TimeZone.utc(), is_native_utc=True), tz=TimeZone.utc(), is_native_utc=True)
    def to_isoz(self): return f"{self:%Y-%m-%dT%H:%M:%SZ}"
```

```python
```

```python
#!/usr/bin/env python3
# coding: utf8
```


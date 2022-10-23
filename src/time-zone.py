import datetime, zoneinfo
from collections import namedtuple
import importlib  
AwareDateTime = importlib.import_module('aware-date-time').AwareDateTime 
class TimeZone:
    @classmethod # UTCのタイムゾーンを返す
    def utc(cls): return datetime.timezone.utc
    @classmethod # ローカルのタイムゾーンを返す
    def local(cls): return datetime.datetime.now().astimezone().tzinfo
    @classmethod # UTC標準時からの時差を返す（指定した日時のタイムゾーンを秒数で返す）
    def sec(cls, dt=None):
        if isinstance(dt, datetime.datetime):
            return cls.sec(dt.astimezone()) if AwareDateTime.is_native(dt) else dt.tzinfo.utcoffset(dt).seconds
        elif isinstance(dt, datetime.timezone): return dt.utcoffset(datetime.datetime.now()).seconds
        elif isinstance(dt, zoneinfo.ZoneInfo):
            d = datetime.datetime.now(tz=dt)
            return d.tzinfo.utcoffset(d).seconds
        elif dt is None: return cls.local().utcoffset(datetime.datetime.now()).seconds
        else: raise TypeError('引数はdatetimeまたはtimezoneにしてください。')
    @classmethod # UTC標準時からの時差を返す（指定した日時のタイムゾーンを+00:00テキストで返す）
    def iso(cls, dt=None):
        seconds = cls.sec(dt)
        minutes = seconds // 60
        h = minutes // 60
        m = minutes - (h * 60)
        s = seconds % 60
        return f"{'+' if 0 <= seconds else '-'}{h:02}:{m:02}{'' if 0 == s else ':'+str(s).zfill(2)}"

    @classmethod # 全タイムゾーンを返す
    def gets(cls):
        Tz = namedtuple('Tz', 'name iso seconds')
        timezones = []
        for name in zoneinfo.available_timezones():
            dt = datetime.datetime.now(tz=zoneinfo.ZoneInfo(name))
            seconds = dt.tzinfo.utcoffset(dt).seconds
            timezones.append(Tz(name, cls.iso(dt), seconds))
        return sorted(timezones, key=lambda i: (i.seconds, i.name))
    @classmethod # 全タイムゾーンをTSVファイル出力する
    def make_tsv(cls):
        tz_txt = '\n'.join([f"{tz.iso}\t{tz.name}" for tz in cls.gets()])
        with open('timezone-list.tsv', 'w', encoding='UTF-8') as f: f.write(tz_txt)
    @classmethod # 指定した秒数、ISO、地域名に一致するタイムゾーンを返す
    def search(cls, q):
        if isinstance(q, int): return list(filter(lambda tz: tz.seconds==q, cls.gets()))
        elif isinstance(q, str) and q.startswith('+'): return list(filter(lambda tz: tz.iso==q, cls.gets()))
        elif isinstance(q, str): return list(filter(lambda tz: q in tz.name, cls.gets()))
        else: raise TypeError("引数はintまたはstr型で指定してください。")



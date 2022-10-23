import datetime
import importlib  
AwareDateTime = importlib.import_module('aware-date-time').AwareDateTime 
TimeZone = importlib.import_module('time-zone').TimeZone
ZoneDateTime = importlib.import_module('zone-date-time').ZoneDateTime 
class SQLiteDateTime(ZoneDateTime):
    def __new__(cls, dt=None): return super().__new__(cls, dt=dt, tz=TimeZone.utc(), is_native_utc=True)
    #def __new__(cls, dt=None): return super().__new__(cls, dt=cls._get_default_datetime(dt, TimeZone.utc(), is_native_utc=True), tz=TimeZone.utc(), is_native_utc=True)
    def to_isoz(self): return f"{self:%Y-%m-%dT%H:%M:%SZ}"

    def to_local(self): return self.to_datetime().astimezone(tz=TimeZone.local())
    def to_tz(self, tz): return self.to_datetime().astimezone(tz=tz)
    """
    def to_local_ymd(self): return f'{self.to_local():%Y-%m-%d}'
    def to_local_hms(self): return f'{self.to_local():%H:%M:%S}'
    def to_local_ymdhms(self): return f'{self.to_local():%Y-%m-%d %H:%M:%S}'
    def to_local_ymd_jp(self): return f'{self.to_local():%Y年%m月%d日}'
    def to_local_ymda_jp(self): return f'{self.to_local():%Y年%m月%d日(%a)}'
    def to_local_hms_jp(self): return f'{self.to_local():%H時%M分%S秒}'
    def to_local_ymdhms_jp(self): return f'{self.to_local():%Y年%m月%d日%H時%M分%S秒}'
    def to_local_ymdhmsa_jp(self): return f'{self.to_local():%Y年%m月%d日(%a)%H時%M分%S秒}'
    """


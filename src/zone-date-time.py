import datetime
import importlib  
AwareDateTime = importlib.import_module('aware-date-time').AwareDateTime 
TimeZone = importlib.import_module('time-zone').TimeZone
class ZoneDateTime(datetime.datetime):
    def __new__(cls, dt=None, tz=None, is_native_utc=False):
        d = cls._get_default_datetime(dt, tz, is_native_utc=is_native_utc)
        return datetime.datetime.__new__(cls, d.year, d.month, d.day, d.hour, d.minute, d.second, d.microsecond, d.tzinfo)
        #return datetime.datetime(d.year, d.month, d.day, d.hour, d.minute, d.second, d.microsecond, d.tzinfo)
    #def __new__(cls, *args, **kwargs):
    #    d = cls._get_default_datetime(kwargs['dt'], kwargs['tz'], is_native_utc=kwargs['is_native_utc'])
    #    return datetime.datetime.__new__(cls, *args, **kwargs)
    #    #return datetime.datetime.__new__(cls, args, kwargs)
    #    #return datetime.datetime.__new__(cls, d.year, d.month, d.day, d.hour, d.minute, d.second, d.microsecond, d.tzinfo)
    #def __init__(self): super().__init__()
    #def __init__(self): super().__init__(self.year, self.month, self.selfay, self.hour, self.minute, self.seconself, self.microseconself, self.tzinfo)
    @classmethod
    def _get_default_datetime(cls, dt, tz, is_native_utc=False):
        if tz is None: tz = TimeZone.local()
        if dt is None: return datetime.datetime.now(tz)
        # dtが文字列のときタイムゾーン情報（+, Z）があればそのまま。なければUTC`+00:00`またはローカル時`+NN:NN`付与
        if isinstance(dt, str): dt = AwareDateTime.from_iso(dt + ('' if '+' in dt or 'Z' in dt else TimeZone.iso(TimeZone.utc() if is_native_utc else TimeZone.local())))
        if not isinstance(dt, datetime.datetime): return datetime.datetime.now(tz)
        return AwareDateTime.to_tz(dt if AwareDateTime.is_aware(dt) else AwareDateTime.to_utc(dt) if is_native_utc else AwareDateTime.to_local(dt), tz)
    def __init__(self, dt=None, tz=None): pass
    def to_iso(self): return f"{self:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(self)}"
    def to_sqlite(self): return f"{self.to_datetime().astimezone(datetime.timezone.utc):%Y-%m-%d %H:%M:%S}"
    #def to_sqlite(self): return f"{datetime.datetime(self.year, self.month, self.day, self.hour, self.minute, self.second, self.microsecond, self.tzinfo).astimezone(datetime.timezone.utc):%Y-%m-%d %H:%M:%S}"
    def to_datetime(self): return datetime.datetime(self.year, self.month, self.day, self.hour, self.minute, self.second, self.microsecond, self.tzinfo)
    #def to_isoz(self): return f"{self:%Y-%m-%dT%H:%M:%SZ}"
    #TypeError: ZoneDateTime.__new__() takes from 1 to 3 positional arguments but 9 were given
    #def to_sqlite(self): return f"{AwareDateTime.to_utc(self):%Y-%m-%d %H:%M:%S}"
    #def to_sqlite(self): return f"{self.astimezone(datetime.timezone.utc):%Y-%m-%d %H:%M:%S}"
    #def to_sqlite(self): return f"{super().astimezone(datetime.timezone.utc):%Y-%m-%d %H:%M:%S}"


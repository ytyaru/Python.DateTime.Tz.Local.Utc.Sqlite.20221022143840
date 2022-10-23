import datetime
import importlib  
AwareDateTime = importlib.import_module('aware-date-time').AwareDateTime 
TimeZone = importlib.import_module('time-zone').TimeZone
ZoneDateTime = importlib.import_module('zone-date-time').ZoneDateTime 
class UtcDateTime(ZoneDateTime):
    def __new__(cls, dt=None): return super().__new__(cls, dt=dt, tz=TimeZone.utc())
    def to_isoz(self): return f"{self:%Y-%m-%dT%H:%M:%SZ}"


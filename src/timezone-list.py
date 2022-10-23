#!/usr/bin/env python3
# coding: utf8
import datetime, zoneinfo #, operator
from collections import namedtuple
def tz_iso(seconds):
    minutes = seconds // 60
    h = minutes // 60
    m = minutes - (h * 60)
    s = seconds % 60
    return f"{'+' if 0 <= seconds else '-'}{h:02}:{m:02}{'' if 0 == s else ':'+str(s).zfill(2)}"

Tz = namedtuple('Tz', 'name iso seconds')
timezones = []
for name in zoneinfo.available_timezones():
    dt = datetime.datetime.now(tz=zoneinfo.ZoneInfo(name))
    seconds = dt.tzinfo.utcoffset(dt).seconds
    timezones.append(Tz(name, tz_iso(seconds), seconds))

#timezones = sorted(timezones, key=operator.attrgetter('seconds', 'name'))
timezones = sorted(timezones, key=lambda i: (i.seconds, i.name))
#for tz in timezones: print(f"{tz.iso}\t{tz.name}")

tz_txt = '\n'.join([f"{tz.iso}\t{tz.name}" for tz in timezones])
print(tz_txt)
with open('timezone-list.tsv', 'w', encoding='UTF-8') as f:
    f.write(tz_txt)


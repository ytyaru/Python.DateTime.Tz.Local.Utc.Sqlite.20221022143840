#!/usr/bin/env python3
# coding: utf8
import datetime, zoneinfo # Python3.9以上必須
import importlib  
UtcDateTime = importlib.import_module('utc-date-time').UtcDateTime
LocalDateTime = importlib.import_module('local-date-time').LocalDateTime
ZoneDateTime = importlib.import_module('zone-date-time').ZoneDateTime 
SQLiteDateTime = importlib.import_module('sqlite-date-time').SQLiteDateTime

def asserts(native):
    assert UtcDateTime(native) == datetime.datetime.fromisoformat('1999-12-31 15:00:00+00:00')
    assert LocalDateTime(native) == datetime.datetime.fromisoformat(native).astimezone(tz=datetime.datetime.now().astimezone().tzinfo)
    assert ZoneDateTime(native, zoneinfo.ZoneInfo('Asia/Tokyo')) == datetime.datetime.fromisoformat('2000-01-01 00:00:00+09:00')
    assert SQLiteDateTime(native) == datetime.datetime.fromisoformat('2000-01-01 00:00:00+00:00')

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

native = '2000-01-01 00:00:00'
for test_data in [native, datetime.datetime.fromisoformat(native)]: asserts(native)

"""
native = '2000-01-01 00:00:00'
assert UtcDateTime(native) == datetime.datetime.fromisoformat('1999-12-31 15:00:00+00:00')
assert LocalDateTime(native) == datetime.datetime.fromisoformat(native).astimezone(tz=datetime.datetime.now().astimezone().tzinfo)
assert ZoneDateTime(native, zoneinfo.ZoneInfo('Asia/Tokyo')) == datetime.datetime.fromisoformat('2000-01-01 00:00:00+09:00')
assert SQLiteDateTime(native) == datetime.datetime.fromisoformat('2000-01-01 00:00:00+00:00')

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
"""


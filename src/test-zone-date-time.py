#!/usr/bin/env python3
# coding: utf8
import unittest
import importlib  
ZoneDateTime = importlib.import_module('zone-date-time').ZoneDateTime 
TimeZone = importlib.import_module('time-zone').TimeZone
import datetime, zoneinfo # <=3.9
class TestZoneDateTime(unittest.TestCase):
    def setUp(self): pass
    def tearDown(self): pass

    def test_new_default(self):
        actual = ZoneDateTime()
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
    def test_new_none_default(self):
        actual = ZoneDateTime(None)
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
    def test_new_none_none(self):
        actual = ZoneDateTime(None, None)
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
    def test_new_default_utc(self):
        actual = ZoneDateTime(tz=datetime.timezone.utc)
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)

    def test_new_iso_native_default(self):
        actual = ZoneDateTime('2000-01-01 00:00:00')
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
            self.assertEqual('2000-01-01T00:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
            #self.assertEqual('2000-01-01T00:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
        actual = ZoneDateTime('2000-01-01T00:00:00')
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
            self.assertEqual('2000-01-01T00:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_iso_native_none(self):
        actual = ZoneDateTime('2000-01-01 00:00:00', None)
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
            self.assertEqual('2000-01-01T00:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
        actual = ZoneDateTime('2000-01-01T00:00:00', None)
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
            self.assertEqual('2000-01-01T00:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_iso_native_utc_sqlite(self):
        actual = ZoneDateTime('2000-01-01 00:00:00', datetime.timezone.utc)
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual('1999-12-31T15:00:00+00:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_iso_native_utc_iso(self):
        actual = ZoneDateTime('2000-01-01T00:00:00', datetime.timezone.utc)
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual('1999-12-31T15:00:00+00:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_iso_native_timedelta_32400(self):
        actual = ZoneDateTime('2000-01-01T00:00:00', datetime.timezone(datetime.timedelta(seconds=32400)))
        self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
        self.assertEqual('2000-01-01T00:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_iso_native_zoneinfo(self):
        actual = ZoneDateTime('2000-01-01T00:00:00', zoneinfo.ZoneInfo('Asia/Tokyo'))
        self.assertEqual(zoneinfo.ZoneInfo('Asia/Tokyo'), actual.tzinfo)
        self.assertEqual('2000-01-01T00:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_iso_native_timedelta_16200(self):
        actual = ZoneDateTime('2000-01-01T00:00:00', datetime.timezone(datetime.timedelta(seconds=16200)))
        self.assertEqual(datetime.timezone(datetime.timedelta(seconds=16200)), actual.tzinfo)
        self.assertEqual('1999-12-31T19:30:00+04:30', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')

    def test_new_iso_utc_default(self):
        actual = ZoneDateTime('2000-01-01T00:00:00+00:00')
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
            self.assertEqual('2000-01-01T09:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_iso_utc_none(self):
        actual = ZoneDateTime('2000-01-01T00:00:00+00:00', None)
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
            self.assertEqual('2000-01-01T09:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_iso_utc_utc_sqlite(self):
        actual = ZoneDateTime('2000-01-01 00:00:00+00:00', datetime.timezone.utc)
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual('2000-01-01T00:00:00+00:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_iso_utc_utc_iso(self):
        actual = ZoneDateTime('2000-01-01T00:00:00+00:00', datetime.timezone.utc)
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual('2000-01-01T00:00:00+00:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_iso_utc_timedelta_32400(self):
        actual = ZoneDateTime('2000-01-01T00:00:00+00:00', datetime.timezone(datetime.timedelta(seconds=32400)))
        self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
        self.assertEqual('2000-01-01T09:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_iso_utc_zoneinfo(self):
        actual = ZoneDateTime('2000-01-01T00:00:00+00:00', zoneinfo.ZoneInfo('Asia/Tokyo'))
        self.assertEqual(zoneinfo.ZoneInfo('Asia/Tokyo'), actual.tzinfo)
        self.assertEqual('2000-01-01T09:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_iso_utc_timedelta_16200(self):
        actual = ZoneDateTime('2000-01-01T00:00:00+00:00', datetime.timezone(datetime.timedelta(seconds=16200)))
        self.assertEqual(datetime.timezone(datetime.timedelta(seconds=16200)), actual.tzinfo)
        self.assertEqual('2000-01-01T04:30:00+04:30', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')

    def test_new_iso_utc_z_default(self):
        actual = ZoneDateTime('2000-01-01T00:00:00Z')
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
            self.assertEqual('2000-01-01T09:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_iso_utc_z_none(self):
        actual = ZoneDateTime('2000-01-01T00:00:00Z', None)
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
            self.assertEqual('2000-01-01T09:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_iso_utc_z_utc_sqlite(self):
        actual = ZoneDateTime('2000-01-01 00:00:00Z', datetime.timezone.utc)
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual('2000-01-01T00:00:00+00:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_iso_utc_z_utc_iso(self):
        actual = ZoneDateTime('2000-01-01T00:00:00Z', datetime.timezone.utc)
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual('2000-01-01T00:00:00+00:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_iso_utc_z_timedelta_32400(self):
        actual = ZoneDateTime('2000-01-01T00:00:00Z', datetime.timezone(datetime.timedelta(seconds=32400)))
        self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
        self.assertEqual('2000-01-01T09:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_iso_utc_z_zoneinfo(self):
        actual = ZoneDateTime('2000-01-01T00:00:00Z', zoneinfo.ZoneInfo('Asia/Tokyo'))
        self.assertEqual(zoneinfo.ZoneInfo('Asia/Tokyo'), actual.tzinfo)
        self.assertEqual('2000-01-01T09:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_iso_utc_z_timedelta_16200(self):
        actual = ZoneDateTime('2000-01-01T00:00:00Z', datetime.timezone(datetime.timedelta(seconds=16200)))
        self.assertEqual(datetime.timezone(datetime.timedelta(seconds=16200)), actual.tzinfo)
        self.assertEqual('2000-01-01T04:30:00+04:30', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')

    def test_new_iso_tokyo_default(self):
        actual = ZoneDateTime('2000-01-01T00:00:00+09:00')
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
            self.assertEqual('2000-01-01T00:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_iso_tokyo_none(self):
        actual = ZoneDateTime('2000-01-01T00:00:00+09:00', None)
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
            self.assertEqual('2000-01-01T00:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_iso_tokyo_utc_sqlite(self):
        actual = ZoneDateTime('2000-01-01 00:00:00+09:00', datetime.timezone.utc)
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual('1999-12-31T15:00:00+00:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_iso_tokyo_utc_iso(self):
        actual = ZoneDateTime('2000-01-01T00:00:00+09:00', datetime.timezone.utc)
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual('1999-12-31T15:00:00+00:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_iso_tokyo_timedelta_32400(self):
        actual = ZoneDateTime('2000-01-01T00:00:00+09:00', datetime.timezone(datetime.timedelta(seconds=32400)))
        self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
        self.assertEqual('2000-01-01T00:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_iso_tokyo_zoneinfo(self):
        actual = ZoneDateTime('2000-01-01T00:00:00+09:00', zoneinfo.ZoneInfo('Asia/Tokyo'))
        self.assertEqual(zoneinfo.ZoneInfo('Asia/Tokyo'), actual.tzinfo)
        self.assertEqual('2000-01-01T00:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_iso_tokyo_timedelta_16200(self):
        actual = ZoneDateTime('2000-01-01T00:00:00+09:00', datetime.timezone(datetime.timedelta(seconds=16200)))
        self.assertEqual(datetime.timezone(datetime.timedelta(seconds=16200)), actual.tzinfo)
        self.assertEqual('1999-12-31T19:30:00+04:30', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')

    def test_new_datetime_native_default(self):
        actual = ZoneDateTime(datetime.datetime.fromisoformat('2000-01-01T00:00:00'))
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
            self.assertEqual('2000-01-01T00:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_datetime_native_none(self):
        actual = ZoneDateTime(datetime.datetime.fromisoformat('2000-01-01T00:00:00'), None)
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
            self.assertEqual('2000-01-01T00:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_datetime_native_utc(self):
        actual = ZoneDateTime(datetime.datetime.fromisoformat('2000-01-01 00:00:00'), datetime.timezone.utc)
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual('1999-12-31T15:00:00+00:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_datetime_native_timedelta_32400(self):
        actual = ZoneDateTime(datetime.datetime.fromisoformat('2000-01-01 00:00:00'), datetime.timezone(datetime.timedelta(seconds=32400)))
        self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
        self.assertEqual('2000-01-01T00:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_datetime_native_zoneinfo(self):
        actual = ZoneDateTime(datetime.datetime.fromisoformat('2000-01-01 00:00:00'), zoneinfo.ZoneInfo('Asia/Tokyo'))
        self.assertEqual(zoneinfo.ZoneInfo('Asia/Tokyo'), actual.tzinfo)
        self.assertEqual('2000-01-01T00:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_datetime_native_timedelta_16200(self):
        actual = ZoneDateTime(datetime.datetime.fromisoformat('2000-01-01 00:00:00'), datetime.timezone(datetime.timedelta(seconds=16200)))
        self.assertEqual(datetime.timezone(datetime.timedelta(seconds=16200)), actual.tzinfo)
        self.assertEqual('1999-12-31T19:30:00+04:30', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')

    def test_new_datetime_utc_iso_default(self):
        actual = ZoneDateTime(datetime.datetime.fromisoformat('2000-01-01T00:00:00+00:00'))
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
            self.assertEqual('2000-01-01T09:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_datetime_utc_iso_none(self):
        actual = ZoneDateTime(datetime.datetime.fromisoformat('2000-01-01T00:00:00+00:00'), None)
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
            self.assertEqual('2000-01-01T09:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_datetime_utc_iso_utc(self):
        actual = ZoneDateTime(datetime.datetime.fromisoformat('2000-01-01 00:00:00+00:00'), datetime.timezone.utc)
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual('2000-01-01T00:00:00+00:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_datetime_utc_iso_timedelta_32400(self):
        actual = ZoneDateTime(datetime.datetime.fromisoformat('2000-01-01 00:00:00+00:00'), datetime.timezone(datetime.timedelta(seconds=32400)))
        self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
        self.assertEqual('2000-01-01T09:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_datetime_utc_iso_zoneinfo(self):
        actual = ZoneDateTime(datetime.datetime.fromisoformat('2000-01-01 00:00:00+00:00'), zoneinfo.ZoneInfo('Asia/Tokyo'))
        self.assertEqual(zoneinfo.ZoneInfo('Asia/Tokyo'), actual.tzinfo)
        self.assertEqual('2000-01-01T09:00:00+09:00', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')
    def test_new_datetime_utc_iso_timedelta_16200(self):
        actual = ZoneDateTime(datetime.datetime.fromisoformat('2000-01-01 00:00:00+00:00'), datetime.timezone(datetime.timedelta(seconds=16200)))
        self.assertEqual(datetime.timezone(datetime.timedelta(seconds=16200)), actual.tzinfo)
        self.assertEqual('2000-01-01T04:30:00+04:30', f'{actual:%Y-%m-%dT%H:%M:%S}{TimeZone.iso(actual)}')

    def test_to_iso_native(self):
        actual = ZoneDateTime('2000-01-01 00:00:00').to_iso()
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual('2000-01-01T00:00:00+09:00', actual)
    def test_to_iso_utc_z(self):
        actual = ZoneDateTime('2000-01-01T00:00:00Z').to_iso()
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual('2000-01-01T09:00:00+09:00', actual)
    def test_to_iso_utc(self):
        actual = ZoneDateTime('2000-01-01T00:00:00+00:00').to_iso()
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual('2000-01-01T09:00:00+09:00', actual)
    def test_to_iso_tokyo(self):
        actual = ZoneDateTime('2000-01-01T00:00:00+09:00').to_iso()
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual('2000-01-01T00:00:00+09:00', actual)

    def test_to_sqlite_native(self):
        actual = ZoneDateTime('2000-01-01 00:00:00').to_sqlite()
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual('1999-12-31 15:00:00', actual)
    def test_to_sqlite_utc_z(self):
        actual = ZoneDateTime('2000-01-01T00:00:00Z').to_sqlite()
        self.assertEqual('2000-01-01 00:00:00', actual)
    def test_to_sqlite_utc(self):
        actual = ZoneDateTime('2000-01-01T00:00:00+00:00').to_sqlite()
        self.assertEqual('2000-01-01 00:00:00', actual)
    def test_to_sqlite_tokyo(self):
        actual = ZoneDateTime('2000-01-01T00:00:00+09:00').to_sqlite()
        self.assertEqual('1999-12-31 15:00:00', actual)


if __name__ == '__main__':
    unittest.main()

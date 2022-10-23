#!/usr/bin/env python3
# coding: utf8
import unittest
import importlib  
UtcDateTime = importlib.import_module('utc-date-time').UtcDateTime
import datetime, zoneinfo # <=3.9
class TestUtcDateTime(unittest.TestCase):
    def setUp(self): pass
    def tearDown(self): pass
    def test_new_type(self):
        actual = UtcDateTime()
        self.assertEqual(UtcDateTime, type(actual))
    def test_new_default(self):
        actual = UtcDateTime()
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
    def test_new_none(self):
        actual = UtcDateTime(None)
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
    def test_new_iso_native(self):
        actual = UtcDateTime('2000-01-01 00:00:00')
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual('1999-12-31T15:00:00+0000', f'{actual:%Y-%m-%dT%H:%M:%S%z}')
        actual = UtcDateTime('2000-01-01T00:00:00')
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual('1999-12-31T15:00:00+0000', f'{actual:%Y-%m-%dT%H:%M:%S%z}')
    def test_new_iso_utc(self):
        actual = UtcDateTime('2000-01-01T00:00:00+00:00')
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual('2000-01-01T00:00:00+0000', f'{actual:%Y-%m-%dT%H:%M:%S%z}')
    def test_new_iso_utc_z(self):
        actual = UtcDateTime('2000-01-01T00:00:00Z')
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual('2000-01-01T00:00:00+0000', f'{actual:%Y-%m-%dT%H:%M:%S%z}')
    def test_new_iso_tokyo(self):
        actual = UtcDateTime('2000-01-01T00:00:00+09:00')
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual('1999-12-31T15:00:00+0000', f'{actual:%Y-%m-%dT%H:%M:%S%z}')
    def test_new_datetime_native(self):
        actual = UtcDateTime(datetime.datetime.now())
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
    def test_new_datetime_utc_timezone(self):
        actual = UtcDateTime(datetime.datetime.now(datetime.timezone.utc))
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
    def test_new_datetime_utc_timedelta(self):
        actual = UtcDateTime(datetime.datetime.now(datetime.timezone(datetime.timedelta(seconds=0))))
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
    def test_new_datetime_utc_zoneinf(self):
        actual = UtcDateTime(datetime.datetime.now(zoneinfo.ZoneInfo('UTC')))
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
    def test_new_datetime_tokyo_timedelta(self):
        actual = UtcDateTime(datetime.datetime.now(datetime.timezone(datetime.timedelta(seconds=32400))))
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
    def test_new_datetime_tokyo_zoneinf(self):
        actual = UtcDateTime(datetime.datetime.now(zoneinfo.ZoneInfo('Asia/Tokyo')))
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)

    def test_to_iso_native(self):
        actual = UtcDateTime('2000-01-01 00:00:00').to_iso()
        if datetime.datetime.now().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual('1999-12-31T15:00:00+00:00', actual)
    def test_to_iso_utc_z(self):
        actual = UtcDateTime('2000-01-01T00:00:00Z').to_iso()
        self.assertEqual('2000-01-01T00:00:00+00:00', actual)
    def test_to_iso_utc(self):
        actual = UtcDateTime('2000-01-01T00:00:00+00:00').to_iso()
        self.assertEqual('2000-01-01T00:00:00+00:00', actual)
    def test_to_iso_tokyo(self):
        actual = UtcDateTime('2000-01-01T00:00:00+09:00').to_iso()
        self.assertEqual('1999-12-31T15:00:00+00:00', actual)

    def test_to_isoz_native(self):
        actual = UtcDateTime('2000-01-01 00:00:00').to_isoz()
        if datetime.datetime.now().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual('1999-12-31T15:00:00Z', actual)
    def test_to_isoz_utc_z(self):
        actual = UtcDateTime('2000-01-01T00:00:00Z').to_isoz()
        self.assertEqual('2000-01-01T00:00:00Z', actual)
    def test_to_isoz_utc(self):
        actual = UtcDateTime('2000-01-01T00:00:00+00:00').to_isoz()
        self.assertEqual('2000-01-01T00:00:00Z', actual)
    def test_to_isoz_tokyo(self):
        actual = UtcDateTime('2000-01-01T00:00:00+09:00').to_isoz()
        self.assertEqual('1999-12-31T15:00:00Z', actual)

    def test_to_sqlite_native(self):
        actual = UtcDateTime('2000-01-01 00:00:00').to_sqlite()
        if datetime.datetime.now().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual('1999-12-31 15:00:00', actual)
    def test_to_sqlite_utc_z(self):
        actual = UtcDateTime('2000-01-01T00:00:00Z').to_sqlite()
        self.assertEqual('2000-01-01 00:00:00', actual)
    def test_to_sqlite_utc(self):
        actual = UtcDateTime('2000-01-01T00:00:00+00:00').to_sqlite()
        self.assertEqual('2000-01-01 00:00:00', actual)
    def test_to_sqlite_tokyo(self):
        actual = UtcDateTime('2000-01-01T00:00:00+09:00').to_sqlite()
        self.assertEqual('1999-12-31 15:00:00', actual)


if __name__ == '__main__':
    unittest.main()

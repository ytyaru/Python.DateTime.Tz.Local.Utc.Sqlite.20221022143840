#!/usr/bin/env python3
# coding: utf8
import unittest
import importlib  
SQLiteDateTime = importlib.import_module('sqlite-date-time').SQLiteDateTime
import datetime, zoneinfo # <=3.9
class TestSQLiteDateTime(unittest.TestCase):
    def setUp(self): pass
    def tearDown(self): pass
    def test_new_type(self):
        actual = SQLiteDateTime()
        self.assertEqual(SQLiteDateTime, type(actual))
    def test_new_default(self):
        actual = SQLiteDateTime()
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
    def test_new_none(self):
        actual = SQLiteDateTime(None)
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
    def test_new_iso_native(self):
        actual = SQLiteDateTime('2000-01-01 00:00:00')
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual('2000-01-01T00:00:00+0000', f'{actual:%Y-%m-%dT%H:%M:%S%z}')
    def test_new_iso_utc(self):
        actual = SQLiteDateTime('2000-01-01T00:00:00+00:00')
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual('2000-01-01T00:00:00+0000', f'{actual:%Y-%m-%dT%H:%M:%S%z}')
    def test_new_iso_utc_z(self):
        actual = SQLiteDateTime('2000-01-01T00:00:00Z')
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual('2000-01-01T00:00:00+0000', f'{actual:%Y-%m-%dT%H:%M:%S%z}')
    """
    """
    def test_new_iso_tokyo(self):
        actual = SQLiteDateTime('2000-01-01T00:00:00+09:00')
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual('1999-12-31T15:00:00+0000', f'{actual:%Y-%m-%dT%H:%M:%S%z}')
        #self.assertEqual('2000-01-01T00:00:00+0000', f'{actual:%Y-%m-%dT%H:%M:%S%z}')
    """
    """
    def test_new_datetime_native(self):
        actual = SQLiteDateTime(datetime.datetime.now())
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
    def test_new_datetime_utc_timezone(self):
        actual = SQLiteDateTime(datetime.datetime.now(datetime.timezone.utc))
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
    def test_new_datetime_utc_timedelta(self):
        actual = SQLiteDateTime(datetime.datetime.now(datetime.timezone(datetime.timedelta(seconds=0))))
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
    def test_new_datetime_utc_zoneinf(self):
        actual = SQLiteDateTime(datetime.datetime.now(zoneinfo.ZoneInfo('UTC')))
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
    def test_new_datetime_tokyo_timedelta(self):
        actual = SQLiteDateTime(datetime.datetime.now(datetime.timezone(datetime.timedelta(seconds=32400))))
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
    def test_new_datetime_tokyo_zoneinf(self):
        actual = SQLiteDateTime(datetime.datetime.now(zoneinfo.ZoneInfo('Asia/Tokyo')))
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)

    def test_to_iso_native(self):
        actual = SQLiteDateTime('2000-01-01 00:00:00').to_iso()
        if datetime.datetime.now().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual('1999-12-31T15:00:00+00:00', actual)
    def test_to_iso_utc_z(self):
        actual = SQLiteDateTime('2000-01-01T00:00:00Z').to_iso()
        self.assertEqual('2000-01-01T00:00:00+00:00', actual)
    def test_to_iso_utc(self):
        actual = SQLiteDateTime('2000-01-01T00:00:00+00:00').to_iso()
        self.assertEqual('2000-01-01T00:00:00+00:00', actual)
    def test_to_iso_tokyo(self):
        actual = SQLiteDateTime('2000-01-01T00:00:00+09:00').to_iso()
        self.assertEqual('1999-12-31T15:00:00+00:00', actual)

    def test_to_isoz_native(self):
        actual = SQLiteDateTime('2000-01-01 00:00:00').to_isoz()
        if datetime.datetime.now().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual('1999-12-31T15:00:00Z', actual)
    def test_to_isoz_utc_z(self):
        actual = SQLiteDateTime('2000-01-01T00:00:00Z').to_isoz()
        self.assertEqual('2000-01-01T00:00:00Z', actual)
    def test_to_isoz_utc(self):
        actual = SQLiteDateTime('2000-01-01T00:00:00+00:00').to_isoz()
        self.assertEqual('2000-01-01T00:00:00Z', actual)
    def test_to_isoz_tokyo(self):
        actual = SQLiteDateTime('2000-01-01T00:00:00+09:00').to_isoz()
        self.assertEqual('1999-12-31T15:00:00Z', actual)

    def test_to_sqlite_native(self):
        actual = SQLiteDateTime('2000-01-01 00:00:00').to_sqlite()
        if datetime.datetime.now().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual('1999-12-31 15:00:00', actual)
    def test_to_sqlite_utc_z(self):
        actual = SQLiteDateTime('2000-01-01T00:00:00Z').to_sqlite()
        self.assertEqual('2000-01-01 00:00:00', actual)
    def test_to_sqlite_utc(self):
        actual = SQLiteDateTime('2000-01-01T00:00:00+00:00').to_sqlite()
        self.assertEqual('2000-01-01 00:00:00', actual)
    def test_to_sqlite_tokyo(self):
        actual = SQLiteDateTime('2000-01-01T00:00:00+09:00').to_sqlite()
        self.assertEqual('1999-12-31 15:00:00', actual)
    
    def test_to_local(self):
        actual = SQLiteDateTime('2000-01-01T00:00:00').to_local()
        if datetime.datetime.now().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual('2000-01-01T09:00:00+0900', f'{actual:%Y-%m-%dT%H:%M:%S%z}')
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
    def test_to_tz_timedelta(self):
        actual = SQLiteDateTime('2000-01-01T00:00:00').to_tz(datetime.timezone(datetime.timedelta(seconds=32400)))
        self.assertEqual('2000-01-01T09:00:00+0900', f'{actual:%Y-%m-%dT%H:%M:%S%z}')
        self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
    def test_to_tz_zoneinfo(self):
        actual = SQLiteDateTime('2000-01-01T00:00:00').to_tz(zoneinfo.ZoneInfo('Asia/Tokyo'))
        self.assertEqual('2000-01-01T09:00:00+0900', f'{actual:%Y-%m-%dT%H:%M:%S%z}')
        self.assertEqual(zoneinfo.ZoneInfo('Asia/Tokyo'), actual.tzinfo)
    """
    """


if __name__ == '__main__':
    unittest.main()

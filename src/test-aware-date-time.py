#!/usr/bin/env python3
# coding: utf8
import unittest
import importlib  
AwareDateTime = importlib.import_module('aware-date-time').AwareDateTime 
import datetime, zoneinfo # <=3.9
import os
class TestAwareDateTime(unittest.TestCase):
    def setUp(self): pass
    def tearDown(self): pass
    def test_is_native_true(self):
        self.assertTrue(AwareDateTime.is_native(datetime.datetime.now()))
    def test_is_native_false(self):
        self.assertFalse(AwareDateTime.is_native(datetime.datetime.now(datetime.timezone.utc)))
    def test_is_aware_true(self):
        self.assertTrue(AwareDateTime.is_aware(datetime.datetime.now(datetime.timezone.utc)))
    def test_is_aware_false(self):
        self.assertFalse(AwareDateTime.is_aware(datetime.datetime.now()))
    def test_to_utc_native(self):
        actual = AwareDateTime.to_utc(datetime.datetime.fromisoformat('2000-01-01T00:00:00'))
        #actual = AwareDateTime.to_utc(datetime.datetime.now())
        if actual.tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(datetime.timezone.utc, actual.tzinfo)
            self.assertEqual("1999-12-31T15:00:00+0000", f"{actual:%Y-%m-%dT%H:%M:%S%z}")
            self.assertEqual(15, actual.hour)
            self.assertEqual(0, actual.minute)
            self.assertEqual(0, actual.second)
            self.assertEqual(31, actual.day)
            self.assertEqual(12, actual.month)
            self.assertEqual(1999, actual.year)
    def test_to_utc_utc(self):
        #actual = AwareDateTime.to_utc(datetime.datetime.now(datetime.timezone.utc))
        actual = AwareDateTime.to_utc(datetime.datetime.fromisoformat('2000-01-01T00:00:00+00:00'))
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual("2000-01-01T00:00:00+0000", f"{actual:%Y-%m-%dT%H:%M:%S%z}")
        self.assertEqual(0, actual.hour)
        self.assertEqual(0, actual.minute)
        self.assertEqual(0, actual.second)
        self.assertEqual(1, actual.day)
        self.assertEqual(1, actual.month)
        self.assertEqual(2000, actual.year)
    def test_to_utc_tokyo(self):
        actual = AwareDateTime.to_utc(datetime.datetime.fromisoformat('2000-01-01T00:00:00+09:00'))
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual("1999-12-31T15:00:00+0000", f"{actual:%Y-%m-%dT%H:%M:%S%z}")
        self.assertEqual(15, actual.hour)
        self.assertEqual(0, actual.minute)
        self.assertEqual(0, actual.second)
        self.assertEqual(31, actual.day)
        self.assertEqual(12, actual.month)
        self.assertEqual(1999, actual.year)
    def test_to_local_utc(self):
        actual = AwareDateTime.to_local(datetime.datetime.fromisoformat('2000-01-01T00:00:00+00:00'))
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
    def test_to_local_tokyo(self):
        actual = AwareDateTime.to_local(datetime.datetime.fromisoformat('2000-01-01T00:00:00+09:00'))
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
    def test_to_local_native(self):
        actual = AwareDateTime.to_local(datetime.datetime.fromisoformat('2000-01-01T00:00:00'))
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
    def test_to_tz_tokyo_utc(self):
        actual = AwareDateTime.to_tz(
            datetime.datetime.fromisoformat('2000-01-01T00:00:00+09:00'), 
            datetime.timezone.utc)
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual("1999-12-31T15:00:00+0000", f"{actual:%Y-%m-%dT%H:%M:%S%z}")
    def test_to_tz_tokyo_native(self):
        actual = AwareDateTime.to_tz(
            datetime.datetime.fromisoformat('2000-01-01T00:00:00+09:00'), 
            None)
        #self.assertEqual(None, actual.tzinfo)
        self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400), 'JST'), actual.tzinfo)
        self.assertEqual("2000-01-01T00:00:00+0900", f"{actual:%Y-%m-%dT%H:%M:%S%z}")
    def test_to_tz_tokyo_tokyo(self):
        actual = AwareDateTime.to_tz(
            datetime.datetime.fromisoformat('2000-01-01T00:00:00+09:00'), 
            datetime.timezone(datetime.timedelta(seconds=32400)))
        self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
        self.assertEqual("2000-01-01T00:00:00+0900", f"{actual:%Y-%m-%dT%H:%M:%S%z}")
    def test_to_tz_utc_tokyo(self):
        actual = AwareDateTime.to_tz(
            datetime.datetime.fromisoformat('2000-01-01T00:00:00+00:00'), 
            datetime.timezone(datetime.timedelta(seconds=32400)))
        self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
        self.assertEqual("2000-01-01T09:00:00+0900", f"{actual:%Y-%m-%dT%H:%M:%S%z}")
    def test_to_tz_utc_native(self):
        actual = AwareDateTime.to_tz(
            datetime.datetime.fromisoformat('2000-01-01T00:00:00+00:00'), 
            None)
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
            self.assertEqual("2000-01-01T09:00:00+0900", f"{actual:%Y-%m-%dT%H:%M:%S%z}")
    def test_to_tz_native_tokyo_timedelta(self):
        actual = AwareDateTime.to_tz(
            datetime.datetime.fromisoformat('2000-01-01T00:00:00'), 
            datetime.timezone(datetime.timedelta(seconds=32400)))
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            #self.assertEqual(datetime.timedelta(seconds=32400), actual.tzinfo)
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400), 'JST'), actual.tzinfo)
            self.assertEqual(datetime.timezone, type(actual.tzinfo))
            self.assertEqual(32400, actual.tzinfo.utcoffset(actual).seconds)
            self.assertEqual("2000-01-01T00:00:00+0900", f"{actual:%Y-%m-%dT%H:%M:%S%z}")
    def test_to_tz_native_tokyo_zoneinfo(self):
        actual = AwareDateTime.to_tz(
            datetime.datetime.fromisoformat('2000-01-01T00:00:00+00:00'), 
            zoneinfo.ZoneInfo('Asia/Tokyo'))
        self.assertEqual(zoneinfo.ZoneInfo('Asia/Tokyo'), actual.tzinfo)
        self.assertEqual(zoneinfo.ZoneInfo, type(actual.tzinfo))
        self.assertEqual(32400, actual.tzinfo.utcoffset(actual).seconds)
    def test_if_native_to_utc_native(self):
        actual = AwareDateTime.if_native_to_utc(datetime.datetime.fromisoformat('2000-01-01T00:00:00'))
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual("1999-12-31T15:00:00+0000", f"{actual:%Y-%m-%dT%H:%M:%S%z}")
    def test_if_native_to_utc_utc(self):
        actual = AwareDateTime.if_native_to_utc(datetime.datetime.fromisoformat('2000-01-01T00:00:00+00:00'))
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual("2000-01-01T00:00:00+0000", f"{actual:%Y-%m-%dT%H:%M:%S%z}")
    def test_if_native_to_utc_tokyo(self):
        actual = AwareDateTime.if_native_to_utc(datetime.datetime.fromisoformat('2000-01-01T00:00:00+09:00'))
        self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
        self.assertEqual("2000-01-01T00:00:00+0900", f"{actual:%Y-%m-%dT%H:%M:%S%z}")
    def test_if_native_to_tz_native_utc(self):
        actual = AwareDateTime.if_native_to_tz(datetime.datetime.fromisoformat('2000-01-01T00:00:00'), datetime.timezone.utc)
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual("1999-12-31T15:00:00+0000", f"{actual:%Y-%m-%dT%H:%M:%S%z}")
    def test_if_native_to_tz_native_tokyo(self):
        actual = AwareDateTime.if_native_to_tz(datetime.datetime.fromisoformat('2000-01-01T00:00:00'), datetime.timezone(datetime.timedelta(seconds=32400)))
        self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), actual.tzinfo)
        self.assertEqual("2000-01-01T00:00:00+0900", f"{actual:%Y-%m-%dT%H:%M:%S%z}")
    def test_if_native_to_tz_utc_tokyo(self):
        actual = AwareDateTime.if_native_to_tz(datetime.datetime.fromisoformat('2000-01-01T00:00:00+00:00'), datetime.timezone(datetime.timedelta(seconds=32400)))
        self.assertEqual(datetime.timezone.utc, actual.tzinfo)
        self.assertEqual("2000-01-01T00:00:00+0000", f"{actual:%Y-%m-%dT%H:%M:%S%z}")

    """
    def test_local_tz(self):
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), AwareDateTime.local_tz())
    def test_tz_sec_default(self):
        actual = AwareDateTime.tz_sec()
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(32400, actual)
    def test_tz_sec_none(self):
        actual = AwareDateTime.tz_sec(None)
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(32400, actual)
    def test_tz_sec_timezone(self):
        actual = AwareDateTime.tz_sec(datetime.timezone(datetime.timedelta(seconds=16200)))
        self.assertEqual(16200, actual)
    def test_tz_sec_utc(self):
        actual = AwareDateTime.tz_sec(datetime.datetime.fromisoformat('2000-01-01T00:00:00+00:00'))
        self.assertEqual(0, actual)
    def test_tz_sec_native(self):
        actual = AwareDateTime.tz_sec(datetime.datetime.fromisoformat('2000-01-01T00:00:00'))
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(32400, actual)
    def test_tz_sec_tokyo(self):
        actual = AwareDateTime.tz_sec(datetime.datetime.fromisoformat('2000-01-01T00:00:00+09:00'))
        self.assertEqual(32400, actual)
    def test_tz_iso_utc(self):
        actual = AwareDateTime.tz_iso(datetime.datetime.fromisoformat('2000-01-01T00:00:00+00:00'))
        self.assertEqual('+00:00', actual)
    def test_tz_iso_native(self):
        actual = AwareDateTime.tz_iso(datetime.datetime.fromisoformat('2000-01-01T00:00:00'))
        if datetime.datetime.now().astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual('+09:00', actual)
    def test_tz_iso_tokyo(self):
        actual = AwareDateTime.tz_iso(datetime.datetime.fromisoformat('2000-01-01T00:00:00+09:00'))
        self.assertEqual('+09:00', actual)
    """


if __name__ == '__main__':
    unittest.main()

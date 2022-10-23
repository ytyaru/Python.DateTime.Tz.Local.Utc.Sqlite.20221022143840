#!/usr/bin/env python3
# coding: utf8
import unittest
import importlib  
TimeZone = importlib.import_module('time-zone').TimeZone
import datetime, zoneinfo # <=3.9
class TestTimeZone(unittest.TestCase):
    def setUp(self): pass
    def tearDown(self): pass
    def test_local(self):
        if datetime.datetime.now().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(datetime.timezone(datetime.timedelta(seconds=32400)), TimeZone.local())

    def test_sec_default(self):
        actual = TimeZone.sec()
        if datetime.datetime.now().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(32400, actual)
    def test_sec_none(self):
        actual = TimeZone.sec(None)
        if datetime.datetime.now().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(32400, actual)
    def test_sec_iso_native(self):
        actual = TimeZone.sec(datetime.datetime.fromisoformat('2000-01-01T00:00:00'))
        if datetime.datetime.now().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual(32400, actual)
    def test_sec_iso_utc(self):
        actual = TimeZone.sec(datetime.datetime.fromisoformat('2000-01-01T00:00:00+00:00'))
        self.assertEqual(0, actual)
    def test_sec_iso_tokyo(self):
        actual = TimeZone.sec(datetime.datetime.fromisoformat('2000-01-01T00:00:00+09:00'))
        self.assertEqual(32400, actual)
    def test_sec_timezone_timedelta(self):
        actual = TimeZone.sec(datetime.timezone(datetime.timedelta(seconds=16200)))
        self.assertEqual(16200, actual)
    def test_sec_zoneinfo_tokyo(self):
        actual = TimeZone.sec(zoneinfo.ZoneInfo('Asia/Tokyo'))
        self.assertEqual(32400, actual)

    def test_iso_default(self):
        actual = TimeZone.iso()
        if datetime.datetime.now().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual('+09:00', actual)
    def test_iso_none(self):
        actual = TimeZone.iso(None)
        if datetime.datetime.now().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual('+09:00', actual)
    def test_iso_iso_native(self):
        actual = TimeZone.iso(datetime.datetime.fromisoformat('2000-01-01T00:00:00'))
        if datetime.datetime.now().tzinfo == datetime.timezone(datetime.timedelta(seconds=32400)):
            self.assertEqual('+09:00', actual)
    def test_iso_iso_utc(self):
        actual = TimeZone.iso(datetime.datetime.fromisoformat('2000-01-01T00:00:00+00:00'))
        self.assertEqual('+00:00', actual)
    def test_iso_iso_tokyo(self):
        actual = TimeZone.iso(datetime.datetime.fromisoformat('2000-01-01T00:00:00+09:00'))
        self.assertEqual('+09:00', actual)
    def test_iso_timezone_timedelta(self):
        actual = TimeZone.iso(datetime.timezone(datetime.timedelta(seconds=16200)))
        self.assertEqual('+04:30', actual)
    def test_iso_zoneinfo_tokyo(self):
        actual = TimeZone.iso(zoneinfo.ZoneInfo('Asia/Tokyo'))
        self.assertEqual('+09:00', actual)

    def test_gets(self):
        actual = TimeZone.gets()
        tokyo = list(filter(lambda tz:tz.name=='Asia/Tokyo', actual))[0]
        self.assertEqual('+09:00', tokyo.iso)
        self.assertEqual(32400, tokyo.seconds)
        self.assertEqual('Asia/Tokyo', tokyo.name)
    def test_search_tokyo(self):
        tokyo = TimeZone.search('Asia/Tokyo')[0]
        self.assertEqual('+09:00', tokyo.iso)
        self.assertEqual(32400, tokyo.seconds)
        self.assertEqual('Asia/Tokyo', tokyo.name)
    def test_search_asia(self):
        actual = TimeZone.search('Asia/')
        self.assertTrue(2 < len(actual))
        self.assertTrue(len(actual) < 600)
    def test_search_32400(self):
        actual = TimeZone.search(32400)
        self.assertTrue(2 < len(actual))
        self.assertTrue(len(actual) < 600)
    def test_search_iso(self):
        actual = TimeZone.search('+09:00')
        self.assertTrue(2 < len(actual))
        self.assertTrue(len(actual) < 600)
#    def test_make_tsv(self):
#        TimeZone.make_tsv()


if __name__ == '__main__':
    unittest.main()

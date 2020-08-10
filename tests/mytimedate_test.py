import unittest
import datetime
from mydatetime import *

class TestMytime(unittest.TestCase):
	def test_closestDateWithDay(self):
		self.assertEqual(closestDateWithDay(datetime.date(2018, 1, 5), 10), datetime.date(2018, 1, 10))
		self.assertEqual(closestDateWithDay(datetime.date(2018, 1, 5), 5), datetime.date(2018, 1, 5))
		self.assertEqual(closestDateWithDay(datetime.date(2018, 1, 5), 4), datetime.date(2018, 2, 4))
		self.assertEqual(closestDateWithDay(datetime.date(2017, 12, 5), 4), datetime.date(2018, 1, 4))

	def test_closestDateWithDayAndMonth(self):
		self.assertEqual(closestDateWithDayAndMonth(datetime.date(2017, 12, 5), 4, 12), datetime.date(2018, 1, 4))
		self.assertEqual(closestDateWithDayAndMonth(datetime.date(2017, 12, 5), 4, 3), datetime.date(2018, 3, 4))
		self.assertEqual(closestDateWithDayAndMonth(datetime.date(2017, 10, 5), 4, 11), datetime.date(2017, 11, 4))

	def test_weekdayNumberToDate(self):
		self.assertEqual(weekdayNumberToDate(datetime.date(2018, 1, 5), 1), datetime.date(2018, 1, 8))
		self.assertEqual(weekdayNumberToDate(datetime.date(2018, 1, 5), 7), datetime.date(2018, 1, 7))
		self.assertEqual(weekdayNumberToDate(datetime.date(2018, 1, 31), 6), datetime.date(2018, 2, 3))
		self.assertEqual(weekdayNumberToDate(datetime.date(2017, 12, 30), 3), datetime.date(2018, 1, 3))

	def test_strWeekdayToNumber(self):
		self.assertEqual(strWeekdayToNumber("пятницу"), 5)
		self.assertEqual(strWeekdayToNumber("пятница"), None)
		self.assertEqual(strWeekdayToNumber("понедельник"), 1)


	def test_strDateToDate(self):
		self.assertEqual(strDateToDate(datetime.date(2018, 1, 5), "6"), datetime.date(2018, 1, 6))
		self.assertEqual(strDateToDate(datetime.date(2018, 1, 5), "6.04"), datetime.date(2018, 4, 6))
		self.assertEqual(strDateToDate(datetime.date(2018, 1, 5), "6.04.2019"), datetime.date(2019, 4, 6))
		self.assertEqual(strDateToDate(datetime.date(2018, 1, 5), "субботу"), datetime.date(2018, 1, 6))
		self.assertEqual(strDateToDate(datetime.date(2018, 1, 1), "позавчера"), datetime.date(2017, 12, 30))
		self.assertEqual(strDateToDate(datetime.date(2018, 1, 1), "6,5"), None)


	def test_dateToStr(self):
		date = datetime.date(2018, 1, 11)
		self.assertEqual(dateToStr(date), '11.01.2018')
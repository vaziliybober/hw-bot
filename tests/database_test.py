import unittest
from database import Database
import datetime
from kurchat10z_config import *
from record import Record

db = Database('tests/test_database.pickle', class_)

class TestDatabase(unittest.TestCase):

	def test_read(self):
		date = datetime.date(2018, 1, 11)
		subject = algebra
		group = ptGroup1
		pupil = veronikaAvdeeva
		record = Record(date, subject, group, pupil, 'test', 'attach')
		db.add(record)
		db.remove(date, subject, group, pupil)
		self.assertEqual(db.read(date, subject, group), [])
		db.add(record)
		db.add(record)
		self.assertEqual(db.read(date, subject, group), [record])
		group2 = ptGroup2
		pupil2 = alyaVlasenkova
		record2 = Record(date, subject, group, pupil2, 'test2', 'attach2')
		db.add(record2)
		self.assertIn(db.read(date, subject, group), [[record, record2], [record2, record]])
		pupil3 = vasiliyBobrov
		record3 = Record(date, subject, group2, pupil3, 'test3', 'attach3')
		db.add(record3)
		self.assertEqual(db.read(date, subject, group2), [record3])
		db.remove(date, subject, group, pupil2)
		db.remove(date, subject, group2, pupil3)

	def test_dates(self):
		date = datetime.date(2018, 1, 11)
		subject = algebra
		group = ptGroup1
		pupil = veronikaAvdeeva
		record = Record(date, subject, group, pupil, 'test', 'attach')
		db.add(record)
		pupil2 = alyaVlasenkova
		record2 = Record(date, subject, group, pupil2, 'test2', 'attach2')
		db.add(record2)
		self.assertEqual(db.dates(), [date])
		db.remove(date, subject, group, pupil)
		db.remove(date, subject, group, pupil2)

	def test_subjects(self):
		date = datetime.date(2018, 1, 11)
		subject = algebra
		group = ptGroup1
		pupil = veronikaAvdeeva
		record = Record(date, subject, group, pupil, 'test', 'attach')
		db.add(record)
		pupil2 = alyaVlasenkova
		record2 = Record(date, subject, group, pupil2, 'test2', 'attach2')
		db.add(record2)
		self.assertEqual(db.subjects(date), [algebra])
		db.remove(date, subject, group, pupil)
		db.remove(date, subject, group, pupil2)

	def test_groups(self):
		date = datetime.date(2018, 1, 11)
		subject = algebra
		group = ptGroup1
		pupil = veronikaAvdeeva
		record = Record(date, subject, group, pupil, 'test', 'attach')
		db.add(record)
		pupil2 = alyaVlasenkova
		record2 = Record(date, subject, group, pupil2, 'test2', 'attach2')
		db.add(record2)
		self.assertEqual(db.groups(date, subject), [group])
		db.remove(date, subject, group, pupil)
		db.remove(date, subject, group, pupil2)


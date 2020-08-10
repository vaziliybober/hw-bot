import pickle
from mydatetime import dateToStr, strDateToDate
import datetime


class Database:
	def __init__(self, filename, class_):
		self._filename = filename
		self._class = class_
		self.validate = self.validateGroup
		try:
			with open(self._filename, 'rb') as file:
				self._dict = pickle.load(file)
		except FileNotFoundError:
			with open(self._filename, 'wb') as file:
				pickle.dump({}, file)
			self._dict = {}

	def filename(self):
		return self._filename

	def class_(self):
		return self._class

	
	def keyExists(self, dict_, key):
		try:
			dict_[key]
		except KeyError:
			return False
		else:
			return True

	def validateKey(self, dict_, key):
		if not self.keyExists(dict_, key):
			dict_[key] = {}

	
	def validateDate(self, date):
		self.validateKey(self._dict, date)

	def validateSubject(self, date, subject):
		self.validateDate(date)
		self.validateKey(self._dict[date], subject)

	def validateGroup(self, date, subject, group):
		self.validateSubject(date, subject)
		self.validateKey(self._dict[date][subject], group)

	def add(self, r):
		date = dateToStr(r.date())
		subject = r.subject().name()
		group = r.group().name()
		pupil = r.pupil().uid()
		self.validate(date, subject, group)
		self._dict[date][subject][group][pupil] = r
		with open(self.filename(), 'wb') as file:
			pickle.dump(self._dict, file)


	def remove(self, date, subject, group, pupil):
		date = dateToStr(date)
		subject = subject.name()
		group = group.name()
		pupil = pupil.uid()

		try:
			self._dict[date][subject][group].pop(pupil)
			if not self._dict[date][subject][group].keys():
				self._dict[date][subject].pop(group)
			if not self._dict[date][subject].keys():
				self._dict[date].pop(subject)
			if not self._dict[date].keys():
				self._dict.pop(date)
		except KeyError:
			return False

		with open(self.filename(), 'wb') as file:
			pickle.dump(self._dict, file)

		return True

	def dates(self, subject=None):
		dates = [strDateToDate(datetime.date.today(), date) for date in self._dict.keys()]
		dates.sort()
		if not subject:
			return dates
		else:
			return [date for date in dates if self._dict[dateToStr(date)].get(subject.name())]

	def subjects(self, date):
		date = dateToStr(date)
		try:
			strSubjects = sorted(self._dict[date].keys())
		except KeyError:
			return []
		subjects = [self.class_().getSubject(subject) for subject in strSubjects]
		return subjects

	def groups(self, date, subject):
		date = dateToStr(date)
		if not self._dict.get(date) or not self._dict[date].get(subject.name()):
			return []
		strGroups = sorted(self._dict[date][subject.name()].keys())
		groups = [subject.getGroup(group) for group in strGroups]
		return groups

	def read(self, date, subject, group):
		date = dateToStr(date)
		subject = subject.name()
		group = group.name()
		
		try:
			items = self._dict[date][subject][group].items()
		except KeyError:
			return []

		records = []
		for uid, record in items:
			records.append(record)

		return records

	
	

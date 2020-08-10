

class Record:
	def __init__(self, date, subject, group, pupil, text, attachments):
		self._date = date
		self._subject = subject
		self._group = group
		self._pupil = pupil
		self._text = text
		self._attachments = attachments

	def date(self):
		return self._date

	def subject(self):
		return self._subject

	def group(self):
		return self._group

	def pupil(self):
		return self._pupil

	def text(self):
		return self._text

	def attachments(self):
		return self._attachments

	
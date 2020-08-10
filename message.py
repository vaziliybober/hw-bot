import mydatetime
import datetime

class Message:
	def __init__(self, text, subjects, today, hasAttachments):
		self._hasAttachments = hasAttachments

		text = text.strip().replace('<br>', '\n') # отсекаем пробельные символы по бокам

		self._gdzBeforeRemoval = False
		self.HW = False
		if text.lower().startswith('гдз'):
			self._gdzBeforeRemoval = True
			text = text[len('гдз'): ].strip()
			if text.lower().startswith('по'):
				text = text[len('по'): ].strip()


		if not self._gdzBeforeRemoval:
			self._subjectHWBeforeRemoval = text.lower().startswith('дз по ')
			if self._subjectHWBeforeRemoval:
				text = text[len('дз по'): ].strip()


			self.HW = text.lower().startswith('дз ') or text.lower() == 'дз'
			if self.HW:
				text = text[len('дз'): ].strip()	# отсекаем 'дз'



		self._subjectHWAfterRemoval = False
		self._gdzAfterRemoval = False
		self.REMOVAL = text.lower().startswith('удалить ')
		if self.REMOVAL:
			text = text[len('удалить'): ].strip() # отсекаем 'удалить'

			if text.lower().startswith('гдз'):
				self._gdzAfterRemoval = True
				text = text[len('гдз'): ].strip()
				if text.lower().startswith('по'):
					text = text[len('по'): ].strip()

			if not self._gdzAfterRemoval:
				self._subjectHWAfterRemoval = text.lower().startswith('дз по ')
				if self._subjectHWAfterRemoval:
					text = text[len('дз по'): ].strip()




		self.SUBJECT = None
		longestSubjectName = ""
		for subject in subjects:
			for name in subject.pseudonames() + [subject.name()]:
				name = name.lower()
				if text.lower().startswith(name + ' ') or text.lower() == name:
					if len(name) > len(longestSubjectName):
						longestSubjectName = name
						self.SUBJECT = subject
		text = text[len(longestSubjectName): ].strip()
		if self.HW and self.SUBJECT:
			self.HW = False


		if text.lower().startswith('на '):
			text = text[len('на'): ].strip() # отсекаем 'на'
			if text.split():
				possibleDate = text.lower().split()[0]
				self.DATE = mydatetime.strDateToDate(today, possibleDate)
				if self.DATE:
					text = text[len(possibleDate): ].strip()
			else:
				text = 'на ' + text # восстанавливаем 'на'
				self.DATE = None
		else:
			self.DATE = None


		self.CONTENT = text


	def hw(self):
		return self.HW
	def removal(self):
		return self.REMOVAL
	def subject(self):
		return self.SUBJECT
	def date(self):
		return self.DATE
	def content(self):
		return self.CONTENT
	def adding(self):
		return bool(not self.removal() and (self.content() or self._hasAttachments))
	def reading(self):
		return bool(not self.removal() and not self.adding())
	def gdz(self):
		return self._gdzBeforeRemoval or self._gdzAfterRemoval


	def errorReport(self):
		if self.gdz() and self.hw():
			return "О вы из Англии?"
		if self.adding():
			if not self.subject():
				return "Отсутствует предмет"
			if not self.date():
				return "Отсутствует дата"
			if self.hw():
				return "О вы из Англии?"

		elif self.removal():
			if not self.subject():
				return "Отсутствует предмет"
			if not self.date():
				return "Отсутствует дата"
			if self.hw():
				return "О вы из Англии?"
			if self._subjectHWBeforeRemoval or self._gdzBeforeRemoval:
				return "О вы из Англии?"

		elif self.reading():
			if not self.subject() and not self.hw() and not self.gdz():
				return "Отсутствует предмет"
			if self.subject() and self.hw():
				return "О вы из Англии?"
			if self.hw() and self._subjectHWBeforeRemoval:
				return "О вы из Англии?"







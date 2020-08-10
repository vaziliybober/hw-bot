

class Class:
	def __init__(self, name, pupils, subjects):
		self._name = name
		self._pupils = pupils
		for pupil in self._pupils:
			pupil.addClass(self)
		self._subjects = subjects

	def __repr__(self):
		return '<Class "' + self.name() + '">'

	def __str__(self):
		return self.__repr__()

	def name(self):
		return self._name

	def pupils(self):
		return self._pupils

	def subjects(self):
		return self._subjects

	def getPupil(self, uid):
		for pupil in self.pupils():
			if type(uid) == int and pupil.uid() == uid or type(uid) == str and pupil.name().lower() == uid.lower():
				return pupil

	def getSubject(self, name):
		for subject in self.subjects():
			if subject.name() == name:
				return subject






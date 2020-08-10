
class Pupil:
	def __init__(self, uid, name=None):
		self._uid = uid
		self._name = name if name else "Unknown pupil"
		self._classes = []
		self._groups = []

	def __repr__(self):
		return '<Pupil "' + self.name() + '">'

	def __str__(self):
		return self.__repr__()

	#def __eq__(self, another):
	#	return self._uid == another._uid


	def uid(self):
		return self._uid

	def name(self):
		return self._name

	def classes(self):
		return self._classes

	def groups(self):
		return self._groups

	def timetable(self):
		return self._timetable

	

	def addClass(self, class_):
		self._classes.append(class_)

	def addGroup(self, group):
		self._groups.append(group)

	def getGroup(self, subject):
		for group in subject.groups():
			if group in self._groups:
				return group

	def setTimetable(self, timetable):
		self._timetable = timetable











if __name__ == '__main__':
	max = Pupil(228322, "Максим Карбышев")
	print(max)
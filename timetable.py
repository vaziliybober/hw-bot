

class Timetable:
	def __init__(self):
		self._timetable = {}
		self._pupils = []

	def setSubjects(self, weekdayNumber, subjects):
		self._timetable[weekdayNumber] = subjects

	def setPupils(self, pupils):
		self._pupils = pupils
		for pupil in pupils:
			pupil.setTimetable(self)

	def subjects(self, weekdayNumber):
		return self._timetable.get(weekdayNumber)

	def copy(self):
		result = Timetable()
		for key, value in self._timetable.items():
			result._timetable[key] = value

		return result

	def __str__(self):
		result = ""
		weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
		for weekdayNumber in range(1, 7):
			result += weekdays[weekdayNumber - 1]
			result += "\n"
			for i, subject in enumerate(self.subjects(weekdayNumber)):
				result += ('---' + str(i + 1) + ". " + subject.name())
				result += "\n"

		return result

	
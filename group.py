from pupil import Pupil

class Group:
	def __init__(self, name, pupils):
		self._name = name
		self._pupils = pupils
		for pupil in self._pupils:
			pupil.addGroup(self)

	def __repr__(self):
		return '<Group object named "' + self.name() + '">'

	def __str__(self):
		return self.__repr__()

	def name(self):
		return self._name

	def pupils(self):
		return self._pupils












if __name__ == '__main__':
	pupils = [Pupil(123, "jenya"), Pupil(321, "vasya")]
	group = Group("some group", pupils)
	print(group)
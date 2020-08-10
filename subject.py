


class Subject:
	def __init__(self, name, pseudonames=None, groups=None):
		self._name = name
		self._pseudonames = pseudonames if pseudonames else []
		self._groups = groups if groups else []
		self.__repr__ = self.__str__


	def name(self):
		return self._name

	def groups(self):
		return self._groups

	def pseudonames(self):
		return self._pseudonames

	def getGroup(self, name):
		for group in self._groups:
			if name == group.name():
				return group








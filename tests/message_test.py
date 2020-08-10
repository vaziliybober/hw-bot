import unittest
import datetime
import mydatetime
from message import Message
from subject import Subject as S

physics = S("Физика")
algebra = S("Алгебра", ["алга"])
geometry = S("Геометрия", ["геомка", "геома"])
literature = S("Литература", ["литра", "лит-ра"])
russian = S("Русский язык", ["русский", "русич", "русск яз", "русск. яз."])
english = S("Английский язык", ["английский", "англ яз", "англ. яз.", "инглиш"])
physCulture = S("Физкультура", ["физра", "физ-ра"])
biology = S("Биология")
history = S("История")
obj = S("Обж")
astronomy = S("Астрономия")
astrophysics = S("Астрофизика")
zftsha = S("ЗФТШ")
informatics = S("Информатика", ["инфа", "программирование"])
chemistry = S("Химия")
geography = S("География")
mathAnalysis = S("Мат. анализ", ["математический анализ", "матан"])
expPhysics = S("Экспериментальная физика", ["эксп. физика", "эксп физика"])

subjects = [physics, algebra, geometry, literature, russian, english, physCulture, biology, history, obj, astronomy, astrophysics, zftsha, informatics,
			chemistry, geography, mathAnalysis, expPhysics]

today = datetime.date(2018, 1, 5)

class TestMessage(unittest.TestCase):
	def test_hw(self):
		mes = Message("зфТш в 26.08.2018", subjects, today, False)
		self.assertEqual(mes.hw(), False)
		mes = Message("дззфТш в 26.08.2018", subjects, today, False)
		self.assertEqual(mes.hw(), False)
		mes = Message("дз  зфТш на 26,08.2018", subjects, today, False)
		self.assertEqual(mes.hw(), True)
		mes = Message("дз ", subjects, today, False)
		self.assertEqual(mes.hw(), True)

	def test_allGroups(self):
		mes = Message("привет, как делА, Все гРуппы", subjects, today, False)
		self.assertEqual(mes.allGroups(), True)
		mes = Message("пппвсе гРуппы", subjects, today, False)
		self.assertEqual(mes.allGroups(), False)
		mes = Message("все гРуппы", subjects, today, False)
		self.assertEqual(mes.allGroups(), False)

	def test_removal(self):
		mes = Message("удалитьпривет, как делА, Все гРуппы", subjects, today, False)
		self.assertEqual(mes.removal(), False)
		mes = Message("удалить привет, как делА, Все гРуппы", subjects, today, False)
		self.assertEqual(mes.removal(), True)
		mes = Message("удалить", subjects, today, False)
		self.assertEqual(mes.removal(), False)

	def test_summary(self):
		mes = Message("конспектпривет, как делА, Все гРуппы", subjects, today, False)
		self.assertEqual(mes.summary(), False)
		mes = Message("конспект привет, как делА, Все гРуппы", subjects, today, False)
		self.assertEqual(mes.summary(), True)
		mes = Message("конспект", subjects, today, False)
		self.assertEqual(mes.summary(), False)

	def test_subject(self):
		mes = Message("привет", subjects, today, False)
		self.assertEqual(mes.subject(), None)
		mes = Message("инглиш", subjects, today, False)
		self.assertEqual(mes.subject().name(), "Английский язык")
		mes = Message("зфтш номер 7 все группы", subjects, today, False)
		self.assertEqual(mes.subject().name(), "ЗФТШ")
		mes = Message("зфтшномер 7", subjects, today, False)
		self.assertEqual(mes.subject(), None)
		mes = Message("удалить зфтш", subjects, today, False)
		self.assertEqual(mes.subject().name(), "ЗФТШ")

	def test_date(self):
		mes = Message("зфТш на 2", subjects, today, False)
		self.assertEqual(mes.date(), mydatetime.closestDateWithDay(today, 2))
		mes = Message("зфТш на 26.08", subjects, today, False)
		self.assertEqual(mes.date(), mydatetime.closestDateWithDayAndMonth(today, 26, 8))
		mes = Message("зфТш на 26.08.2018", subjects, today, False)
		self.assertEqual(mes.date(), datetime.date(2018, 8, 26))
		mes = Message("зфТш в 26.08.2018", subjects, today, False)
		self.assertEqual(mes.date(), None)
		mes = Message("зфТш на 26,08.2018", subjects, today, False)
		self.assertEqual(mes.date(), None)

	def test_content(self):
		mes = Message("зфТш в 26.08.2018", subjects, today, False)
		self.assertEqual(mes.content(), "в 26.08.2018")
		mes = Message("удалить зфТш на 26.08.2018 упр. 89 все группы", subjects, today, False)
		self.assertEqual(mes.content(), "упр. 89")
		mes = Message("зфТшшшш в 26.08.2018", subjects, today, False)
		self.assertEqual(mes.content(), "зфТшшшш в 26.08.2018")
		mes = Message("зфТш на 26.08.2018", subjects, today, False)
		self.assertEqual(mes.content(), '')

	def test_adding(self):
		mes = Message("зфТшшшш в 26.08.2018", subjects, today, False)
		self.assertEqual(mes.adding(), True)
		mes = Message("зфТш на 26.08.2018", subjects, today, False)
		self.assertEqual(mes.adding(), False)
		mes = Message("зфТш от 26.08.2018 все группы", subjects, today, False)
		self.assertEqual(mes.adding(), True)
		mes = Message("удалить зфТш от 26.08.2018 все группы", subjects, today, False)
		self.assertEqual(mes.adding(), False)

	def test_reading(self):
		mes = Message("зфТш", subjects, today, False)
		self.assertEqual(mes.reading(), True)
		mes = Message("дз", subjects, today, False)
		self.assertEqual(mes.reading(), True)
		mes = Message("зфтш на позавчера", subjects, today, False)
		self.assertEqual(mes.reading(), True)
		mes = Message("зфтш на послезавтра фыва все группы", subjects, today, False)
		self.assertEqual(mes.reading(), False)

	def test_errorReport(self):
		mes = Message("зфТшшшш в 26.08.2018", subjects, today, False)
		self.assertEqual(mes.errorReport(), "Отсутствует предмет")
		mes = Message("зфТш на 26,08.2018", subjects, today, False)
		self.assertEqual(mes.errorReport(), "Отсутствует дата")
		mes = Message("дз зфТш на 26.08.2018", subjects, today, False)
		self.assertEqual(mes.errorReport(), "О вы из Англии?")
		mes = Message("зфТш на 26.08.2018", subjects, today, False)
		self.assertEqual(mes.errorReport(), None)
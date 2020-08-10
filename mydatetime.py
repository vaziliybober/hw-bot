import datetime
import calendar


def closestDateWithDay(today, day):
	month = today.month
	year = today.year
	if day < today.day:
		month += 1
	if month > 12:
		month = 1
		year += 1

	return datetime.date(year, month, day)


def closestDateWithDayAndMonth(today, day, month):
	if month == today.month:
		return closestDateWithDay(today, day)

	year = today.year
	if month < today.month:
		year += 1
	
	return datetime.date(year, month, day)


def weekdayNumberToDate(today, weekdayNumber):
	todayWeekdayNumber = today.isoweekday()
	daydelta = (weekdayNumber - todayWeekdayNumber)
	if daydelta <= 0:
		daydelta = 7 + daydelta
	timedelta = datetime.timedelta(days=daydelta)

	return today + timedelta


def dateToWeekdayNumber(date):
	return date.isoweekday()

def strWeekdayToNumber(strWeekday):
	weekdays = ['понедельник', 'вторник', 'среду', 'четверг', 'пятницу', 'субботу', 'воскресенье']
	for i, weekday in enumerate(weekdays):
		if strWeekday.startswith(weekday):
			return i + 1


def strDateToDate(today, string):

	if string == 'сегодня':
		return today

	if string == 'завтра':
		return today + datetime.timedelta(days=1)

	if string == 'послезавтра':
		return today + datetime.timedelta(days=2)

	if string == 'вчера':
		return today + datetime.timedelta(days=-1)

	if string == 'позавчера':
		return today + datetime.timedelta(days=-2)

	weekdayNumber = strWeekdayToNumber(string)
	if weekdayNumber:
		return weekdayNumberToDate(today, weekdayNumber)

	splitString = string.split('.')
	numberOfWords = len(splitString)
	try:
		if numberOfWords == 0:
			return None

		day = int(splitString[0])
		if numberOfWords == 1:
			return closestDateWithDay(today, day)

		month = int(splitString[1])
		if numberOfWords == 2:
			return closestDateWithDayAndMonth(today, day, month)

		year = int(splitString[2])
		if numberOfWords == 3:
			return datetime.date(year, month, day)

		return None

	except ValueError:
		return None


def dateToStr(date):
	day = str(date.day)
	if len(day) == 1:
		day = '0' + day
	month = str(date.month)
	if len(month) == 1:
		month = '0' + month
	year = str(date.year)
	return day + '.' + month + '.' + year


def dateToTodayStr(today, date):
	if date - today == datetime.timedelta(1):
		return "завтра"
	if date - today == datetime.timedelta(2):
		return "послезавтра"
	if date - today == datetime.timedelta(0):
		return "сегодня"
	if date - today == datetime.timedelta(-1):
		return "вчера"
	if date - today == datetime.timedelta(-2):
		return "позавчера"

def dateToWeekday(date):
	weekdays = ['ближайший понедельник', 'ближайший вторник', 'ближайшая среда', 'ближайший четверг', 'ближайшая пятница', 'ближайшая суббота', 'ближайшее воскресенье']
	return weekdays[date.isoweekday() - 1]
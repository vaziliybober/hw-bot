import vk, time
from JSON import Json
from logger import Logger
import datetime
from database import Database
from reference import reference
from record import Record
from message import Message
from mydatetime import dateToStr, dateToTodayStr, dateToWeekday, dateToWeekdayNumber

from kurchat10z_config import class_ as kurchat10z

from kurchat10z_config import vasiliyBobrov

admins = [vasiliyBobrov]
#----------------------------------------------------------------------------


def createMessage(uid, text, attachments=''):
	return {"user_id": uid, "message": text, "attachment": attachments}

def getAnswers(db, class_, json):
	mes = Message(json.text(), class_.subjects(), datetime.date.today(), bool(json.attachments()))
	pupil = class_.getPupil(json.uid())
	date = mes.date()
	subject = mes.subject()
	

	fastMes = lambda text: [createMessage(json.uid(), text)]

	if json.text().strip().lower() == 'справка':
		return fastMes(reference)

	if json.text().strip().lower() == 'расписание':
		return fastMes(pupil.timetable().__str__())

	if mes.errorReport():
		return fastMes('Ошибка! ' + mes.errorReport() + '\nЧтобы ознакомиться с ботом, напишите "справка".')

	group = pupil.getGroup(subject) if subject else None
	hw = mes.hw()

	if mes.adding():
		record = Record(date, subject, group, pupil, mes.content(), json.attachments())
		db.add(record)
		adding = ""
		if not subject in pupil.timetable().subjects(dateToWeekdayNumber(date)):
			adding = ". Учтите, что вы записали дз не по расписанию!"
		return fastMes("Запись добавлена" + adding)

	elif mes.removal():
		if pupil in admins:
			probablePupil = class_.getPupil(mes.content())
			if probablePupil:
				pupil = probablePupil
				group = pupil.getGroup(subject)
		if db.remove(date, subject, group, pupil):
			return fastMes("Запись удалена")
		else:
			return fastMes("Запись не найдена")

	elif mes.reading():
		messages = []

		dates = [date] if date else [date for date in db.dates(subject) if date >= datetime.date.today()]

		bigMessage = ""
		currentMessage = ""
		for date in dates:
			if not mes.date():
				adding = dateToTodayStr(datetime.date.today(), date)
				if not adding:
					if date <= datetime.date.today() + datetime.timedelta(days=7):
						adding = '(' + dateToWeekday(date) + ')'
					else:
						adding = ""
				else:
					adding = '(' + adding + ')'
				currentMessage += ('На ' + dateToStr(date) + ' ' + adding + '\n')
			subjects = [mes.subject()] if mes.subject() else db.subjects(date)
			for subject in subjects:
				if not mes.subject():
					currentMessage += ('---' + subject.name() + '\n')
				groups = db.groups(date, subject)
				for group in groups:
					if group.name() != 'Весь класс':
						currentMessage += ('------' + group.name() + '\n')
					records = db.read(date, subject, group)

					if records:
						bigMessage += currentMessage
					currentMessage = ""
					for record in records:
						bigMessage += ('---------' + record.pupil().name() + '\n')
						if record.attachments():
							bigMessage += (record.text())
							messages.append(createMessage(json.uid(), bigMessage, record.attachments()))
							bigMessage = ""
							currentMessage = ""
						else:
							bigMessage += (record.text() + '\n\n')


		if bigMessage:
			messages += fastMes(bigMessage)

		if not messages:
			messages += fastMes("Нет записей")

		return messages

			


#----------------------------------------------------------------------------
logger = Logger('log.txt')


classes = [kurchat10z]

access_token='20ef9f6cf3ae19b3e46894a175955dffc485609ea227e7ddabfbf7c8439a9f11e1c3a63ca42a3c9f754a1' # Бот Василий


def getTsPts(api):
	try:
		args = api.messages.getLongPollServer(need_pts = True, v=5.71)
	except:
		logger.log(datetime.datetime.now().__str__()[:-7] + ": vk error in api.messages.getLongPollHistory")
	else:
		return (args['ts'], args['pts'])

def restartSession():
	global session, api, ts, pts
	while True:
		try:
			session = vk.Session(access_token = access_token)
			api = vk.API(session, v=5.71)
			ts, pts = getTsPts(api)
		except:
			continue
		else:
			break
		

restartSession()


while True:
	time.sleep(1)
	
	try:
		event = api.messages.getLongPollHistory(pts = pts, ts = ts, v=5.71)
	except:
		logger.log(datetime.datetime.now().__str__()[:-7] + ": vk error in getLongPollHistory")
		restartSession()
		continue
	
	if event['messages']['count'] == 0:
		continue

	json = Json(event['messages']['items'][0])
	
	
	
	

	if json.isConversation():
		continue
	pupilClasses = [_ for _ in classes if _.getPupil(json.uid())]

	for class_ in pupilClasses:
		mes = Message(json.text(), class_.subjects(), datetime.date.today(), bool(json.attachments()))
		gdzAdding = '_gdz' if mes.gdz() else ''
		db = Database('data/' + class_.name() + gdzAdding + '.pickle', class_)
		answers = getAnswers(db, class_, json)
		for answer in answers:
			if answer:
				try:
					api.messages.send(**answer, v=5.71)
				except vk.exceptions.VkAPIError:
					logger.log(datetime.datetime.now().__str__()[:-7] + ": vk error in api.messages.send")
					time.sleep(1)
				else:
					time.sleep(1)

	ts, pts = getTsPts(api)






class Json:
	def __init__(self, json):
		self._json = json
		self._text = self.text()
		self._attachments = self.attachments()
		self._uid = self.uid()
		self._date = self.date()
		self._isConversation = self.isConversation()
		self._messageId = self.messageId()


	def messageId(self):
		try:
			self._id
		except AttributeError:
			return self._json['id']
		else:
			return self._id


	def isConversation(self):
		try:
			self._isChat
		except AttributeError:
			try:
				self._json['chat_id']
			except KeyError:
				return False
			else:
				return True
		else:
			return self._isChat


	def text(self):
		try:
			self._text
		except AttributeError:
			return self._json['body']
		else:
			return self._text


	def attachments(self):
		try:
			self._attachments
		except AttributeError:
			attachments = self._json.get('attachments', [])

			acc = []
			for attachment in attachments:
				type_ = attachment['type']
				data = attachment[type_]
				try:
					owner_id = data['owner_id']
				except KeyError:
					continue
				media_id = data['id']
				try:
					access_key = data['access_key']
				except KeyError:
					continue
				acc.append(type_ + str(owner_id) + '_' + str(media_id) + '_' + access_key)

			return ','.join(acc)
		else:
			return self._attachments


	def uid(self):
		try:
			self._uid
		except AttributeError:
			return self._json['user_id']
		else:
			return self._uid

	def date(self):
		try:
			self._date
		except AttributeError:
			return self._json['date']
		else:
			return self._date

import unittest
from JSON import Json


class TestJSON(unittest.TestCase):

	def test_text(self):
		json = Json({'body': 'asdf', 'read_state': 0, 'out': 0, 'date': 1506610548, 'mid': 14976, 'uid': 181458569, 'title': ''})
		self.assertEqual(json.text(), 'asdf')
		json = Json({'attachments': [{'type': 'photo', 'photo': {'src_xxbig': 'https://pp.userapi.com/c637326/v637326569/4e53d/bU8MoUBK820.jpg', 'src_big': 'https://pp.userapi.com/c637326/v637326569/4e53b/Sa7NLZKH4x4.jpg', 'src_xbig': 'https://pp.userapi.com/c637326/v637326569/4e53c/8yvMes7qETk.jpg', 'created': 1488139249, 'access_key': 'cf7d76099ca912aeb5', 'height': 2160, 'src_small': 'https://pp.userapi.com/c637326/v637326569/4e539/tHwVW7Hcd2c.jpg', 'owner_id': 181458569, 'src_xxxbig': 'https://pp.userapi.com/c637326/v637326569/4e53e/eu_HoIwNMgc.jpg', 'text': '', 'aid': 182423804, 'src': 'https://pp.userapi.com/c637326/v637326569/4e53a/Pm0ovbpa35g.jpg', 'width': 1620, 'pid': 456239106}}], 'title': '', 'body': '', 'read_state': 0, 'attachment': {'type': 'photo', 'photo': {'src_xxbig': 'https://pp.userapi.com/c637326/v637326569/4e53d/bU8MoUBK820.jpg', 'src_big': 'https://pp.userapi.com/c637326/v637326569/4e53b/Sa7NLZKH4x4.jpg', 'src_xbig': 'https://pp.userapi.com/c637326/v637326569/4e53c/8yvMes7qETk.jpg', 'created': 1488139249, 'access_key': 'cf7d76099ca912aeb5', 'height': 2160, 'src_small': 'https://pp.userapi.com/c637326/v637326569/4e539/tHwVW7Hcd2c.jpg', 'owner_id': 181458569, 'src_xxxbig': 'https://pp.userapi.com/c637326/v637326569/4e53e/eu_HoIwNMgc.jpg', 'text': '', 'aid': 182423804, 'src': 'https://pp.userapi.com/c637326/v637326569/4e53a/Pm0ovbpa35g.jpg', 'width': 1620, 'pid': 456239106}}, 'date': 1506611469, 'mid': 14977, 'uid': 181458569, 'out': 0})
		self.assertEqual(json.text(), '')
		json = Json({'body': '', 'date': 1506611603, 'attachment': {'type': 'photo', 'photo': {'width': 720, 'src_xbig': 'https://pp.userapi.com/c637326/v637326569/4e564/rTn2HXj6eiQ.jpg', 'aid': 182423804, 'text': '', 'src_small': 'https://pp.userapi.com/c637326/v637326569/4e561/ptc6V-KTaB0.jpg', 'src': 'https://pp.userapi.com/c637326/v637326569/4e562/kYlGaM7N2bo.jpg', 'src_xxxbig': 'https://pp.userapi.com/c637326/v637326569/4e566/uwqbyl16s6E.jpg', 'access_key': '1db48a3f693fef5f07', 'created': 1488139350, 'pid': 456239110, 'height': 1280, 'owner_id': 181458569, 'src_xxbig': 'https://pp.userapi.com/c637326/v637326569/4e565/N7J9Zn8VoIk.jpg', 'src_big': 'https://pp.userapi.com/c637326/v637326569/4e563/BjxNRZs-1Lo.jpg'}}, 'out': 0, 'title': '', 'read_state': 0, 'mid': 14979, 'uid': 181458569, 'attachments': [{'type': 'photo', 'photo': {'width': 720, 'src_xbig': 'https://pp.userapi.com/c637326/v637326569/4e564/rTn2HXj6eiQ.jpg', 'aid': 182423804, 'text': '', 'src_small': 'https://pp.userapi.com/c637326/v637326569/4e561/ptc6V-KTaB0.jpg', 'src': 'https://pp.userapi.com/c637326/v637326569/4e562/kYlGaM7N2bo.jpg', 'src_xxxbig': 'https://pp.userapi.com/c637326/v637326569/4e566/uwqbyl16s6E.jpg', 'access_key': '1db48a3f693fef5f07', 'created': 1488139350, 'pid': 456239110, 'height': 1280, 'owner_id': 181458569, 'src_xxbig': 'https://pp.userapi.com/c637326/v637326569/4e565/N7J9Zn8VoIk.jpg', 'src_big': 'https://pp.userapi.com/c637326/v637326569/4e563/BjxNRZs-1Lo.jpg'}}, {'type': 'audio', 'audio': {'performer': 'Enya - Only Time', 'title': 'Enya - Only Time', 'content_restricted': 1, 'genre': 18, 'duration': 213, 'owner_id': 181458569, 'aid': 456239068, 'artist': 'Enya - Only Time'}}, {'type': 'doc', 'doc': {'date': 1495732503, 'ext': 'ogg', 'access_key': 'a8f94f0d7435630990', 'title': 'bzz.ogg', 'size': 11763, 'owner_id': 181458569, 'did': 446096624, 'url': 'https://vk.com/doc181458569_446096624?hash=7b1b37b8adeac868c8&dl=GQYTGOBXGQ2DQOI:1506611604:9fa9627dc916af4c95&api=1&no_preview=1'}}]})
		self.assertEqual(json.text(), '')


	def test_attachments(self):
		json = Json({'mid': 15001, 'body': '', 'date': 1506615601, 'title': '', 'uid': 181458569, 'attachments': [{'photo': {'pid': 456239106, 'src_small': 'https://pp.userapi.com/c637326/v637326569/4e539/tHwVW7Hcd2c.jpg', 'src_xxbig': 'https://pp.userapi.com/c637326/v637326569/4e53d/bU8MoUBK820.jpg', 'height': 2160, 'aid': 182423804, 'created': 1488139249, 'access_key': 'cf7d76099ca912aeb5', 'width': 1620, 'owner_id': 181458569, 'src_big': 'https://pp.userapi.com/c637326/v637326569/4e53b/Sa7NLZKH4x4.jpg', 'src_xxxbig': 'https://pp.userapi.com/c637326/v637326569/4e53e/eu_HoIwNMgc.jpg', 'src': 'https://pp.userapi.com/c637326/v637326569/4e53a/Pm0ovbpa35g.jpg', 'text': '', 'src_xbig': 'https://pp.userapi.com/c637326/v637326569/4e53c/8yvMes7qETk.jpg'}, 'type': 'photo'}], 'attachment': {'photo': {'pid': 456239106, 'src_small': 'https://pp.userapi.com/c637326/v637326569/4e539/tHwVW7Hcd2c.jpg', 'src_xxbig': 'https://pp.userapi.com/c637326/v637326569/4e53d/bU8MoUBK820.jpg', 'height': 2160, 'aid': 182423804, 'created': 1488139249, 'access_key': 'cf7d76099ca912aeb5', 'width': 1620, 'owner_id': 181458569, 'src_big': 'https://pp.userapi.com/c637326/v637326569/4e53b/Sa7NLZKH4x4.jpg', 'src_xxxbig': 'https://pp.userapi.com/c637326/v637326569/4e53e/eu_HoIwNMgc.jpg', 'src': 'https://pp.userapi.com/c637326/v637326569/4e53a/Pm0ovbpa35g.jpg', 'text': '', 'src_xbig': 'https://pp.userapi.com/c637326/v637326569/4e53c/8yvMes7qETk.jpg'}, 'type': 'photo'}, 'out': 0, 'read_state': 0})
		self.assertEqual(json.attachments(), 'photo181458569_456239106_cf7d76099ca912aeb5')
		json = Json({'mid': 15002, 'body': '', 'date': 1506615727, 'title': '', 'uid': 181458569, 'attachments': [{'doc': {'date': 1495208695, 'access_key': 'cf27b6b7efd213f71a', 'size': 327, 'ext': 'py', 'title': 'platform.py', 'owner_id': 181458569, 'url': 'https://vk.com/doc181458569_445848744?hash=b13fed0aae4172b820&dl=GQYTGOBXGQ2DQOI:1506615727:e23c53473968a6122f&api=1&no_preview=1', 'did': 445848744}, 'type': 'doc'}, {'photo': {'pid': 456239110, 'src_small': 'https://pp.userapi.com/c637326/v637326569/4e561/ptc6V-KTaB0.jpg', 'src_xxbig': 'https://pp.userapi.com/c637326/v637326569/4e565/N7J9Zn8VoIk.jpg', 'height': 1280, 'aid': 182423804, 'created': 1488139350, 'access_key': '1db48a3f693fef5f07', 'width': 720, 'owner_id': 181458569, 'src_big': 'https://pp.userapi.com/c637326/v637326569/4e563/BjxNRZs-1Lo.jpg', 'src_xxxbig': 'https://pp.userapi.com/c637326/v637326569/4e566/uwqbyl16s6E.jpg', 'src': 'https://pp.userapi.com/c637326/v637326569/4e562/kYlGaM7N2bo.jpg', 'text': '', 'src_xbig': 'https://pp.userapi.com/c637326/v637326569/4e564/rTn2HXj6eiQ.jpg'}, 'type': 'photo'}], 'attachment': {'doc': {'date': 1495208695, 'access_key': 'cf27b6b7efd213f71a', 'size': 327, 'ext': 'py', 'title': 'platform.py', 'owner_id': 181458569, 'url': 'https://vk.com/doc181458569_445848744?hash=b13fed0aae4172b820&dl=GQYTGOBXGQ2DQOI:1506615727:e23c53473968a6122f&api=1&no_preview=1', 'did': 445848744}, 'type': 'doc'}, 'out': 0, 'read_state': 0})
		self.assertEqual(json.attachments(), 'doc181458569_445848744_cf27b6b7efd213f71a,photo181458569_456239110_1db48a3f693fef5f07')
		json = Json({'mid': 15006, 'read_state': 0, 'title': '', 'body': 'asdf', 'date': 1506617684, 'out': 0, 'uid': 181458569})
		self.assertEqual(json.attachments(), '')

	def test_uid(self):
		json = Json({'mid': 15001, 'body': '', 'date': 1506615601, 'title': '', 'uid': 181458569, 'attachments': [{'photo': {'pid': 456239106, 'src_small': 'https://pp.userapi.com/c637326/v637326569/4e539/tHwVW7Hcd2c.jpg', 'src_xxbig': 'https://pp.userapi.com/c637326/v637326569/4e53d/bU8MoUBK820.jpg', 'height': 2160, 'aid': 182423804, 'created': 1488139249, 'access_key': 'cf7d76099ca912aeb5', 'width': 1620, 'owner_id': 181458569, 'src_big': 'https://pp.userapi.com/c637326/v637326569/4e53b/Sa7NLZKH4x4.jpg', 'src_xxxbig': 'https://pp.userapi.com/c637326/v637326569/4e53e/eu_HoIwNMgc.jpg', 'src': 'https://pp.userapi.com/c637326/v637326569/4e53a/Pm0ovbpa35g.jpg', 'text': '', 'src_xbig': 'https://pp.userapi.com/c637326/v637326569/4e53c/8yvMes7qETk.jpg'}, 'type': 'photo'}], 'attachment': {'photo': {'pid': 456239106, 'src_small': 'https://pp.userapi.com/c637326/v637326569/4e539/tHwVW7Hcd2c.jpg', 'src_xxbig': 'https://pp.userapi.com/c637326/v637326569/4e53d/bU8MoUBK820.jpg', 'height': 2160, 'aid': 182423804, 'created': 1488139249, 'access_key': 'cf7d76099ca912aeb5', 'width': 1620, 'owner_id': 181458569, 'src_big': 'https://pp.userapi.com/c637326/v637326569/4e53b/Sa7NLZKH4x4.jpg', 'src_xxxbig': 'https://pp.userapi.com/c637326/v637326569/4e53e/eu_HoIwNMgc.jpg', 'src': 'https://pp.userapi.com/c637326/v637326569/4e53a/Pm0ovbpa35g.jpg', 'text': '', 'src_xbig': 'https://pp.userapi.com/c637326/v637326569/4e53c/8yvMes7qETk.jpg'}, 'type': 'photo'}, 'out': 0, 'read_state': 0})
		self.assertEqual(json.uid(), 181458569)
		json = Json({'mid': 15002, 'body': '', 'date': 1506615727, 'title': '', 'uid': 81458569, 'attachments': [{'doc': {'date': 1495208695, 'access_key': 'cf27b6b7efd213f71a', 'size': 327, 'ext': 'py', 'title': 'platform.py', 'owner_id': 181458569, 'url': 'https://vk.com/doc181458569_445848744?hash=b13fed0aae4172b820&dl=GQYTGOBXGQ2DQOI:1506615727:e23c53473968a6122f&api=1&no_preview=1', 'did': 445848744}, 'type': 'doc'}, {'photo': {'pid': 456239110, 'src_small': 'https://pp.userapi.com/c637326/v637326569/4e561/ptc6V-KTaB0.jpg', 'src_xxbig': 'https://pp.userapi.com/c637326/v637326569/4e565/N7J9Zn8VoIk.jpg', 'height': 1280, 'aid': 182423804, 'created': 1488139350, 'access_key': '1db48a3f693fef5f07', 'width': 720, 'owner_id': 181458569, 'src_big': 'https://pp.userapi.com/c637326/v637326569/4e563/BjxNRZs-1Lo.jpg', 'src_xxxbig': 'https://pp.userapi.com/c637326/v637326569/4e566/uwqbyl16s6E.jpg', 'src': 'https://pp.userapi.com/c637326/v637326569/4e562/kYlGaM7N2bo.jpg', 'text': '', 'src_xbig': 'https://pp.userapi.com/c637326/v637326569/4e564/rTn2HXj6eiQ.jpg'}, 'type': 'photo'}], 'attachment': {'doc': {'date': 1495208695, 'access_key': 'cf27b6b7efd213f71a', 'size': 327, 'ext': 'py', 'title': 'platform.py', 'owner_id': 181458569, 'url': 'https://vk.com/doc181458569_445848744?hash=b13fed0aae4172b820&dl=GQYTGOBXGQ2DQOI:1506615727:e23c53473968a6122f&api=1&no_preview=1', 'did': 445848744}, 'type': 'doc'}, 'out': 0, 'read_state': 0})
		self.assertEqual(json.uid(), 81458569)

	def test_date(self):
		json = Json({'mid': 15002, 'body': '', 'date': 1506615727, 'title': '', 'uid': 81458569, 'attachments': [{'doc': {'date': 1495208695, 'access_key': 'cf27b6b7efd213f71a', 'size': 327, 'ext': 'py', 'title': 'platform.py', 'owner_id': 181458569, 'url': 'https://vk.com/doc181458569_445848744?hash=b13fed0aae4172b820&dl=GQYTGOBXGQ2DQOI:1506615727:e23c53473968a6122f&api=1&no_preview=1', 'did': 445848744}, 'type': 'doc'}, {'photo': {'pid': 456239110, 'src_small': 'https://pp.userapi.com/c637326/v637326569/4e561/ptc6V-KTaB0.jpg', 'src_xxbig': 'https://pp.userapi.com/c637326/v637326569/4e565/N7J9Zn8VoIk.jpg', 'height': 1280, 'aid': 182423804, 'created': 1488139350, 'access_key': '1db48a3f693fef5f07', 'width': 720, 'owner_id': 181458569, 'src_big': 'https://pp.userapi.com/c637326/v637326569/4e563/BjxNRZs-1Lo.jpg', 'src_xxxbig': 'https://pp.userapi.com/c637326/v637326569/4e566/uwqbyl16s6E.jpg', 'src': 'https://pp.userapi.com/c637326/v637326569/4e562/kYlGaM7N2bo.jpg', 'text': '', 'src_xbig': 'https://pp.userapi.com/c637326/v637326569/4e564/rTn2HXj6eiQ.jpg'}, 'type': 'photo'}], 'attachment': {'doc': {'date': 1495208695, 'access_key': 'cf27b6b7efd213f71a', 'size': 327, 'ext': 'py', 'title': 'platform.py', 'owner_id': 181458569, 'url': 'https://vk.com/doc181458569_445848744?hash=b13fed0aae4172b820&dl=GQYTGOBXGQ2DQOI:1506615727:e23c53473968a6122f&api=1&no_preview=1', 'did': 445848744}, 'type': 'doc'}, 'out': 0, 'read_state': 0})
		self.assertEqual(json.date(), 1506615727)
		json = Json({'mid': 15006, 'read_state': 0, 'title': '', 'body': 'asdf', 'date': 1506617685, 'out': 0, 'uid': 458569})
		self.assertEqual(json.date(), 1506617685)
		json = Json({'mid': 15001, 'body': '', 'date': 1506615601, 'title': '', 'uid': 158569, 'attachments': [{'photo': {'pid': 456239106, 'src_small': 'https://pp.userapi.com/c637326/v637326569/4e539/tHwVW7Hcd2c.jpg', 'src_xxbig': 'https://pp.userapi.com/c637326/v637326569/4e53d/bU8MoUBK820.jpg', 'height': 2160, 'aid': 182423804, 'created': 1488139249, 'access_key': 'cf7d76099ca912aeb5', 'width': 1620, 'owner_id': 181458569, 'src_big': 'https://pp.userapi.com/c637326/v637326569/4e53b/Sa7NLZKH4x4.jpg', 'src_xxxbig': 'https://pp.userapi.com/c637326/v637326569/4e53e/eu_HoIwNMgc.jpg', 'src': 'https://pp.userapi.com/c637326/v637326569/4e53a/Pm0ovbpa35g.jpg', 'text': '', 'src_xbig': 'https://pp.userapi.com/c637326/v637326569/4e53c/8yvMes7qETk.jpg'}, 'type': 'photo'}], 'attachment': {'photo': {'pid': 456239106, 'src_small': 'https://pp.userapi.com/c637326/v637326569/4e539/tHwVW7Hcd2c.jpg', 'src_xxbig': 'https://pp.userapi.com/c637326/v637326569/4e53d/bU8MoUBK820.jpg', 'height': 2160, 'aid': 182423804, 'created': 1488139249, 'access_key': 'cf7d76099ca912aeb5', 'width': 1620, 'owner_id': 181458569, 'src_big': 'https://pp.userapi.com/c637326/v637326569/4e53b/Sa7NLZKH4x4.jpg', 'src_xxxbig': 'https://pp.userapi.com/c637326/v637326569/4e53e/eu_HoIwNMgc.jpg', 'src': 'https://pp.userapi.com/c637326/v637326569/4e53a/Pm0ovbpa35g.jpg', 'text': '', 'src_xbig': 'https://pp.userapi.com/c637326/v637326569/4e53c/8yvMes7qETk.jpg'}, 'type': 'photo'}, 'out': 0, 'read_state': 0})
		self.assertEqual(json.date(), 1506615601)

	def test_messageId(self):
		json = Json({'body': 'sdf',
					 'date': 1515322215,
					 'mid': 19687,
					 'out': 0,
					 'read_state': 0,
					 'title': '',
					 'uid': 181458569})
		self.assertEqual(json.messageId(), 19687)

	def test_isConversation(self):
		json = Json({'body': 'sdf',
					 'date': 1515322329,
					 'mid': 19689,
					 'out': 0,
					 'read_state': 0,
					 'title': '',
					 'uid': 181458569})
		self.assertEqual(json.isConversation(), False)

		json = Json({'admin_id': 181458569,
					 'body': 'для бота',
					 'chat_active': '181458569,208058020,186951375,146389567',
					 'chat_id': 16,
					 'date': 1515322368,
					 'mid': 19691,
					 'out': 0,
					 'photo_100': 'https://pp.userapi.com/c830109/v830109075/ab85/pBwVQESCXE8.jpg',
					 'photo_200': 'https://pp.userapi.com/c830109/v830109075/ab83/aOpwT4njKqY.jpg',
					 'photo_50': 'https://pp.userapi.com/c830109/v830109075/ab86/U80tn6ZcxJI.jpg',
					 'read_state': 0,
					 'title': 'Партизаны',
					 'uid': 181458569,
					 'users_count': 10})
		self.assertEqual(json.isConversation(), True)

		
















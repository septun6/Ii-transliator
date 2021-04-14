import json

class Database:
	def __init__(self, name):
		self.name = name
		print("Working with database \"%s\"" % name)

	def read_database(self):
		with open(self.name, "r", encoding="utf-8") as file:
			data = json.load(file)
		return data

	def change_database(self, data):
		with open(self.name, "w", encoding="utf-8") as file:
			json.dump(data, file, ensure_ascii=False)
		return

	def add_user(self, telegram_id, writing_system):
		telegram_id = str(telegram_id)
		data = self.read_database()
		data[telegram_id] = {"writing_system" : writing_system, "state" : "", "ws_from" : "", "ws_to": ""}
		self.change_database(data)
		return

	def remove_user(self, telegram_id):
		telegram_id = str(telegram_id)
		data = self.read_database()
		del data[telegram_id]
		self.change_database(data)
		return

	def get_user_writing_system(self, telegram_id):
		if self.user_is_registered(telegram_id):
			telegram_id = str(telegram_id)
			user_info = self.read_database()[telegram_id]
			return user_info["writing_system"]
		else:
			return false


	def user_is_registered(self, telegram_id):
		telegram_id = str(telegram_id)
		data = self.read_database()
		if telegram_id in data.keys():
			answer = True
		else:
			answer = False
		return answer

	def get_user_state(self, telegram_id):
		if self.user_is_registered(telegram_id):
			telegram_id = str(telegram_id)
			user_info = self.read_database()[telegram_id]
			return user_info["state"]
		return false

	def update_user_state(self, telegram_id, state):
		telegram_id = str(telegram_id)
		data = self.read_database()
		data[telegram_id]["state"] = state

		self.change_database(data)
		return

	def update_user_writing_system(self, telegram_id, writing_system):
		telegram_id = str(telegram_id)
		data = self.read_database()
		data[telegram_id]["writing_system"] = writing_system

		self.change_database(data)
		return

	def update_user_data(self, telegram_id, **update_data):
		telegram_id = str(telegram_id)
		data = self.read_database()

		for key in update_data.keys():
			data[telegram_id][key] = update_data[key]
		
		self.change_database(data)
		return

	def get_user_data(self, telegram_id, *req_data):
		telegram_id = str(telegram_id)
		answer = {}
		data = self.read_database()

		for key in req_data:
			answer[key] = data[telegram_id][key]

		return answer
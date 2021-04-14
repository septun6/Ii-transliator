import config
import telebot
import work_dict
import worker
from dbworker import Database

bot = telebot.TeleBot(config.token)
dbworker = Database(config.database_name)

@bot.message_handler(commands=['start'])
def start(message):
	user_id = message.from_user.id

	if not dbworker.user_is_registered(user_id):
		message_to_user = "Вітаю! Я бот-транслятор і можу перекладати тексти української мови з однієї системи письма в іншу.\nДля початку роботи треба обрати систему письма, яку буде використовувати бот для спілкування"
		bot.send_message(user_id, message_to_user)

		message_to_user = "Оберіть систему письма бота:"
		user_markup = telebot.types.ReplyKeyboardMarkup(True, False)

		for writing_system in work_dict.list_of_writing_systems:
			user_markup.row(writing_system)

		dbworker.add_user(user_id, "ky")
		dbworker.update_user_state(user_id, "SetSystem")

	else:
		user_writing_system = dbworker.get_user_writing_system(user_id)
		message_to_user = work_dict.dict_for_work[user_writing_system]["welcome_back"]
		bot.send_message(user_id, message_to_user)

		message_to_user = work_dict.dict_for_work[user_writing_system]["select_menu_item"]
		user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
		for buttom in work_dict.dict_for_work[user_writing_system]["list_of_buttoms"]:
			user_markup.row(buttom)

		dbworker.update_user_state(user_id, "Main")

	bot.send_message(user_id, message_to_user, reply_markup=user_markup)


@bot.message_handler(commands=['stop'])
def stop(message):
	user_id = message.from_user.id
	dbworker.remove_user(user_id)
	bot.send_message(user_id, "Ваші дані видалені!")

@bot.message_handler(func=lambda message: dbworker.get_user_state(message.from_user.id) == "SetSystem", content_types=['text'])
def set_writing_system(message):
	user_id = message.from_user.id

	if message.text in work_dict.get_work_list("change_writing_system"):
		user_writing_system = dbworker.get_user_writing_system(user_id)
		message_to_user = work_dict.dict_for_work[user_writing_system]["choose_a_bot_writing_system"]

		user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
		for writing_system in work_dict.list_of_writing_systems:
			user_markup.row(writing_system)
		

		bot.send_message(user_id, message_to_user, reply_markup=user_markup)

	elif message.text in work_dict.list_of_writing_systems:
		user_writing_system = work_dict.dict_of_code_writing_systems[message.text]
		dbworker.update_user_writing_system(user_id, user_writing_system)

		message_to_user = work_dict.dict_for_work[user_writing_system]["bot's_writing_system_has_changed"]
		bot.send_message(user_id, message_to_user)

		message_to_user = work_dict.dict_for_work[user_writing_system]["select_menu_item"]
		user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
		for buttom in work_dict.dict_for_work[user_writing_system]["list_of_buttoms"]:
			user_markup.row(buttom)

		bot.send_message(user_id, message_to_user, reply_markup=user_markup)
		dbworker.update_user_state(user_id, "Main")

	else:
		user_writing_system = dbworker.get_user_writing_system(user_id)
		message_to_user = work_dict.dict_for_work[user_writing_system]["Error"]
		bot.send_message(user_id, message_to_user)


@bot.message_handler(func=lambda message: dbworker.get_user_state(message.from_user.id) == "Main", content_types=['text'])
def main_working(message):
	user_id = message.from_user.id
	user_writing_system = dbworker.get_user_writing_system(user_id)

	if message.text in work_dict.get_work_list("change_writing_system"):
		message_to_user = work_dict.dict_for_work[user_writing_system]["choose_a_bot_writing_system"]

		user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
		for writing_system in work_dict.list_of_writing_systems:
			user_markup.row(writing_system)
		

		bot.send_message(user_id, message_to_user, reply_markup=user_markup)
		dbworker.update_user_state(user_id, "SetSystem")

	elif message.text in work_dict.get_work_list("translate"):
		message_to_user = work_dict.dict_for_work[user_writing_system]['writing_system_text_to']
		user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
		for buttom in work_dict.dict_for_work[user_writing_system]['writing_systems_to']:
			user_markup.row(buttom)
		bot.send_message(user_id, message_to_user, reply_markup=user_markup)
		dbworker.update_user_state(user_id, "TranslateTo")

	else:
		message_to_user = work_dict.dict_for_work[user_writing_system]["Error"]
		bot.send_message(user_id, message_to_user, reply_markup=None)


@bot.message_handler(func=lambda message: dbworker.get_user_state(message.from_user.id) == "TranslateTo", content_types=['text'])
def set_system_to(message):
	user_id = message.from_user.id
	user_writing_system = dbworker.get_user_writing_system(user_id)

	if message.text in work_dict.dict_for_work[user_writing_system]['writing_systems_to']:
		if message.text == work_dict.dict_for_work[user_writing_system]['back_to_menu']:
			message_to_user = work_dict.dict_for_work[user_writing_system]["select_menu_item"]
			user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
			for buttom in work_dict.dict_for_work[user_writing_system]["list_of_buttoms"]:
				user_markup.row(buttom)
			dbworker.update_user_state(user_id, "Main")
		
		else:
			message_to_user = work_dict.dict_for_work[user_writing_system]["writing_system_text_from"]
			user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
			for buttom in work_dict.dict_for_work[user_writing_system]["writing_systems_from"]:
				user_markup.row(buttom)
			dbworker.update_user_data(user_id, state="TranslateFrom", ws_to=work_dict.dict_of_code_writing_systems[message.text])

	else:
		message_to_user = work_dict.dict_for_work[user_writing_system]["Error"]
		user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
		for writing_system in work_dict.list_of_writing_systems:
			user_markup.row(writing_system)
	
	bot.send_message(user_id, message_to_user, reply_markup=user_markup)


@bot.message_handler(func=lambda message: dbworker.get_user_state(message.from_user.id) == "TranslateFrom", content_types=['text'])
def set_system_from(message):
	user_id = message.from_user.id
	user_writing_system = dbworker.get_user_writing_system(user_id)

	if message.text in work_dict.dict_for_work[user_writing_system]["writing_systems_from"]:
		if message.text == work_dict.dict_for_work[user_writing_system]["back_to_menu"]:
			message_to_user = work_dict.dict_for_work[user_writing_system]["select_menu_item"]
			user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
			for buttom in work_dict.dict_for_work[user_writing_system]["list_of_buttoms"]:
				user_markup.row(buttom)
			dbworker.update_user_data(user_id, state="Main", ws_to="")
		
		elif message.text == work_dict.dict_for_work[user_writing_system]['back']:
			message_to_user = work_dict.dict_for_work[user_writing_system]['writing_system_text_to']
			user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
			for buttom in work_dict.dict_for_work[user_writing_system]['writing_systems_to']:
				user_markup.row(buttom)
			dbworker.update_user_data(user_id, state="TranslateTo", ws_to="")

		else:
			message_to_user = work_dict.dict_for_work[user_writing_system]['enter_text']
			user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
			for buttom in work_dict.dict_for_work[user_writing_system]['text_buttoms']:
				user_markup.row(buttom)
			dbworker.update_user_data(user_id, state="Translate", ws_from=work_dict.dict_of_code_writing_systems[message.text])

		bot.send_message(user_id, message_to_user, reply_markup=user_markup)

	else:
		message_to_user = work_dict.dict_for_work[user_writing_system]["Error"]
		bot.send_message(user_id, message_to_user)


@bot.message_handler(func=lambda message: dbworker.get_user_state(message.from_user.id) == "Translate", content_types=['text'])
def set_system_from(message):
	user_id = message.from_user.id
	user_writing_system = dbworker.get_user_writing_system(user_id)

	if message.text in work_dict.dict_for_work[user_writing_system]["text_buttoms"]:
		if message.text == work_dict.dict_for_work[user_writing_system]["back_to_menu"]:
			message_to_user = work_dict.dict_for_work[user_writing_system]["select_menu_item"]
			user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
			for buttom in work_dict.dict_for_work[user_writing_system]["list_of_buttoms"]:
				user_markup.row(buttom)
			dbworker.update_user_data(user_id, state="Main", ws_to="", ws_from="")
		
		else:
			message_to_user = work_dict.dict_for_work[user_writing_system]['writing_system_text_from']
			user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
			for buttom in work_dict.dict_for_work[user_writing_system]['writing_systems_from']:
				user_markup.row(buttom)
			dbworker.update_user_data(user_id, state="TranslateFrom", ws_from="")

		bot.send_message(user_id, message_to_user, reply_markup=user_markup)

	else:
		user_data = dbworker.get_user_data(user_id, 'ws_from', 'ws_to')
		text = worker.translate(user_data['ws_from'], user_data['ws_to'], message.text)
		bot.send_message(user_id, text)

		message_to_user = work_dict.dict_for_work[user_writing_system]["select_menu_item"]
		user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
		for buttom in work_dict.dict_for_work[user_writing_system]["list_of_buttoms"]:
			user_markup.row(buttom)
		dbworker.update_user_data(user_id, state="Main", ws_to="", ws_from="")
		bot.send_message(user_id, message_to_user, reply_markup=user_markup)


if __name__ == '__main__':
	bot.polling(none_stop=True)

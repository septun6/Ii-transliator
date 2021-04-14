def get_work_list(message):
	work_list = []
	for ws in dict_for_work.keys():
		work_list.append(dict_for_work[ws][message])

	return work_list


list_of_writing_systems = ['Кирилиця', 'Latynycja (Variant sajtu Na časi)', 'Latynytsia (derzhavnyi variant)']

dict_of_code_writing_systems = {'Кирилиця' : 'ky', 'Kyrylycja': 'ky', 'Kyrylytsia': "ky",
	'Латиниця (Варіант сайту На часі)': "ln", 'Latynycja (Variant sajtu Na časi)' : 'ln', 
	'Latynytsia (Variant saitu Na chasi)': "ln", 'Латиниця (державний варіант)': "ld", 
	'Latynycja (deržavnyj variant)': "ld", 'Latynytsia (derzhavnyi variant)' : 'ld'}

dict_for_work = {
	"ky" : {
		"well_done" : "Молодець",
		"list_of_buttoms" : ["Перекласти текст", "Змінити систему письма бота"],
		"change_writing_system" : "Змінити систему письма бота",
		"translate" : "Перекласти текст",
		"welcome_back" : "З поверненням!",
		"choose_a_bot_writing_system" : "Оберіть систему письма бота:",
		"select_menu_item": "Оберіть пункт меню:",
		"bot's_writing_system_has_changed" : "Система письма бота успішно змінилася!",
		"writing_systems_to": ['Кирилиця', 'Латиниця (Варіант сайту На часі)', 'Латиниця (державний варіант)', 'Повернутися до меню'],
		"writing_systems_from": ['Кирилиця', 'Латиниця (Варіант сайту На часі)', 'Назад', 'Повернутися до меню'],
		"text_buttoms": ['Назад', 'Повернутися до меню'],
		"back_to_menu": 'Повернутися до меню',
		"back": 'Назад',
		"enter_text": "Введіть текст",
		"writing_system_text_to": "Оберіть систему письма повідомлення, на яку потрібно перекласти",
		"writing_system_text_from": "Оберіть систему письма повідомлення, з якої воно перекладається",
		"Error": "Не зрозумів, спробуйте ще раз!"},

	"ln" : {
		"well_done" : "Molodeć", 
		"list_of_buttoms" : ["Pereklasty tekst", "Zminyty systemu pyśma bota"],
		"change_writing_system" : "Zminyty systemu pyśma bota",
		"translate" : "Pereklasty tekst",
		"welcome_back" : "Z povernennjam!",
		"choose_a_bot_writing_system" : "Oberiť systemu pyśma bota:",
		"select_menu_item": "Oberiť punkt menju:",
		"bot's_writing_system_has_changed" : "Systema pyśma bota uspišno zminylasja!",
		"writing_systems_to": ['Kyrylycja', 'Latynycja (Variant sajtu Na časi)', 'Latynycja (deržavnyj variant)', 'Povernutysja do menju'],
		"writing_systems_from": ['Kyrylycja', 'Latynycja (Variant sajtu Na časi)', 'Nazad', 'Povernutysja do menju'],
		"text_buttoms": ['Nazad', 'Povernutysja do menju'],
		"back_to_menu": 'Povernutysja do menju',
		"back": 'Nazad',
		"enter_text": 'Vvediť tekst',
		"writing_system_text_to": 'Oberiť systemu pyśma povidomlennja, na jaku potribno pereklasty',
		"writing_system_text_from": 'Oberiť systemu pyśma povidomlennja, z jakoї vono perekladajeťsja',
		"Error": "Ne zrozumiv, sprobujte šče raz!"},

	"ld" : {
		"well_done" : "Molodets", 
		"list_of_buttoms" : ["Pereklasty tekst", "Zminyty systemu pysma bota"],
		"change_writing_system" : "Zminyty systemu pysma bota",
		"translate" : "Pereklasty tekst",
		"welcome_back" : "Z povernenniam!",
		"choose_a_bot_writing_system" : "Oberit systemu pysma bota:",
		"select_menu_item": "Oberit punkt meniu:",
		"bot's_writing_system_has_changed" : "Systema pysma bota uspishno zminylasia!",
		"writing_systems_to": ['Kyrylytsia', 'Latynytsia (Variant saitu Na chasi)', 'Latynytsia (derzhavnyi variant)', 'Povernutysia do meniu'],
		"writing_systems_from": ['Kyrylytsia', 'Latynytsia (Variant saitu Na chasi)', 'Nazad', 'Povernutysia do meniu'],
		"text_buttoms": ['Nazad', 'Povernutysia do meniu'],
		"back_to_menu": 'Povernutysia do meniu',
		"back": 'Nazad',
		"enter_text": 'Vvedit tekst',
		"writing_system_text_to": 'Oberit systemu pysma povidomlennia, na yaku potribno pereklasty',
		"writing_system_text_from": 'Oberit systemu pysma povidomlennia, z yakoii vono perekladaietsia',
		"Error": "Ne zrozumiv, sprobuite shche raz!"}}
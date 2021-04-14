#from kyrylica to latinica (official)

def next_let_func_1(text, route, index_letter, value_let, capital_letters, lower_case_letters): # check letter (next or past) is capital or lower_case
	meter_help = 0
	for index_new_letter in range(1, 5):
		try:
			check_letter = text[index_letter + index_new_letter * route] #end of string
		except IndexError:
			break
		if (text[index_letter + index_new_letter * route] in capital_letters) and (index_new_letter == 1): #next letter is capital
			value_let = 0
			break
		elif text[index_letter + index_new_letter * route] in lower_case_letters: #letter is lower-case
			value_let = 1
			break
		elif (text[index_letter + index_new_letter * route] in capital_letters) and (index_new_letter != 1): #letter is capital
			meter_help += 1
		elif not(text[index_letter + index_new_letter * route] in capital_letters) and not(text[index_letter + index_new_letter * route] in lower_case_letters): #this is not letter 
			meter_help -= 1
		elif meter_help == 2:
			value_let = 0
			break
	return value_let

def yi_func(text, index_letter, check_list, route):
	try:
		check_letter = text[index_letter + route] 
	except IndexError:
		return 3
	if check_letter in check_list:
		return 2
	else:
		return 3

def text_tran(text):
	
	alphabet = {'А': 'A', 'О': 'O', 'І': 'I', 'Е': 'E', 'У': 'U', 'И': 'Y', 'а': 'a', 'о': 'o', 'і': 'i', 'е': 'e', 'у': 'u', 'и': 'y', 
		'Б': 'B', 'В': 'V', 'Г': 'H', 'Ґ': 'G', 'Д': 'D', 'Ж': 'Zh', 'З': 'Z', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'П': 'P', 'Р': 'R', 
		'С': 'S', 'Т': 'T', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 
		'д': 'd', 'ж': 'zh', 'з': 'z', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'ф': 'f', 'х': 'kh', 
		'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch'}

	alphabet_set = ('а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 
		'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я', '’', "'", 'А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З', 'И', 'І', 'Ї', 'Й', 'К', 'Л', 
		'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я')

	lower_case_letters = ('а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 
		'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я')

	capital_letters = ('А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З', 'И', 'І', 'Ї', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 
		'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я')

	simple_letter = ('а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'ж', 'з', 'и', 'і', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 
		'ч', 'ш', 'щ', 'А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'З', 'И', 'І', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х') 

	big_double_simple_letter_set = ('Х', 'Ж', 'Ц', 'Ч', 'Ш', 'Щ')

	big_double_simple_letter = {'Ж': 'ZH', 'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Х': 'KH'}

	double_non_simple = [('Я', 'Ю', 'Ї', 'Є', 'Й'), 'я', 'ю', 'ї', 'є', 'й']

	alphabet_double_non_simple_let = {3: {'lower_case': 'y', 'capital': 'Y'}, 2: {'lower_case': 'i', 'capital': 'I'}, 0: {'Я': 'A', 'Ю': 'U', 
		'Ї': 'I', 'Є': 'E'}, 1: {'Я': 'a', 'Ю': 'u', 'Ї': 'i', 'Є': 'e', 'Й': '', 'я': 'a', 'ю': 'u', 'ї': 'i', 'є': 'e', 'й': ''}}

	letters_with = ('Д', 'Т', 'З', 'С', 'Ц', 'Л', 'Н', 'д', 'т', 'з', 'с', 'ц', 'л', 'н')

	index_letter, text_out, text_status = -1, '', True

	for letter in text:
		index_letter, value_let = index_letter + 1, -1
		if letter == '*':
			value_let = yi_func(text, index_letter, ('*'), 1) + yi_func(text, index_letter, ('*'), 2)
			text_status = not(text_status) if value_let == 4 else text_status
		if text_status == False:
			text_out += letter
			continue
		if letter in simple_letter:
			text_out += alphabet[letter]
		elif letter in big_double_simple_letter_set:
			value_let = next_let_func_1(text, 1, index_letter, value_let, capital_letters, lower_case_letters)
			if value_let == -1:
				value_let = next_let_func_1(text, -1, index_letter, value_let, capital_letters, lower_case_letters)
			if value_let == 1: # letter is lower-case
				text_out += alphabet[letter]
			else: #letter is capital
				text_out += capital_letters_with[letter]
		elif letter in double_non_simple or letter in double_non_simple[0]:
			value_first_letter_cap_or_low = 'capital' if letter in double_non_simple[0] else 'lower_case'
			value_letter_y_or_i = yi_func(text, index_letter, alphabet_set, -1)
			if letter in ('Й', 'й'):
				value_let = 1
			else:
				value_let = next_let_func_1(text, 1, index_letter, value_let, capital_letters, lower_case_letters)
				if value_let == -1:
					value_let = next_let_func_1(text, -1, index_letter, value_let, capital_letters, lower_case_letters)
				if value_let != 1:
					value_let = 0
			text_out += alphabet_double_non_simple_let[value_letter_y_or_i][value_first_letter_cap_or_low] + alphabet_double_non_simple_let[value_let][letter]
		elif letter in ('Ь', 'ь'):
			value_let = yi_func(text, index_letter, letters_with, -1)
			text_out = text_out + '' if value_let == 2 else text_out + letter
		else:
			text_out += letter
	return text_out
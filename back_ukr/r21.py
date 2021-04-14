# from latinica ("Na chasi") to kyrilica

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

def next_let_func_2(index_letter, text, letter_help, letter, alphabet_non_simp_let, check_list, route): #check next or past letter by choose letter
		try:
			check_letter = text[index_letter + route] 
		except IndexError:
			return alphabet_non_simp_let[letter]
		if check_letter in check_list:
			return alphabet_non_simp_let[letter_help][check_letter]
		else:
			return alphabet_non_simp_let[letter]

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

	alphabet = {'O': 'О', 'I': 'І', 'Y': 'И', 'Ї': 'Ї', 'o': 'о', 'i': 'і', 'y': 'и', 'ї': 'ї', 'B': 'Б', 
		'V': 'В', 'G': 'Г', 'Ğ': 'Ґ', 'D': 'Д', 'Ž': 'Ж', 'Z': 'З', 'J': 'Й', 'K': 'К', 'L': 'Л', 'M': 'М', 'N': 'Н', 'P': 'П', 'R': 'Р', 
		'S': 'С', 'T': 'Т', 'F': 'Ф', 'H': 'Х', 'C': 'Ц', 'b': 'б', 'v': 'в', 'g': 'г', 'ğ': 'ґ', 'd': 'д', 'ž': 'ж', 'z': 'з', 'j': 'й', 
		'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'p': 'п', 'r': 'р', 's': 'с', 't': 'т', 'f': 'ф', 'h': 'х', 'c': 'ц', 'Ď': 'Дь', 'Ť': 'Ть', 
		'Ź': 'Зь', 'Ś': 'Сь', 'Ć': 'Ць', 'Ľ': 'Ль', 'Ń': 'Нь', 'ď': 'дь', 'ť': 'ть', 'ź': 'зь', 'ś': 'сь', 'ć': 'ць', 'ľ': 'ль', 'ń': 'нь'}

	lower_case_letters = ('a', 'o', 'i', 'e', 'u', 'y', 'ї', 'b', 'v', 'g', 'ğ', 'ž', 'j', 'k', 'm', 'p', 'r', 'f', 'h', 'č', 'š', 'd', 't', 
		'z', 's', 'c', 'l', 'n', 'ď', 'ť', 'ź', 'ś', 'ć', 'ľ', 'ń')

	capital_letters_with = {'Ď': 'ДЬ', 'Ť': 'ТЬ', 'Ź': 'ЗЬ', 'Ś': 'СЬ', 'Ć': 'ЦЬ', 'Ľ': 'ЛЬ', 'Ń': 'НЬ'}

	capital_letters = ('A', 'O', 'I', 'E', 'U', 'Y', 'Ї', 'B', 'V', 'G', 'Ğ', 'Ž', 'J', 'K', 'M', 'P', 'R', 'F', 'H', 'Č', 'Š', 'D', 'T', 'Z',
		'S', 'C', 'L', 'N', 'Ď', 'Ť', 'Ź', 'Ś', 'Ć', 'Ľ', 'Ń')

	simple_letters = ('O', 'I', 'Y', 'Ї', 'o', 'i', 'y', 'ї', 'B', 'V', 'G', 'Ğ', 'D', 'Ž', 'Z', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'F', 
		'H', 'C', 'b', 'v', 'g', 'ğ', 'd', 'ž', 'z', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'f', 'h', 'c', 'ď', 'ť', 'ź', 'ś', 'ć', 'ľ', 'ń')

	capital_letters_with_list = ('Ď', 'Ť', 'Ź', 'Ś', 'Ć', 'Ľ', 'Ń')

	vowels_letters = ('A', 'E', 'U', 'a', 'e', 'u')

	alphabet_non_simp_let = {'Š': 'Ш', 'Šš': {'Č': 'Щ', 'č': 'Щ'}, 'š': 'ш', 'šš': {'Č': 'щ', 'č': 'щ'}, 'E': 'Е', 'U': 'У', 'A': 'А', 
	'e': 'е', 'a': 'а', 'u': 'у', 'Č': 'Ч', 'č': 'ч', 'J': 'Й', 'j': 'й', ' ': {'j': '', 'J': '', 'š': '', 'Š': ''}, 'jj': {'a': 'я', 'e': 'є', 'u': 'ю', 
	'A': 'я', 'U': 'ю', 'E': 'є'}, 'Jj': {'a': 'Я', 'e': 'Є', 'u': 'Ю', 'A': 'Я', 'U': 'Ю', 'E': 'Є'}}
	
	index_letter, text_out, text_status = -1, '', True
	
	for letter in text:
		index_letter, value_let = index_letter + 1, -1
		if letter == '*':
			value_let = yi_func(text, index_letter, ('*'), 1) + yi_func(text, index_letter, ('*'), 2)
			text_status = not(text_status) if value_let == 4 else text_status
		if text_status == False:
			text_out += letter
			continue
		if letter in simple_letters:
			text_out += alphabet[letter]
		elif letter in capital_letters_with_list:
			value_let = next_let_func_1(text, 1, index_letter, value_let, capital_letters, lower_case_letters)
			if value_let == -1:
				value_let = next_let_func_1(text, -1, index_letter, value_let, capital_letters, lower_case_letters)
			if value_let == 1: # letter is lower-case
				text_out += alphabet[letter]
			else: #letter is capital
				text_out += capital_letters_with[letter]
		elif letter in ['j', 'J']:
			text_out += next_let_func_2(index_letter, text, letter + 'j', letter, alphabet_non_simp_let, vowels_letters, 1)
		elif letter in ['š', 'Š']:
			text_out += next_let_func_2(index_letter, text, letter + 'š', letter, alphabet_non_simp_let, ['č', 'Č'], 1)
		elif letter in vowels_letters:
			text_out += next_let_func_2(index_letter, text, ' ', letter, alphabet_non_simp_let, ['j', 'J'], -1)
		elif letter in ['č', 'Č']:
			text_out += next_let_func_2(index_letter, text, ' ', letter, alphabet_non_simp_let, ['š', 'Š'], -1)
		else:
			text_out += letter
	return text_out
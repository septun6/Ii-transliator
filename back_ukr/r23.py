# from latinica (na chasi) to latinica (official)	

def next_let_func_1(text, route, index_letter, value_let, capital_letters, lower_case_letters):
	value_let = next_let_func_1_help(text, route, index_letter, value_let, capital_letters, lower_case_letters)
	if value_let == -1:
		value_let = next_let_func_1_help(text, route * -1, index_letter, value_let, capital_letters, lower_case_letters)
	return value_let

def next_let_func_1_help(text, route, index_letter, value_let, capital_letters, lower_case_letters): # check letter (next or past) is capital or lower_case
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

def next_let_func_2(index_letter, text, letter_help, letter, alphabet_non_simp_let, check_list, route, value_let): #check next or past letter by choose letter
		try:
			check_letter = text[index_letter + route] 
		except IndexError:
			return alphabet_non_simp_let[value_let][letter]
		if check_letter in check_list:
			return alphabet_non_simp_let[value_let][letter_help][check_letter]
		else:
			return alphabet_non_simp_let[value_let][letter]

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

	alphabet = {'A': 'A', 'E': 'E', 'O': 'O', 'I': 'I', 'Y': 'Y', 'a': 'a', 'e': 'e', 'o': 'o', 'i': 'i', 'y': 'y', 'B': 'B', 
		'V': 'V', 'G': 'H', 'Ğ': 'G', 'D': 'D', 'Ž': 'Zh', 'Z': 'Z', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'P': 'P', 'R': 'R', 
		'S': 'S', 'T': 'T', 'F': 'F', 'H': 'Kh', 'C': 'Ts', 'b': 'b', 'v': 'v', 'g': 'h', 'ğ': 'g', 'd': 'd', 'ž': 'zh', 'z': 'z', 
		'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'p': 'p', 'r': 'r', 's': 's', 't': 't', 'f': 'f', 'h': 'kh', 'c': 'ts', 'Ď': 'D', 'Ť': 'T', 
		'Ź': 'Z', 'Ś': 'S', 'Ć': 'Ts', 'Ľ': 'L', 'Ń': 'N', 'ď': 'd', 'ť': 't', 'ź': 'z', 'ś': 's', 'ć': 'ts', 'ľ': 'l', 'ń': 'n'}

	capital_letters_with = {'Ž': 'ZH', 'C': 'TS', 'H': 'KH'}

	simple_letters = ('G', 'Ğ', 'g', 'ğ', 'ž', 'h', 'c', 'Ď', 'Ť', 'Ź', 'Ś', 'Ľ', 'Ń', 'ď', 'ť', 'ź', 'ś', 'ć', 'ľ', 'ń')

	lower_case_letters = ('a', 'o', 'i', 'e', 'u', 'y', 'ї', 'b', 'v', 'g', 'ğ', 'ž', 'j', 'k', 'm', 'p', 'r', 'f', 'h', 'č', 'š', 'd', 't', 
		'z', 's', 'c', 'l', 'n', 'ď', 'ť', 'ź', 'ś', 'ć', 'ľ', 'ń')

	capital_letters = ('A', 'O', 'I', 'E', 'U', 'Y', 'Ї', 'B', 'V', 'G', 'Ğ', 'Ž', 'J', 'K', 'M', 
		'P', 'R', 'F', 'H', 'Č', 'Š', 'D', 'T', 'Z', 'S', 'C', 'L', 'N', 'Ď', 'Ť', 'Ź', 'Ś', 'Ľ', 'Ń', 'Ć')

	alphabet_set = ('a', 'o', 'i', 'e', 'u', 'y', 'ї', 'b', 'v', 'g', 'ğ', 'ž', 'j', 'k', 'm', 'p', 'r', 'f', 'h', 'č', 'š', 'd', 't', 
		'z', 's', 'c', 'l', 'n', 'ď', 'ť', 'ź', 'ś', 'ć', 'ľ', 'ń', 'A', 'O', 'I', 'E', 'U', 'Y', 'Ї', 'B', 'V', 'G', 'Ğ', 'Ž', 'J', 'K', 'M', 
		'P', 'R', 'F', 'H', 'Č', 'Š', 'D', 'T', 'Z', 'S', 'C', 'L', 'N', 'Ď', 'Ť', 'Ź', 'Ś', 'Ľ', 'Ń', 'Ć', '’', "'")

	alphabet_non_simp_let = {0: {'Š': 'SH', 'Šš': {'Č': 'SHCH', 'č': 'SHCH'}, 'Č': 'CH', ' ': {'š': '', 'Š': ''}}, 1: {'Š': 'Sh', 
		'Šš': {'Č': 'Shch', 'č': 'Shch'}, 'Č': 'Ch', ' ': {'š': '', 'Š': ''}}, 2: {'š': 'sh', 'šš': {'Č': 'shch', 'č': 'shch'}, 'č': 'ch', 
		' ': {'š': '', 'Š': ''}}}

	alphabet_double_non_simple_let = {3: {'lower_case': 'y', 'capital': 'Y'}, 2: {'lower_case': 'i', 'capital': 'I'}, 0: {'Ї': 'I'}, 
		1: {'Ї': 'i', 'J': '', 'ї': 'i', 'j': ''}}

	index_letter, text_out, text_status = -1, '', True

	for letter in text:
		index_letter, value_let, route = index_letter + 1, -1, 1
		if letter == '*':
			value_let = yi_func(text, index_letter, ('*'), 1) + yi_func(text, index_letter, ('*'), 2)
			text_status = not(text_status) if value_let == 4 else text_status
		if text_status == False:
			text_out += letter
			continue
		if letter in simple_letters:
			text_out += alphabet[letter]
		elif letter in capital_letters_with:
			value_let = next_let_func_1(text, route, index_letter, value_let, capital_letters, lower_case_letters)
			if value_let == 1: # letter is lower-case
				text_out += alphabet[letter]
			else: #letter is capital
				text_out += capital_letters_with[letter]
		elif letter in ('š', 'Š'):
			if letter == 'Š':
				value_let = next_let_func_1(text, route, index_letter, value_let, capital_letters, lower_case_letters)
				value_let = 0 if value_let != 1 else 1
			else:
				value_let = 2
			text_out += next_let_func_2(index_letter, text, letter + 'š', letter, alphabet_non_simp_let, ['č', 'Č'], 1, value_let)
		elif letter in ('č', 'Č'):
			if letter == 'Č':
				value_let = next_let_func_1(text, route, index_letter, value_let, capital_letters, lower_case_letters)
				value_let = 0 if value_let != 1 else 1
			else:
				value_let = 2
			text_out += next_let_func_2(index_letter, text, ' ', letter, alphabet_non_simp_let, ['š', 'Š'], -1, value_let)
		elif letter in ('J', 'j', 'ї', 'Ї'):
			value_first_letter_cap_or_low = 'capital' if letter in ('Ї', 'J') else 'lower_case'
			value_letter_y_or_i = yi_func(text, index_letter, alphabet_set, -1)
			if letter in ('J', 'j') or letter == "ї":
				value_let = 1
			else:
				value_let = next_let_func_1(text, route, index_letter, value_let, capital_letters, lower_case_letters)
				if value_let != 1:
					value_let = 0
			text_out += alphabet_double_non_simple_let[value_letter_y_or_i][value_first_letter_cap_or_low] + alphabet_double_non_simple_let[value_let][letter]
		else: 
			text_out += letter
	return text_out
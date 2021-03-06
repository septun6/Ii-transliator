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
		'V': 'V', 'G': 'H', '??': 'G', 'D': 'D', '??': 'Zh', 'Z': 'Z', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'P': 'P', 'R': 'R', 
		'S': 'S', 'T': 'T', 'F': 'F', 'H': 'Kh', 'C': 'Ts', 'b': 'b', 'v': 'v', 'g': 'h', '??': 'g', 'd': 'd', '??': 'zh', 'z': 'z', 
		'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'p': 'p', 'r': 'r', 's': 's', 't': 't', 'f': 'f', 'h': 'kh', 'c': 'ts', '??': 'D', '??': 'T', 
		'??': 'Z', '??': 'S', '??': 'Ts', '??': 'L', '??': 'N', '??': 'd', '??': 't', '??': 'z', '??': 's', '??': 'ts', '??': 'l', '??': 'n'}

	capital_letters_with = {'??': 'ZH', 'C': 'TS', 'H': 'KH'}

	simple_letters = ('G', '??', 'g', '??', '??', 'h', 'c', '??', '??', '??', '??', '??', '??', '??', '??', '??', '??', '??', '??', '??')

	lower_case_letters = ('a', 'o', 'i', 'e', 'u', 'y', '??', 'b', 'v', 'g', '??', '??', 'j', 'k', 'm', 'p', 'r', 'f', 'h', '??', '??', 'd', 't', 
		'z', 's', 'c', 'l', 'n', '??', '??', '??', '??', '??', '??', '??')

	capital_letters = ('A', 'O', 'I', 'E', 'U', 'Y', '??', 'B', 'V', 'G', '??', '??', 'J', 'K', 'M', 
		'P', 'R', 'F', 'H', '??', '??', 'D', 'T', 'Z', 'S', 'C', 'L', 'N', '??', '??', '??', '??', '??', '??', '??')

	alphabet_set = ('a', 'o', 'i', 'e', 'u', 'y', '??', 'b', 'v', 'g', '??', '??', 'j', 'k', 'm', 'p', 'r', 'f', 'h', '??', '??', 'd', 't', 
		'z', 's', 'c', 'l', 'n', '??', '??', '??', '??', '??', '??', '??', 'A', 'O', 'I', 'E', 'U', 'Y', '??', 'B', 'V', 'G', '??', '??', 'J', 'K', 'M', 
		'P', 'R', 'F', 'H', '??', '??', 'D', 'T', 'Z', 'S', 'C', 'L', 'N', '??', '??', '??', '??', '??', '??', '??', '???', "'")

	alphabet_non_simp_let = {0: {'??': 'SH', '????': {'??': 'SHCH', '??': 'SHCH'}, '??': 'CH', ' ': {'??': '', '??': ''}}, 1: {'??': 'Sh', 
		'????': {'??': 'Shch', '??': 'Shch'}, '??': 'Ch', ' ': {'??': '', '??': ''}}, 2: {'??': 'sh', '????': {'??': 'shch', '??': 'shch'}, '??': 'ch', 
		' ': {'??': '', '??': ''}}}

	alphabet_double_non_simple_let = {3: {'lower_case': 'y', 'capital': 'Y'}, 2: {'lower_case': 'i', 'capital': 'I'}, 0: {'??': 'I'}, 
		1: {'??': 'i', 'J': '', '??': 'i', 'j': ''}}

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
		elif letter in ('??', '??'):
			if letter == '??':
				value_let = next_let_func_1(text, route, index_letter, value_let, capital_letters, lower_case_letters)
				value_let = 0 if value_let != 1 else 1
			else:
				value_let = 2
			text_out += next_let_func_2(index_letter, text, letter + '??', letter, alphabet_non_simp_let, ['??', '??'], 1, value_let)
		elif letter in ('??', '??'):
			if letter == '??':
				value_let = next_let_func_1(text, route, index_letter, value_let, capital_letters, lower_case_letters)
				value_let = 0 if value_let != 1 else 1
			else:
				value_let = 2
			text_out += next_let_func_2(index_letter, text, ' ', letter, alphabet_non_simp_let, ['??', '??'], -1, value_let)
		elif letter in ('J', 'j', '??', '??'):
			value_first_letter_cap_or_low = 'capital' if letter in ('??', 'J') else 'lower_case'
			value_letter_y_or_i = yi_func(text, index_letter, alphabet_set, -1)
			if letter in ('J', 'j') or letter == "??":
				value_let = 1
			else:
				value_let = next_let_func_1(text, route, index_letter, value_let, capital_letters, lower_case_letters)
				if value_let != 1:
					value_let = 0
			text_out += alphabet_double_non_simple_let[value_letter_y_or_i][value_first_letter_cap_or_low] + alphabet_double_non_simple_let[value_let][letter]
		else: 
			text_out += letter
	return text_out
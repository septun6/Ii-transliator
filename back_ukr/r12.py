#! /usr/bin/env python
# -*- coding: utf-8 -*-
# from kyrilica to latinica (na chasi)

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

def next_let_func_2(text, index_letter, check_list, route):
    try:
        check_letter = text[index_letter + route] 
    except IndexError:
        return 3
    if check_letter in check_list:
        return 2
    else:
        return 3

def text_tran(text):

    alphabet = {'А': 'A', 'О': 'O', 'І': 'I', 'Е': 'E', 'У': 'U', 'И': 'Y', 'Ї': 'Ї', 'Є': 'Je', 'Я': 'Ja', 'Ю': 'Ju', 'а': 'a', 'о': 'o', 
        'і': 'i', 'е' : 'e', 'у': 'u', 'и': 'y', 'ї': 'ї', 'є': 'je', 'я': 'ja', 'ю': 'ju', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Ґ': 'Ğ', 'Д': 'D', 
        'Ж': 'Ž', 'З': 'Z', 'Й': 'J', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'Ф': 'F', 'Х': 'H', 
        'Ц': 'C', 'Ч': 'Č', 'Ш': 'Š', 'Щ': 'Šč', 'б': 'b', 'в': 'v', 'г': 'g', 'ґ': 'ğ', 'д': 'd', 'ж': 'ž', 'з': 'z', 'й': 'j', 'к': 'k', 
        'л': 'l', 'м': 'm', 'н': 'n', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'č', 'ш': 'š', 'щ': 'šč'}

    alphabet_set = ('а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 
        'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я', '’', "'", 'А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З', 'И', 'І', 'Ї', 'Й', 'К', 'Л', 
        'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я')

    other_letters = {'Д': 'Ď', 'Т': 'Ť', 'З': 'Ź', 'С': 'Ś', 'Ц': 'Ć', 'Л': 'Ľ', 'Н': 'Ń', 'д': 'ď', 'т': 'ť', 'з': 'ź', 'с': 'ś', 'ц': 'ć', 
        'л': 'ľ', 'н': 'ń', 'Щ': 'ŠČ', 'Є': 'JE', 'Ю': 'JU', 'Я': 'JA'}

    capital_letters = ('А', 'О', 'І', 'Е', 'У', 'И', 'Ї', 'Б', 'В', 'Г', 'Ґ', 'Ж', 'Й', 'К', 'М', 'П', 'Р', 'Ф', 'Х', 'Ч', 'Ш', 'Д', 'Т', 'З', 'С',
        'Ц', 'Л', 'Н', 'Щ', 'Я', 'Ю', 'Є', 'Ь')

    lower_case_letters = ('а', 'о', 'і', 'е', 'у', 'и', 'ї', 'б', 'в', 'г', 'ґ', 'ж', 'й', 'к', 'м', 'п', 'р', 'ф', 'х', 'ч', 'ш', 'д', 'т', 'з', 'с', 
        'ц', 'л', 'н', 'щ', 'я', 'ю', 'є', 'ь')

    simple_letters = ('А', 'О', 'І', 'Е', 'У', 'И', 'Ї', 'а', 'о', 'і', 'е', 'у', 'и', 'ї', 'Б', 'В', 'Г', 'Ґ', 'Ж', 'Й', 'К', 'М', 'П', 'Р', 
        'Ф', 'Х', 'Ч', 'Ш', 'б', 'в', 'г', 'ґ', 'ж', 'й', 'к', 'м', 'п', 'р', 'ф', 'х', 'ч', 'ш', 'щ', 'є', 'ю', 'я')

    letters_with = ('Д', 'Т', 'З', 'С', 'Ц', 'Л', 'Н', 'д', 'т', 'з', 'с', 'ц', 'л', 'н')

    b_double_letters = ('Щ', 'Є', 'Ю', 'Я')

    text_out, index_letter, text_status = '', -1, True

    # print(len(text))
    # print(text[0]+text[1])
    # print(ord(text[0]), len("П"))

    for letter in text:
        index_letter, value_let = index_letter + 1, -1
        if letter == '*':
            value_let = next_let_func_2(text, index_letter, ('*'), 1) + next_let_func_2(text, index_letter, ('*'), 2)
            text_status = not(text_status) if value_let == 4 else text_status
        if text_status == False:
            text_out += letter
            continue
        if letter in simple_letters:
            text_out += alphabet[letter]
        elif letter in letters_with:
            value_let = next_let_func_2(text, index_letter, ('Ь', 'ь'), 1)
            text_out = text_out + other_letters[letter] if value_let == 2 else text_out + alphabet[letter]
        elif letter in b_double_letters:
            value_let = next_let_func_1(text, 1, index_letter, value_let, capital_letters, lower_case_letters)
            if value_let == -1:
                value_let = next_let_func_1(text, -1, index_letter, value_let, capital_letters, lower_case_letters)
            text_out = text_out + alphabet[letter] if value_let == 1 else text_out + other_letters[letter]
        elif letter in ('Ь', 'ь'):
            value_let = next_let_func_2(text,index_letter, alphabet_set, -1)
            text_out = text_out + '' if value_let == 2 else text_out + letter
        else:
            text_out += letter
    return text_out    
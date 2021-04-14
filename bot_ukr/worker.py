import r12, r13, r23, r21

def translate(from_system, to_system, text):
	if from_system == "ky":
		if to_system == "ln":
			text_out = r12.text_tran(text)
		else:
			text_out = r13.text_tran(text)
	else:
		if to_system == "ky":
			text_out = r21.text_tran(text)
		else:
			text_out = r23.text_tran(text)
	return text_out
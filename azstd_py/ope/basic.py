def input_lines(prompt_head='', prompt_line='', end='/f'):
	print(prompt_head, end='')
	buf_lines = []
	is1stline = True
	while True:
		if is1stline == False:
			buf = input(prompt_line)
		else:
			buf = input()
			is1stline = False
		if buf == end:
			break
		buf_lines.append(buf)
	return '\n'.join(buf_lines)
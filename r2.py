
def read_file(filmname):
	lines = []
	with open(filmname, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	person = None
	吳淨如_word_count = 0
	吳淨如_sticker_count = 0
	吳怡臻_word_count = 0
	吳怡臻_sticker_count = 0
	for line in lines:
		s = line.split(" ")
		time = s[0]
		name = s[1]
		if name == '吳淨如':
			if s[2] == '貼圖':
				吳淨如_sticker_count += 1
			else:
				for m in s[2:]:
					吳淨如_word_count += len(m)
		elif name == '吳怡臻':
			if s[2] == '貼圖':
				吳怡臻_sticker_count += 1
			else:
				for m in s[2:]:
					吳怡臻_word_count += len(m)
	print('吳淨如說了', 吳淨如_word_count, '個字', '傳了', 吳淨如_sticker_count, '個貼圖')
	print('吳怡臻說了', 吳怡臻_word_count, '個字', '傳了', 吳怡臻_sticker_count, '個貼圖')
		# print(S)


def write_file(filename, lines):
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')		

def main():
	lines = read_file('line.txt')
	lines = convert(lines)
	# write_file('output.txt', lines)

main()
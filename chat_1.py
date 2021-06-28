# 讀取檔案
def read_file(filename):
	data = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f: # 出現\ufeff用utf-8-sig
		for line in f:
			data.append(line.strip())
	return data

def convert(data):
	person = None
	allen_word_count = 0
	allen_sticker_count = 0
	allen_photo_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_photo_count = 0
	for d in data:
		s = d.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_photo_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_photo_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('Allen傳了', allen_word_count, '個字', allen_sticker_count, '個貼圖', allen_photo_count, '張圖片')
	print('Viki傳了', viki_word_count, '個字', viki_sticker_count, '個圖片', viki_photo_count, '張圖片')

def write_file(filename, data):
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		for d in data:
			f.write(d + '\n')

def main():
	data = read_file('Line-Viki.txt')
	data = convert(data)
	# write_file('output.txt', data)

main()

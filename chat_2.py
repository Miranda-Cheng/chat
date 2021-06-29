data = []
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		data.append(line.strip())
for d in data:
	s = d.split(' ')
	time = s[0][:5]
	name = s[0][5:]
	print(name)

	# s[0]是字串，str.可以當成清單來看待，使用清單的分割法
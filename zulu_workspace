import sys

line = sys.stdin.readline()
linecount = 0
wordcount = 0
charactercount = 0
while line:
	print(line)
	linecount = linecount + 1
	for c in line: 
		if c == ' ':
			wordcount = wordcount + 1
		#if c in 'aeiouAEIOUüáÄäÁæəyíóèâồūōɛöĩéēƐāàëÌịôÜúÖûŌốòãụọệêếớųũīîBCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz': 
			#charactercount = charactercount + 1
		if c != ' ':
			charactercount = charactercount + 1
	line = sys.stdin.readline()
print("total lines: " + str(linecount))
print("word count: " + str(wordcount))
print("character count: " + str(charactercount))

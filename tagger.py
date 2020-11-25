import sys
frequency = {}
counter = 0
tagger = {}
word_frequency = {}
fd = open('wiki.conllu','r')
for line in fd.readlines():
	line = line.strip('\n')
	#continue if there is a tab in the line
	if '\t' not in line:
		continue
	counter = counter + 1
	#split row at tabs
	row = line.split('\t')
	#assign column 4 to value pos
	pos = row[3]
	zulu_word = row[1]
	#if the pos is in the frequency increment it by one starting from zero
	if pos not in frequency:
		frequency[pos] = 0
	frequency[pos] += 1
	# if the word from column 2 is in the tagger, it equals the dictionary
	if zulu_word not in tagger:
		tagger[zulu_word] = {}
	if pos not in tagger[zulu_word]:
		tagger[zulu_word][pos] = 0
	tagger[zulu_word][pos] += 1
	if zulu_word not in word_frequency:
		word_frequency[zulu_word] = 0
	#get a count of word frequency
	word_frequency[zulu_word] += 1
#	print(word_frequency[zulu_word])
#loop through pos tags
#for zulu_word in tagger:
#	tagger[zulu_word][pos] = 2
#	if zulu_word not in tagger:
#		print('KeyError: ', zulu_word)
#		continue
#	for pos in tagger:
#		if pos not in tagger[zulu_word]:
#			print('KeyError: ', pos)
#			continue
#		tagger[zulu_word][pos] += 1
print('# P', '\t', 'count', '\t', 'tag', '\t', 'form')
for x in frequency:
	s = frequency[x]/counter
	print('%.2f' %s, '\t', frequency[x], '\t', x, '\t', '_')
for z in tagger:
#	try to calculate word frequencies here
	for p in tagger[z]:
		r = tagger[z][p]/word_frequency[z]
		print('%.2f' %r, '\t', word_frequency[z], '\t', p, '\t', z)

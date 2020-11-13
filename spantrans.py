import sys

spanish = [] #list of spanish sentences
english = [] #list of english sentences
spa = [] #spanish words
eng = [] #english words
#text file has spanish and english translations separated by a tab character
fd = open('spanishtoenglish.txt','r')
for line in fd.readlines():
	#get rid of new line
	line = line.strip('\n')
	#assign variable s to spanish sentences and e to english sentences
	(s, e) = line.split('\t')
	#tokenise spanish sentence
	s = s.split(' ')
	#tokenise english sentence
	e = e.split(' ')
	#add tokenised spanish sentence to spanish file
	spanish.append(s)
	#add tokenised english sentence to english file
	english.append(e)
	#tokenis words in spanish sentences
	spa = spa + s
	#tokenise words in english sentences
	eng = eng + e
spa = list(set(spa))
eng = list(set(eng))


m = {}

#for each of the vocabulary items in the spanish list (initializes matrix)
for spa_word in spa:
	#if the vocabulary item isn't in the list the value of the item is the list
	if spa_word not in m:
		m[spa_word] = {}
	#for each of the vocabulary items in the english list...?
	for eng_word in eng:
		m[spa_word][eng_word] = 0
#COLLECT THE COUNTS
	#number sentences using i
for i in range(0,len(spanish)):
	spa_sent = spanish[i]
	eng_sent = english[i]
		#loop through spanish words in sentences
	for spa_word in spa_sent:
#			m[w1][w2] = 2
			#loop through english words in sentence
		if spa_word not in m:
			print('KeyError: ', spa_word)
			continue
		for eng_word in eng_sent:
				#add 1 to value of m[w1][w2] for words in sentences with matching indexes
			if eng_word not in m[spa_word]:
				print('KeyError: ', eng_word)
				continue
			m[spa_word][eng_word] += 1

print('\t' + '\t'.join(eng))
for spa_word in m:
	print('%s\t' % (spa_word), end='')
	for eng_word in m[spa_word]:
		print('%d\t' % (m[spa_word][eng_word]), end='')
	print('')

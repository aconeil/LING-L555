import sys
#list for singular forms
POStagger = {}
#Dictioanry for lemma form
lemma = {}
#dictionary for plural forms
plural_tagger = {}
#read in tsv dictionary file
fd = open('postag.tsv','r')
for line in fd.readlines():
	line = line.strip('\n')
	if '\t' not in line:
		continue
        #split rows at tabs
	row = line.split('\t')
        #assign column 3 to pos
	pos = row[2]
        #assign column 4 to basaa word in singular
	entry = row[3]
        #assign column 5 to basaa word in plural
	plural = row[4]
	plural_tagger[plural] = entry
	lemma[entry] = entry
	if entry not in POStagger:
		POStagger[entry] = set()
	POStagger[entry].add(pos)
tag_to_freq = {}
#load in the unigram file
for line in open('unigram.tsv'):
	if line.strip() == '':
		continue
	if line[0] == '#':
		continue
	row = line.split('\t')
	#where e.g. tag_to_freq["PRON"] = 4
	tag = row[2]
	count = int(row[1])
	tag_to_freq[tag] = count
print(tag_to_freq)
corpus = sys.stdin.readlines()
for line in corpus:
	line = line.strip('\n')
	line = line.casefold()
	if '\t' not in line:
		print(line)
		continue
        #split rows in corpus by tab
	row = line.split('\t')
	form = row[1]
	if form in POStagger:
		#if there is only one pos for a form make column 4 that form
		if len(POStagger[form]) == 1:
			row[3] = list(POStagger[form])[0]
		#if there is more than one pos for a form
		elif len(POStagger[form]) > 1:
			maxfreq = 0
			maxtag = '_'
			for tag in POStagger[form]:
				if tag in tag_to_freq:
					if tag_to_freq[tag] > maxfreq:
						maxfreq = tag_to_freq[tag]
						maxtag = tag
			row[3] = maxtag
	elif form in '?:;.()-*[]':
		row[3] = 'PUNCT'
	else:
		row[3] = 'X'
	print('\t'.join(row))

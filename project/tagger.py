import sys
#list for singular forms
POStagger = {}
#Dictioanry for lemma form
lemma = {}
#create list for pos
poslist = []
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
corpus = sys.stdin.readlines()
for line in corpus:
        line = line.strip('\n')
        line = line.casefold()
        if '\t' not in line:
                print(line)
                continue
        #split rows in corpus by tab
        row = line.split('\t')
#       print(poslist)
#       if row[1] in POStagger:
#               print(row[0], row[1], POStagger[row[1]])
#       else:
#               print(row)
#       print(poslist)
#       pos.append()
        #assign the value of the second column to be used as the tag
        form = row[1]
        if form in POStagger:
                if len(POStagger[form]) == 1:
                        row[3] = list(POStagger[form])[0]
        print('\t'.join(row))


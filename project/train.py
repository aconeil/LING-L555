#frequency table that shows the freuquency of which a word is assigned to different pos tags
import sys
#dictionary for frequency of word to pos tag
frequency = {}
#dictionary for pos tags
tagger = {}
#dictionary for words
word_frequency = {}
counter = 0
fd = open('bas.conllu','r')
for line in fd.readlines():
        line = line.strip('\n')
        if '\t' not in line:
                continue
        #increment counter by one to indicate total entries?
        counter = counter + 1
        #split row at tabs
        row = line.split('\t')
        #assign column 4 to pos value
        pos = row[3]
        lemma_form = row[2]
        entry_form = row[1]
        #if the pos is i nthe frequency increment it by 1
        if pos not in frequency:
                frequency[pos] = 0
        frequency[pos] += 1
        #of the basaa lemma is in the tagger it equals the dictionary
        if lemma_form not in tagger:
                tagger[lemma_form] = {}
        if pos not in tagger[lemma_form]:
                tagger[lemma_form][pos] = 0
        tagger[lemma_form][pos] += 1
        if lemma_form not in word_frequency:
                word_frequency[lemma_form] = 0
        word_frequency[lemma_form] += 1
print('#P', '\t', 'count', '\t', 'tag', '\t', 'form')
#for a value in frequency
for x in frequency:
        #divide the key of frequency[x] by the counter
        s = frequency[x]/counter
        print('%.2f' %s, '\t', frequency[x], '\t', x, '\t', '_')
for b in tagger:
        for p in tagger[b]:
                r = tagger[b][p]/word_frequency[b]
                print('%.2f' %r, '\t', word_frequency[b], '\t', p, '\t', b)

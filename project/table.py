import sys

sentencecounter = 0
POS = "_"
MORPHEME = "_"
GLOSS = "_"
LEMMA = "_"
text = sys.stdin.readlines()
for c in text:
        c = c.replace('=',' = ')
        c = c.replace(',',' , ')
        c = c.replace('.',' . ')
        c = c.replace('>',' > ')
        c = c.replace('<', ' < ')
        c = c.replace(':',' : ')
        c = c.replace(';',' ; ')
        c = c.replace('"',' " ')
        c = c.replace('·',' · ')
        c = c.replace('(',' ( ')
        c = c.replace(')',' ) ')
        c = c.strip('\n')
        if c =='':
                continue
        sentencecounter = sentencecounter + 1
        tokens = c.strip('\n')
        tokens = tokens.split(' ')
        tokencounter = 0
        print("# sent_id =" + str(sentencecounter))
        print("# text =" + c.strip('\n'))
        for token in tokens:
                if token =='':
                        continue
                tokencounter = tokencounter + 1
                print('%d\t%s\t%s\t%s\t%s\t%s\t' % (tokencounter, token, LEMMA, POS, MORPHEME, GLOSS))
        print()


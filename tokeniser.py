import sys

counter = 0
LEMMA = '_'
UPOS = '_'
XPOS = '_'
FEATS = '_'
HEAD = '_'
DEPREL = '_'
DEPS = '_'
MISC = '_'

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
	c = c.strip('\n')
	if c =='':
		continue
	counter = counter + 1
	tokens = c.strip('\n')
	tokens = tokens.split(' ')
	tokencounter = 0
#	print(tokens)
	print("# sent_id =" + str(counter))
	print("# text = " + c.strip('\n'))
	for token in tokens:
		if token =='':
			continue
		tokencounter = tokencounter + 1 
#		print("# sent_id =" + str(counter))
#		print("# text =" + c)
		print('%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t' % (tokencounter,token,LEMMA,UPOS,XPOS,FEATS,HEAD,DEPREL,DEPS,MISC))
	print()

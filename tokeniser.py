import sys

counter = 0

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
	counter = counter + 1
	tokens = c.split(' ')
	tokencounter = 0
	for token in tokens:
		tokencounter = tokencounter + 1
		print(tokencounter,token)

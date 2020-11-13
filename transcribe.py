import sys

#create a dict called IPAkey
IPAkey = {}

#Open my IPA key file in read mode
fd = open('IPAkey.txt','r')
#read each line
for line in fd.readlines():
	#strip new line
	line = line.strip('\n')
	#split on tab character and put values into tuple
	(f, w) = line.split('\t')
	IPAkey[f] = w
#print(IPAkey)
#read input and call it text
input_text = sys.stdin.readlines()
for line in input_text:
#	print('f:', f)
	#get rid of newline
	line = line.strip('\n')
	if '\t' not in line:
		print(line)
		continue
	#split at spaces to get individual words
	tokens = line.split('\t')
	#replace values matching f with w
	transcription = tokens[1]

	for c in IPAkey:
#		print('c:', c, 'f:', f)
		transcription = transcription.replace(c, IPAkey[c])
#	print(transcription)
#	print(tokens)
	tokens[9] = "IPA=" + transcription
	print('\t'.join(tokens))

	#assign f in key to w
#	token[w] = f
#for a letter in the token
#for c in token:
#replace any instance of the variable f with c
	#c = c.replace(f, w)
	#print what is happening


import sys

text = sys.stdin.read()
for c in text:
	if c in ', :;·"/':
		print(text.replace(c,'\n'))

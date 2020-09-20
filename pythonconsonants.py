import sys

consonants = 0

for c in sys.stdin.read():
	if c in 'BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz':
		consonants = consonants + 1
print("consonant count:" + str(consonants))

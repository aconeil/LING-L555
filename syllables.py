import sys

vowel = 0
word = 0
avgsyl = 0

for c in sys.stdin.read():
	if c in 'aeiouAEIOUüáÄäÁæəyíóèâồūōɛöĩéēƐāàëÌịôÜúÖûŌốòãụọệêếớųũīî':
		vowel = vowel + 1
	if c == ' ':
		word = word + 1

avgsyl = vowel/word
print("average syllables per word: " + str(avgsyl))

import sys

vowels = 0

for c in sys.stdin.read():
	if c in 'aeiouAEIOUüáÄäÁæəyíóèâồūōɛöĩéēƐāàëÌịôÜúÖûŌốòãụọệêếớųũīî':
		vowels = vowels + 1
print("vowel count:" + str(vowels))

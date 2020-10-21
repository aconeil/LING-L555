import sys

freq = []

fd = open('freq.txt', 'r')
for line in fd.readlines():
	line = line.strip('\n')
	row = line.split('\t')
	if len(row) != 2:
		print('Fail', len(row), row)
		sys.exit()
	(f, w) = line.split('\t')
	freq.append((int(f), w))
freq.sort(reverse=True)
rank = 1 # Highest rank
min = freq[0][0] # The current minimum
ranks = [] # List of ranks
for i in range(0, len(freq)):
	if freq[i][0] < min:
		rank = rank + 1
		min = freq[i][0]
	ranks.append((rank, freq[i][0], freq[i][1]))
#print(ranks[0:4])
#print('%d\t%d\t%s' % (w[0], w[1], w[2]))
fd = open('rank.txt', 'w+')
for w in ranks:
	fd.write('%d\t%d\t%s\n' % (w[0], w[1], w[2]))
	print('%d\t%d\t%s\n' % (w[0], w[1], w[2]))
fd.close()

s = input("Enter string: ")
d = {}
for i in range(len(s)):
	if (s[i] not in d):
		d[s[i]] = 1
	else:
		d[s[i]] += 1

print(d)
st = input("Enter word: ")
print(s.find(st))
print(sorted(s.split(" ")))

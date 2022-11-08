l = input()
word = l.split()
words = {}
for word in l.split():
    words[word] = words.get(word,0) + 1

for ww in sorted(words):
    print("{} : {}".format(ww,words[ww]))
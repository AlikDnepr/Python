with open("example.txt") as inf:
    s = inf.read().replace('\n', ' ').lower().split()
words = {}
words[s[0]] = 1
k = 0

for i in range (0,len(s)-1):
    if s[i] in words == words[i]:
        k+=1
        words[s[i]] = k
    else:
        words[s[i]] = 1

word = list(words.keys())
word_count = list(words.values())
max_word_count = 0
min_word = ''

for i in range(len(word_count)-1):
    if  word_count[i] > max_word_count:
        max_word_count = word_count[i]
        min_word = word[i]
    elif word_count[i] == max_word_count:
        if word[i] < min_word:
            min_word = word[i]

print(min_word,max_word_count)
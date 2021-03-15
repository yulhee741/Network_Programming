print("Your word:", end=' ')
word = input()

pos = word.find('a')
print(word[:pos+1])
print(word[pos+1:])


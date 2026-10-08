s=input("enter a sentence:")
print(s)
wordsList=s.split()
print(wordsList)
unique =set(wordsList)
for word in unique:
    print(f"{word} occurs {wordsList.count(word)}times")
    

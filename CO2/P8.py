def longestword(word):
    max_length=len(word[0])
    for item in word:
        length=len(item)
        if length>max_length:
            max_length
    return max_length
words=input("enter a list of words separted by space:")
word=words.split()
result=longestword(word)
print(f"the lenght of the longest word id:{result}")


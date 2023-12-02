#palindrom app:Sentences, words and numbers that are pronounced the same backwards are called words.
word=input("enter word:")
print("inverse of", word,"is",word[::])
if word==word[::]:
    print("the word is palindrom")
else:
    print("the word is not palindrom")

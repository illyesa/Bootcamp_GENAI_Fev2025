
#1
def Sorting():
    words = input("Enter comma-separated words: ").split(',')
    sorted_words = sorted([word.strip() for word in words])
    print(','.join(sorted_words))

Sorting()

#2
def longest_word(sentence):
    words = sentence.split()
    max_word=words[0]
    for word in words:
        if len(word) > len(max_word):
            max_word= word
    return max_word

print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))

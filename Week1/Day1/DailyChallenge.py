
#1
number=int(input("chose a number :"))
length=int(input("chose a length :"))
a=[]
for i in range(1,length+1):
    a.append(number*i)
print(a)

#2
word=input("chose your word :")
new_word=""
for i in range(0,len(word)-1):
    if word[i] != word[i+1]:
        new_word += word[i]
new_word += word[-1]
print(new_word)

# #1
# def add_two_numbers(a,b):
#     return a + b

# print(add_two_numbers(3,5))
# print(add_two_numbers(10,20))
# #2
# def greet(name):
#     print(f"Hello, {name}!")

# greet("Alice")
# greet("Bob")
# #3
# def check_even_odd(a):
#     if a % 2 == 0 :
#         print("Even")
#     else:
#         print("Odd")
# check_even_odd(198)

# #4
# def sum_list(a):
#     s=0
#     for b in a :
#         s+=b
#     print(s)
# sum_list([1, 2, 3, 4])
# sum_list([5, 5, 5])

# #5
# def print_days():
#     d = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#     for e in d:
#         print(e)
# print_days()

# #6
# def check_sign(a):
#     if a<0:
#         print("Negative")
#     elif a>0:
#         print("Positive")
#     else:
#         print("Zero")
# check_sign(10)
# check_sign(-5)
# check_sign(0)

# #7
# def repeat_word(a, b):
#     for i in range(b):
#         print(a)
# repeat_word("hello", 3)
# repeat_word("goodbye", 2)

# #8
# def find_largest(a):
#     b=a[0]  #max(a)
#     for i in a:
#         if b<i:
#             b=i
#     return b
# print(find_largest([1, 2, 3, 4]))
# print(find_largest([10, 20, 5]))

# #9
# def check_letter(a,b):
#     return b in a
# print(check_letter("apple","a"))
# print(check_letter("banana","z"))

# #10
# def count_to_number(a):
#     for i in range(a):
#         print(i+1)
# count_to_number(5)
# count_to_number(3)


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# from collections import Counter

# l = [1, 1, 2, 3, 3, 4, 4, 5, 5]
# print(Counter(l))  # see what this returns!

# string = "aweosakjdsaldwjdwq"
# print(Counter(string))

# s = 'this is such a nice nice nice thing that is nice!'
# c = Counter(s.split())
# print(c)

# n=[num**2 for num in range(10)]
# print(n)

# m=[chr(num) for num in range(65, 91)]  
# # Output: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
# #          'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
# #          'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# print(m)

# vowels = []
# for letter in 'awesome':
#     if letter in ['a', 'e', 'i', 'o', 'u']:
#         vowels.append(letter)

# print(vowels)  # Output: ['a', 'e', 'o', 'e']

# vowels = [letter for letter in 'awesome' if letter in ['a', 'e', 'i', 'o', 'u']]
# print(vowels)  # Output: ['a', 'e', 'o', 'e']


# l=len([word for word in "the quick brown fox jumps over the lazy dog".split(" ") if len(word) == 3])
# print(l)

# l=[odd for odd in range(21) if odd%2==0]
# print(l)

# d = dict(name='Elie', job='Instructor')

# for k in d:
#     print(k)

# d = dict(name='Elie', job='Instructor')

# for key, value in d.items():
#     print(f"{key}: {value}")

# def add_numbers(a, b, c):
#     return a + b + c

# numbers = [1, 2, 3]
# more_numbers = (4, 5, 6)

# # Using * to unpack lists/tuples
# print(add_numbers(*numbers))  # 6
# print(add_numbers(*more_numbers))  # 15



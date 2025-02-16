
# perso={
#     "first_name" : "John",
#     "first_name" : "John",
#     "last_name" : "Doe",
#     "favorite_hobby" : "Python",
#     "sports_hobby" : "gym",
#     "age" : 82,
#     }
# playlist = {
#     'title': "Hello World",
#     'author': "Planet",
#     'songs': [
#         {
#             'song_title': "Song One",
#             'artist': ['Artist 1', 'Artist 2'],
#             'duration': 4.31,
#         },
#         {
#             'song_title': "Song Two",
#             'artist': ['Artist 1'],
#             'duration': 2.53,
#         },
#         {
#             'song_title': "Song Three",
#             'artist': ['Artist 1', 'Artist 2', 'Artist 3'],
#             'duration': 3.43,
#         }
#     ]
# }
# total_duration = 0
# for i in playlist["songs"] :
#     total_duration += i["duration"]

# print(total_duration)

# words = ['PYTHON', 'JOHN', 'chEEse', 'hAm', 'DOE', '123']
# uppercased_words = [word for word in words if word.isupper()]

# print(uppercased_words)

# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# ## create an instance of the class
# p = Point(3,4)

# ## access the attributes
# print("p.x is:", p.x)
# print("p.y is:", p.y)

# def calculate_average(sentence):
#     list_of_word = sentence.split()
#     total=0
#     for word in list_of_word:
#         total+= len(word)
#     return round(total/len(list_of_word),1)
# print(calculate_average("bonjour comment cela va"))


# class Circle:
#     color = "red"

# class NewCircle(Circle):
#     color = "blue"

# nc = NewCircle
# print(nc.color)
# # >> What will be the output ?
# class Circle:
#     def __init__(self, diameter):
#       self.diameter = diameter

#     def grow(self, factor=2):
#         """grows the circle's diameter by factor"""
#         self.diameter = self.diameter * factor

# class NewCircle(Circle):
#     def grow(self, factor=2):
#         """grows the area by factor..."""
#         self.diameter = (self.diameter * factor * 2)

# nc = NewCircle(1)
# print(nc.diameter)

# nc.grow()

# print(nc.diameter)
# # >> What will be the output

print(divmod(8,3))
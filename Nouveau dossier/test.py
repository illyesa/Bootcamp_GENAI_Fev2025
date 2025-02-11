
perso={
    "first_name" : "John",
    "first_name" : "John",
    "last_name" : "Doe",
    "favorite_hobby" : "Python",
    "sports_hobby" : "gym",
    "age" : 82,
    }
playlist = {
    'title': "Hello World",
    'author': "Planet",
    'songs': [
        {
            'song_title': "Song One",
            'artist': ['Artist 1', 'Artist 2'],
            'duration': 4.31,
        },
        {
            'song_title': "Song Two",
            'artist': ['Artist 1'],
            'duration': 2.53,
        },
        {
            'song_title': "Song Three",
            'artist': ['Artist 1', 'Artist 2', 'Artist 3'],
            'duration': 3.43,
        }
    ]
}
total_duration = 0
for i in playlist["songs"] :
    total_duration += i["duration"]

print(total_duration)

words = ['PYTHON', 'JOHN', 'chEEse', 'hAm', 'DOE', '123']
uppercased_words = [word for word in words if word.isupper()]

print(uppercased_words)

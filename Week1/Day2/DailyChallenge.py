def letter_indices(word):
    letter_dict = {}

    for index, letter in enumerate(word):
        if letter in letter_dict:
            letter_dict[letter].append(index)
        else:
            letter_dict[letter] = [index]
    
    return letter_dict


# Ask the user for a word
user_word = input("Enter a word: ").strip().lower()  # Convert to lowercase to handle uniform cases

# Generate the dictionary
result = letter_indices(user_word)

# Display the result
print(result)
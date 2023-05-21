sentence = "This is how to pick out only the beginning letter"

# Create a variable to store the current word.
current_word = ""

# Create a variable to store the beginning letter of the current word.
extractor = ""

# Loop over the characters in the sentence.
for character in sentence:
    # If the current character is a space, then it can reach to the end of the current word.
    if character == " ":
        # Print the beginning letter of the current word.
        print(extractor)

        # Reset the current word and beginning letter variables.
        current_word = ""
        extractor = ""

    # Otherwise, this is still in the current word.
    else:
        # Add the current character to the current word.
        current_word += character

        # Set the beginning letter of the current word to the current character.
        extractor = character

# Print the beginning letter of the last word.
print(extractor)

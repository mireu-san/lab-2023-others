sentence = "This is how to pick out only the first letter"

# Create a variable to store the current word.
current_word = ""

# Create a variable to store the first letter of the current word.
first_letter = ""

# Loop over the characters in the sentence.
for character in sentence:
    # If the current character is a space, then we have reached the end of the current word.
    if character == " ":
        # Print the first letter of the current word.
        print(first_letter)

        # Reset the current word and first letter variables.
        current_word = ""
        first_letter = ""

    # Otherwise, this is still in the current word.
    else:
        # Add the current character to the current word.
        current_word += character

        # Set the first letter of the current word to the current character.
        first_letter = character

# Print the first letter of the last word.
print(first_letter)

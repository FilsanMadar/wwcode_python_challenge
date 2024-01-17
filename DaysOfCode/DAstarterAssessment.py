def decode():
    # Open and read the content of the file
    with open('/Users/FilsanM/Documents/PS-2021/coding_qual_input.txt', 'r') as file:
        content = file.readlines()

    # Remove any newline characters and spaces
    content = [line.strip() for line in content if line.strip() != '']

    # Split the content into numbers and words
    # Assuming the format is number and word pairs on each line
    number_word_pairs = [line.split() for line in content]
    numbers = [int(pair[0]) for pair in number_word_pairs]
    words = [pair[1] for pair in number_word_pairs]

    # Create a dictionary mapping numbers to words
    num_to_word = dict(zip(numbers, words))

    # Function to construct the pyramid and decode the message
    def decode_message(numbers, num_to_word):
        # Sort the numbers in ascending order
        sorted_numbers = sorted(numbers)
        # Retrieve the words at the end of the pyramid
        end_words = [num_to_word[num] for num in sorted_numbers[-2:]]
        # Concatenate them to form the decoded message
        decoded_message = ' '.join(end_words)
        return decoded_message

    # Call the function and print the result
    decoded_msg = decode_message(numbers, num_to_word)
    print('Decoded message:', decoded_msg)

# Call the main decode function
decode()

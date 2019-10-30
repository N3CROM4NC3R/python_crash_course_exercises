filename = 'common_words.txt'

try:

    with open(filename,'r') as file_object:
        history = file_object.read()
        word_count = history.lower().count('the')
        print(word_count)
        
except FileNotFoundError:
    print("File not found")
from vocab import vocab_list
def check(input_str):
    j = None
    for i in input_str:
        if (i == ',' and j == ' ') or (i == ' ' and j == ','):
            print("Invalid input. Please enter again.")
            return True
        else:
            j = i
    return False

if __name__ == "__main__":
    while True:
        w = input("Enter the new word you learned: ")
        m = input("Enter the meaning of that word: ")
        eg = input("Enter a use-case example: ")
        
        input_keywords = input("Enter keywords comma-separated: ")
        if not check(input_keywords):
            word = {
                'word': w,
                'meaning': m,
                'example': eg,
                'keyword': input_keywords.split(',')
            }

            vocab_list[len(vocab_list.keys())] = word
            print("Vocablist updated!")
            break 

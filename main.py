def main():
    with open("books/frankenstein.txt") as f:
    # Opens up the file and reads it in to the contents variable
        file_contents = f.read()
        #print(file_contents) #Prints contents variable to the console

        #prints the number of words
        number_of_words = count(file_contents)
        #print(f"The book conatains {number_of_words} words.")

        #print a dictionary with characters in the text and how often they appeared
        char_dic = let_dict(file_contents)
        #convert the character dictionary into a list of dictionaries for sorting
        char_list = [{"char": key, "num": value} for key, value in char_dic.items()]
        #print(f"The following characters were used in the text with the following numbers: {char_dic}")

        #Report
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{number_of_words} words found in the document\n")
        #sort and print the characters by frequency
        char_list.sort(reverse=True, key=sort_on)
        for item in char_list:
            print(f"The '{item['char']}' character was found {item['num']} times")
        print("--- End report ---")

        


def count(text):
     #splits the file contents into words and puts them all in a list
     word_list = text.split()
    #count function returns the number of items in the word_list
     return len(word_list)



def let_dict(text):
     #converts all upper case to lower case letters
     low_text = text.lower()
     #initialize a dictionary
     dic = {}
     #loops over all characters in the text string, adds the character as a key with value 1 if it is new
     #increases the value by 1 if it is not new
     for letter in low_text:
          #if the letter is already a key in the dictionary, increase it's value by 1
          if letter in dic:
               dic[letter] += 1
          #else add the key to dic and make it's value 1
          else:
               dic[letter] = 1
     return dic

def sort_on(dic):
     return dic["num"]

# This protective if condition ensures 'main()' is called at the right moment.
if __name__ == '__main__':
        main()
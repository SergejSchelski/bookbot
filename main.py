def main():
    with open("books/frankenstein.txt") as f:
    # Opens up the file and reads it in to the contents variable
        file_contents = f.read()
        #print(file_contents) #Prints contents variable to the console
        #prints the number of words
        number_of_words = count(file_contents)
        print(f"The book conatains {number_of_words} words.")
        
def count(text):
     #splits the file contents into words and puts them all in a list
     word_list = text.split()
    #count function returns the number of items in the word_list
     return len(word_list)

# This protective if condition ensures 'main()' is called at the right moment.
if __name__ == '__main__':
        main()
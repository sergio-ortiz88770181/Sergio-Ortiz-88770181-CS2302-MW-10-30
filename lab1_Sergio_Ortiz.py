#CS 2302 Data Structures Fall 2019 MW 10:30
#Sergio Ortiz
#Assignment - Lab #1
#Instructor - Olac Fuentes
#Teaching Assistant - Anindita Nath
#September 4, 2019
#This program will find all the anagrams from a  user given word


import time

#anagram finder(): will find the anagrams of a word
#input - scrambled_words: a list containing permutations of the
#                         user's word
#      - words_set: a set with most of the common English words
#      - anagram_list: a list where we will add the anagrams
#
#output - a list with the anagrams
def anagram_finder(scrambled_words ,words_set, anagram_list):
    for word in scrambled_words:
        if(word in words_set):
            anagram_list.append(word)
    anagram_list = remove_duplicates(anagram_list)
    anagram_list.sort()
    return anagram_list

#make_prefix_set(): makes a set with all the prefixes
#                   in the word_set
#input -words_set: a set with most of the common
#                  English words
#output - a set with all the prefixes from the words_set
def make_prefix_set(words_set):
    prefix_set = set()
    temp_list = []
    for word in words_set:
        temp_list = find_prefixes(word)
        for prefix in temp_list:
            prefix_set.add(prefix)
    return prefix_set

#make_set(): will make a set with most of the common
#          english words by reading them off a file
#          and adding them to a set
#input - none
#output - a set with English words
def make_set():
    english_words_file = open("words_alpha.txt", "r")
    words_set = set()

    for word in english_words_file:
        word = word.strip('\n')
        words_set.add(word)
    english_words_file.close()
    return words_set

#find_prefixes(): will find all the prefixes of a word
#input -string: a word
#output - a list with all the prefixes of the given word
def find_prefixes(string):
    prefixes_list = []
    for i in range(len(string)):
        prefixes_list.append(string[:i])
    return prefixes_list

#remove_duplicates(): will remove duplicates from a list
#                     by adding all the elements to a set
#                     then returning them back to the list
#input - list: a list with words, might contain duplicates
#output - list: a list without any duplicate words
def remove_duplicates(list):
    duplicate_remover = set()
    for word in list:
        duplicate_remover.add(word)

    new_list = []
    for word in duplicate_remover:
        new_list.append(word)

    return new_list

#scrambler(): will take a word and return its permutations
#input -remaining: a list with the remaining words (not scrambled)
#      -scrambled: a list with the scrambled words
#output -none, but the scrambled words are appended to a list
#        scrambled_words
def scrambler(remaining, scrambled, prefixes_set):
    if(len(remaining) == 0):
        scrambled_words.append(scrambled)
    else:
        seen = set()
        for letter in range(len(remaining)):
            if(letter not in seen):
                seen.add(letter)
                if(scrambled in prefixes_set):
                    scramble_letters = remaining[letter]
                    remaining_letters = remaining[:letter] + remaining[letter + 1:]
                    scrambler(remaining_letters, scrambled + scramble_letters, prefixes_set)


words_set = make_set()
prefixes_set = make_prefix_set(words_set)
user_word = input("Enter a word or empty string to finish ")

while(user_word != ""):
    if(user_word in words_set):
        scrambled_words = []
        start = time.time()
        scrambler(user_word, "", prefixes_set)
        anagrams_list = []
        anagrams_list = anagram_finder(scrambled_words, words_set, anagrams_list)
        end = time.time()
        total_time = end - start

        anagrams_list.remove(user_word)

        print("The word "+user_word+" has the following "+str(len(anagrams_list))+" anagrams:")
        for word in anagrams_list:
            print(word)
        print("It took "+str(total_time)+" seconds to find the anagrams")
        user_word = input("Enter a word or empty string to finish ")
    else:
        user_word = input("I am sorry, we cannot recognize that word, try again ")
print("Bye, thanks for using this program!")

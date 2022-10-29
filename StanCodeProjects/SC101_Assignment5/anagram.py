"""
File: anagram.py
Name: Karen Chang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """

    ####################
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')

    while True:
        # Ask user input a word
        ana = input('Find anagram for: ')
        start = time.time()

        # The loop will be end if user input 'EXIT'
        if ana == EXIT:
            break

        # Recursively finds all the anagram(s) for the word input by user
        else:
            find_anagrams(ana)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')

    ####################


def read_dictionary():
    """
    The FILE is a data of all the words in a dictionary.
    This function will get the data from FILE and store all the words in FILE as a list.

    :return: list, All words in data FILE which stars from 'a' to 'z'
    """

    # dictionary is a list which the default is without any data in it
    dictionary = []

    # Get data from FILE
    with open(FILE, 'r') as f:
        for words in f:
            dictionary.append(words.strip())
    return dictionary


def find_anagrams(s):
    """
    This function prints all the anagrams of the word user input.
    When the function start to confirm, it will shows "Searching"
    If a anagram be found, it will also be shown to user.
    After confirming all permutations of the word, it will print all the anagrams.

    :param s: str, the word user input
    """
    ans = ''                 # str, The anagram of the word which default is ''
    ans_list = []            # list, The list of all anagrams which default is empty
    dic = read_dictionary()  # list, The list of all the words in a real dictionary

    # start to find the anagrams
    print('Searching...')
    final_ans = find_anagrams_helper(s, ans, ans_list, dic)

    # After finding the anagrams
    print(len(final_ans), 'anagrams for: ', final_ans)


def find_anagrams_helper(s, ans, ans_list, dic):
    """
    This is a helper function for confirming anagrams recursively.

    :param s: str, The word user input for confirming anagrams
    :param ans: str, The permutations of the word for confirming whether it is anagram or not
    :param ans_list: list, The list of all anagrams after confirming
    :param dic: list, The list of words in a dictionary
    :return: ans_list, The final list of all anagrams
    """

    # Base case
    if len(ans) == len(s):
        # If the word in not duplicated and in a dictionary
        if ans not in ans_list and ans in dic:
            print('Founds: ' + ans)
            print('Searching...')
            ans_list.append(ans)
            return ans_list

    # Other case
    else:
        for ch in s:
            # choose
            # add characteristic of 's' which is the word user input one by one
            ans += ch

            # explore
            # if 'ans' is using the same digits as 's' and there is a word which star with 'ans'
            if ans.count(ch) <= s.count(ch) and has_prefix(ans, dic):
                find_anagrams_helper(s, ans, ans_list, dic)

            # un-choose
            ans = ans[:len(ans)-1]

    return ans_list


def has_prefix(sub_s, dic):
    """
    This function confirms whether there is a word in dictionary stars with the given digits

    :param sub_s: str, A string of digits
    :param dic: list, The list of words in a dictionary
    :return: bool, whether there is a word in dictionary stars with the given digits
    """
    for word in dic:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()

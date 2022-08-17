"""
File: anagram.py
Name: Jason Tsai   ( 智翔 )
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

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop


def main():
    """
    TODO:做一個可以數入單字後，將單字重新排列組合，並且呼叫出有意義的單字。
    """
    # 開場白。
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    # 查詢迴圈。
    while True:
        # 輸入欲查詢字串。
        word_input = input('Find anagram for: ')
        # print出等候wording。
        print("Searching ...")
        # 計算時間之起始時間。
        start = time.time()
        # 先行跑字典並暫存。
        word_dictionary = read_dictionary(word_input)
        # 當輸入離開值時執行。
        if word_input == EXIT:
            print("---------- thx :) ---------- ")
            break
        # 輸入單字時執行。
        else:
            # 將最終答案暫存在箱子。
            final_answer = find_anagrams(word_input, word_dictionary)
            # print出有幾種結果和結果內容。
            print(len(final_answer), 'anagrams', final_answer)
            # 計算時間之結束時間。
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary(word_input):
    # 再字典面先行以字母開頭作分類整理，basic_word為輸入值字母lst。
    basic_word = list(word_input)
    # dictionary基礎建設。
    all_words_lst = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [],
                     'l': [], 'm': [], 'n': [], 'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [], 'u': [], 'v': [],
                     'w': [], 'x': [], 'y': [], 'z': []}
    # 以26個字母為基礎開始整理字典。
    for i in range(len(basic_word)):
        # 讀檔。
        with open(FILE, 'r') as f:
            for line in f:
                # 當字串開頭(line.split()[0][0])為該迴圈之字母(basic_word[i])、且字串不等於輸入值長度時執行。
                if line.split()[0][0] == basic_word[i] and len(line.split()[0]) == len(word_input):
                    # 當該單字不在字典內時執行(避免重複單字判斷重複拉取單字)。
                    # if line.split() not in all_words_lst[basic_word[i]]:   >>>>但是針對單字不重複時會增加判斷時間。
                    # 將該單字存入dictionary。
                    all_words_lst[basic_word[i]] += line.split()
    return all_words_lst


def find_anagrams(s, word_dictionary):
    """
    :param word_dictionary:帶入字典。
    :param s:輸入的字串。
    :return:最終搜尋的結果。
    """
    # 定義最終結果的初始值。
    final_answer = []
    # 呼叫 helper function。
    find_anagrams_helper(s, '', final_answer, word_dictionary)
    # 回傳最終解答。
    return final_answer


def find_anagrams_helper(s, word_lst, final_answer, word_dictionary):
    # 當代入字串等於 0 時執行(base case)。
    if len(s) == 0:
        # 當儲存字串存在字典中的key值為字串字首的lst，且該字串不存在final_answer的lst裡時執行。
        if word_lst in word_dictionary[word_lst[0]] and word_lst not in final_answer:
            # print 出「找到XXX字，並繼續搜尋」wording。
            print("Found:  ", word_lst, '\nSearching ...')
            # 在最終結果字串裡面增加找到的結果。
            final_answer.append(word_lst)
    # 當代入字串不等於 0 時執行。
    else:
        # 執行迴圈，迴圈次數同等於字串長度。
        for i in range(len(s)):
            # 當暫存字串是空值時執行。
            if word_lst == '':
                # 帶入helper function 迴圈。
                find_anagrams_helper(s[:i] + s[i + 1:], word_lst + s[i], final_answer, word_dictionary)
                # 移除最後一個字母。
                word_lst = word_lst[:-1]
            # 當帶入prefix function的布林值為 True 時執行。
            elif has_prefix(word_lst, word_dictionary[word_lst[0]]) is True:
                # 暫存字串增加字串裡的第i個字。
                word_lst += s[i]
                # 帶入helper function 迴圈。
                find_anagrams_helper(s[:i] + s[i + 1:], word_lst, final_answer, word_dictionary)
                # 移除最後一個字母。
                word_lst = word_lst[:-1]


def has_prefix(word_lst, word_dictionary):
    """
    :param word_lst: 輸入單字的字段。
    :param word_dictionary: 限縮後的字典。
    :return: 判斷字串的片段是否能在字典清單裡找到，如果有就回傳 True ，反之。
    """
    for word in word_dictionary:            # 若該單字在字典時執行。
        if word.startswith(word_lst):       # 字段符合該單字
            return True                     # 回傳True。
    return False                            # 其餘回傳False。


if __name__ == '__main__':
    main()

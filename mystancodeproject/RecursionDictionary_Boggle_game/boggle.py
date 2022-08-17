"""
File: boggle.py
Name:蔡智翔。
----------------------------------------
TODO:完成boggle game
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    # 四次輸入的暫存箱子列為 list。
    row_lst = ['row_1', 'row_2', 'row_3', 'row_4']
    # 主要執行四次。
    for i in range(4):
        # print出請輸入字母的wording。
        row_lst[i] = input(str(i + 1) + ' row of letter: ')
        # 限制字母之間需要空白鍵的項目。
        row_limit_space = list(row_lst[i])[1] or list(row_lst[i])[3] or list(row_lst[i])[5] or list(row_lst[i])[7]
        # 限制輸入必須是字母的項目。
        row_limit_letter = list(row_lst[i])[0] or list(row_lst[i])[2] or list(row_lst[i])[4] or list(row_lst[i])[6]
        # 當「輸入不等於8個字元」或是「字母間沒有空白格」或是「輸入的不是英文字母」時執行。
        # 我的輸入設定一定要「一個英文字搭配一個空格，所以總共會有8個字元」。
        if len(row_lst[i]) != 8 or row_limit_space != ' ' or row_limit_letter.isalpha() is False:
            # 印出不符合輸入要求的wording。
            print('Illegal input !! Please input four letters and set a space after the letter :( ')
            # 終止程式。
            return
    # 把全部輸入文字整合成一個list。
    row_word = list((row_lst[0] + row_lst[1] + row_lst[2] + row_lst[3]).split())
    # 打造二維矩陣。
    board = [row_word[0:4], row_word[4:8], row_word[8:12], row_word[12:16]]
    # 開始計時。
    start = time.time()
    # 讀字典。
    word_dictionary = read_dictionary(row_word)
    # 帶入recursion。
    final_ans = boggle_game(board, word_dictionary)
    # print出執行結果。
    print('There are ', len(final_ans), ' words in total ~')
    # 結束計時。
    end = time.time()
    print('----------------------------------')
    # 印出結果。
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary(word_input_lst):
    # 製作一份沒有input_letter的原始清單
    letter_without_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't', 'u', 'v', 'w', 'x', 'y', 'z']
    # 將有在input_list裡的字母清除，得到一個完全沒有出現在input_list的清單。
    for letter in word_input_lst:
        if letter in letter_without_lst:
            letter_without_lst.remove(letter)
    # 存放新字典的初始化箱子。
    new_words = []
    # 暴力讀檔案。
    with open(FILE, 'r') as f:
        words = f.read().split()
    # 在暴力讀檔完後的字典清單裡，逐字判斷。
    for word in words:
        # 當字首不在input_lst裡，且字長度介於4到16之間時執行。
        if word[0] in word_input_lst and 16 >= len(word) >= 4:
            # 將單字新增到我們的新字典。
            new_words.append(word)
            # 將單字的字母竹字判斷。
            for letter in word:
                # 當有字母是在「完全沒有出現在input_list的清單」的字串裡時執行。
                if letter in letter_without_lst:
                    # 將該單字從字典中移除。
                    new_words.remove(word)
                    # 結束迴圈。
                    break
    # 將最終的新字典回傳為function的值。
    return new_words


def has_prefix(word_save, word_dictionary):
    """
    :param word_save: 輸入單字的字段。
    :param word_dictionary: 限縮後的字典。
    :return: 判斷字串的片段是否能在字典清單裡找到，如果有就回傳 True ，反之。
    """
    for word in word_dictionary:  # 若該單字在字典時執行。
        if word.startswith(word_save):  # 字段符合該單字
            return True  # 回傳True。
    return False  # 其餘回傳False。


def boggle_game(board, word_dictionary):
    # 最終解答存取箱子的初始值。
    final_ans = []
    # 帶入字母並執行搜尋之箱子的初始值。
    word_save = ''
    # 帶入矩陣執行迴圈，也就是針對16個字母逐字執行。
    for i in range(4):
        for j in range(4):
            # choose ---> 先把要帶入的陣列值先存取；執行搜尋之暫存箱子加入字母；並把該欄位換成'-'，避免後續重複執行。
            word_save_box = board[i][j]
            word_save += board[i][j]
            board[i][j] = '-'
            # explore ---> 帶入helper function執行。
            boggle_game_helper(board, i, j, word_save, final_ans, word_dictionary)
            # un-choose ---> 執行搜尋之暫存箱子還原；board的值也還原。
            word_save = ''
            board[i][j] = word_save_box
    # 將最終解答回傳作為function的解答。
    return final_ans


def boggle_game_helper(board, start_row, start_col, word_save, final_ans, word_dictionary):
    # Base Case。
    if word_save in word_dictionary and word_save not in final_ans:
        final_ans.append(word_save)
        print('Found: " ', word_save, ' "')
        recursion_function_without_base_case(board, start_row, start_col, word_save, final_ans, word_dictionary)

    # 當代入的字串可以在字典裡存在時執行。
    elif has_prefix(word_save, word_dictionary) is True:
        recursion_function_without_base_case(board, start_row, start_col, word_save, final_ans, word_dictionary)


def recursion_function_without_base_case(board, start_row, start_col, word_save, final_ans, word_dictionary):
    # 定義8個下一步需要執行的位置，也就是在字母周遭的8個格子。
    next_move = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    # 執行迴圈，一個位置代表需要執行一次，共八次。
    for row, col in next_move:
        # 其中超出範圍的位置不執行。
        if start_row + row in (4, -1) or start_col + col in (4, -1):
            pass
        # 都該位置不超出範圍，且不等於'-'(也就是還有值維字母時)時執行。
        elif board[start_row + row][start_col + col] != '-':
            # choose ---> 先把要帶入的陣列值先存取；執行搜尋之暫存箱子加入字母；並把該欄位換成'-'，避免後續重複執行。
            word_box = board[start_row + row][start_col + col]
            word_save += word_box
            board[start_row + row][start_col + col] = '-'
            # explore ---> 帶入helper function執行。
            boggle_game_helper(board, start_row + row, start_col + col, word_save, final_ans, word_dictionary)
            # Un-choose ---> 執行搜尋之暫存箱子還原；board的值也還原。
            word_save = word_save[:-1]
            board[start_row + row][start_col + col] = word_box

if __name__ == '__main__':
    main()

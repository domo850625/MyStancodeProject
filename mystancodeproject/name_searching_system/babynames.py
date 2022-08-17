"""
File: babynames.py
Name: 
--------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any value.
    """

    if name in name_data:                                           # 當 name 存在 name_data 裡時觸發。
        if year in name_data[name]:                                 # 當 year 已經在 name 裡重複時觸發。
            if int(name_data[name][year]) >= int(rank):             # 該排名較低 (rank 較大) 時觸發。
                name_data[name][year] = rank                        # 取代原先的 rank。
        else:                                                       # 當 year 不在 name 裡時觸發。
            name_data[name].setdefault(year, rank)                  # 在該 name 下新增新的「年度」與「排名」。
    else:                                                           # 當 name 不存在 name_data 裡時觸發。
        name_data[name] = {year: rank}                              # 新增新的name dict


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.
    """
    with open(filename, 'r') as f:                                                      # 開啟檔案。
        for line in f:                                                                  # 進入迴圈(執行次數 == 行數)。
            baby_info = line.split(",")                                                 # 將該行文字以","分開。
            if len(baby_info) == 1:                                                     # 當字串數量等於1時執行。
                year = baby_info[0].strip()                                             # 代表為年分，取第一個字串。
            else:                                                                       # 當字串數量大於1時執行。
                baby_name_rank = baby_info[0].strip()                                   # 將第一個字串列為 rank。
                baby_name_boy = baby_info[1].strip()                                    # 將第二個字串列為男孩name。
                baby_name_girl = baby_info[2].strip()                                   # 將第三個字串列為女孩name。

                add_data_for_name(name_data, year, baby_name_rank, baby_name_boy)       # 帶入function判斷是否加入男孩dict。
                add_data_for_name(name_data, year, baby_name_rank, baby_name_girl)      # 帶入function判斷是否加入女孩dict。


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}                                          # 設立 name_data dict的初始值。
    for filename in filenames:                              # 執行迴圈(執行次數 == 字串數)。
        add_file(name_data, filename)                       # 將每比資料帶入function執行。
    return name_data                                        # 回傳name_data 作為 function結論值。


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string
    """
    baby_name_lst = list(name_data.keys())                      # 因為 dict 無順序可言，先將所有key值提列成list。
    baby_target_lst = []                                        # 裝載「name搜尋結果」的初始定義。
    for i in range(len(baby_name_lst)):                         # 執行迴圈(執行次數 == list字串個數)。
        name_box = baby_name_lst[i]                             # 先將每輪裡的字串放進箱子存取。
        if name_box.lower().find(target.lower()) != -1:         # 將字元、target做「小寫處理」，並當再字串裡找到target時執行。
            baby_target_lst.append(baby_name_lst[i])            # 將符合條件的字串丟入我們的baby_target_lst。
    return baby_target_lst                                      # 將baby_target_lst回傳為function執行結果。


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()

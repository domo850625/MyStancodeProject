"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names' + year + '.html'

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        numbers = soup.find('tbody').find_all('td')                 # 提列出重點字段。
        number_lst = []                                             # 重新整理字串所需的空字串。
        males = 0                                                   # 計算males初始值。
        females = 0                                                 # 計算female初始值。
        for i in range(len(numbers) - 2):                           # 執行迴圈，不需要最後兩項備註文字。
            number_lst.append(numbers[i].text.replace(",", ""))     # 清理資料後丟入新字串。
            if (i + 1) % 5 == 3:                                    # 當到male人數時執行。
                males += int(number_lst[i])                         # 累計加總。
            if (i + 1) % 5 == 0:                                    # 當到female人數時執行。
                females += int(number_lst[i])                       # 累計加總。

        print('Male Number  : ' + str(males))                       # print出male結果。
        print('Female Number: ' + str(females))                     # print出female結果。


if __name__ == '__main__':
    main()

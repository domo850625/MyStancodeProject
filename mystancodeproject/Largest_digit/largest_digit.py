"""
File: largest_digit.py
Name: Jason Tsai   ( 智翔 )
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:帶入欲判斷的數值。
	:return :回傳 helper function的結果
	"""
	return find_largest_digit_helper(n, 0)


def find_largest_digit_helper(n, biggest_num):
	if n < 0:														# 矯正器，當輸入數值為負數時啟動。
		n = -n														# 把負數數值矯正成正整數。
	if n == 0:														# 當帶入的數值為 0 時啟動。
		return biggest_num											# 回傳當時的最大數值。
	else:															# 當帶入的數值不為 0 時啟動。
		compare_num = n % 10										# 定義當時迴圈需要拿來與最大數值比較的箱子。
		if compare_num > biggest_num:								# 當該箱子大於原本的最大數值時啟動。
			biggest_num = compare_num								# 最大數值便成該迴圈拿來比較的數值。
		return find_largest_digit_helper(n // 10, biggest_num)		# 將輸入數值去掉個位數，並進入下一階段迴圈去判斷最大數。


if __name__ == '__main__':
	main()

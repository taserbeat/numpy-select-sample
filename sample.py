import numpy as np


# 参考: https://biotech-lab.org/articles/12701
# ただし、上記サイトでは2次元配列の例が間違っている

array = np.array([[1, 10, 100], [2, 4, 6], [3, 6, 9], [4, 8, 12]])
print("array:")
print(array)
print()

# 0列目が偶数である行を抽出する
print("The rows where the col-0 is even number.")
bool_idx = np.where(array.T % 2 == 0, True, False)[0]
print(array[bool_idx])
print()

# 1列目が5以上である行を抽出する
print("The rows where the col-1 is 5 or more.")
bool_idx = np.where(array.T >= 5, True, False)[1]
print(array[bool_idx])
print()

# 2列目が10以上である行を抽出する
print("The rows where the col-2 is 10 or more.")
bool_idx = np.where(array.T >= 10, True, False)[2]
print(array[bool_idx])
print()

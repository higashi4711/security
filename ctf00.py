# coding: utf-8
# CTF問題  83 69 67 67 79 78

### 1 ###
print '解法1'
# リストに入れる
a = [83, 69, 67, 67, 79, 78]

# リスト関数mapで各要素をアスキーコードから文字へ変換
b = map(chr, a)
print b

# 連結
print ''.join(b)



### 2 ###
print '解法2'
# リストに入れる
c = '83 69 67 67 79 78'.split()
print c

# 文字列を数値に変換
d = map(int, c)
print d

# アスキーコードから文字列に変換し、連結
print ''.join(map(chr,d))


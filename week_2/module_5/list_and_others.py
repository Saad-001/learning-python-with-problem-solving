fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

apl = fruits.count('apple')
print("apple count : ", apl)

cnt = fruits.count('tangerine')
print("tang count : ", cnt)

idx = fruits.index('banana')
print("idx", idx)

# Find next banana starting a position 4
next_banana_idx = fruits.index('banana', 4)
print("next banana idx : ", next_banana_idx)

fruits.reverse()
print("after reversing fruits list : ", fruits)

fruits.append('grape')
print("after grape append fruits is", fruits)

fruits.insert(2, "lichi")
print("after inserting : ", fruits)

fruits.sort()
print("sorted fruits : ", fruits)

poped = fruits.pop()
print("agter a pop : ", poped)

"""
Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list

Sample Input:
list1 = ["M", "na", "i", "Bo"]
list2 = ["y", "me", "s", "nd"]

Sample Output:
['My', 'name', 'is', 'Bond']

"""
list1 = ["M", "na", "i", "Bo", "I'", "a"]
list2 = ["y", "me", "s", "nd", "m", "", "student", "."]

list3 = []

long_len = len(list1) if len(list1) > len(list2) else len(list2)

def index_in_list(a_list, index):
    return (index < len(a_list))

for i in range(long_len) : 
    if index_in_list(list1, i) and index_in_list(list2, i):
        temp = list1[i] + list2[i]
        list3.append(temp)
    elif index_in_list(list1, i) :
        list3.append(list1[i])
    elif index_in_list(list2, i) :
        list3.append(list2[i])

print(list3)



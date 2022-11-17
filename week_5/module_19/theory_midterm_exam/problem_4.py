"""
4.  Write a program to find anagrams in a given list of words. Two words are called anagrams if one word can be formed by rearranging letters of another. For example ‘eat’, ‘ate’ and ‘tea’ are anagrams.
>>> anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node']) 
[['eat', 'ate', 'tea], ['done', 'node'], ['soup']]

"""
def sort_word (str_1) :
    return str(sorted(str_1))


def anagrams (words_list) :
    anagrams_dict = {}

    for word in words_list :
        sorted_word = sort_word(word)

        if sorted_word not in anagrams_dict :
            anagrams_dict[sorted_word] = [word]
        else :
            anagrams_dict[sorted_word].append(word)

    return list(anagrams_dict.values())

result = anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
print(result)


class Find_pair :

    def pair_matched_target (self, given_list, target) :
        for i, num in enumerate(given_list) :
            if i+1 < len(given_list) :
                if (given_list[i] + given_list[i+1]) == target :
                    return i+1, i+2

pair_1 = Find_pair()

numbers= [10, 20, 10, 40, 50, 60, 70]
target = 50

result = pair_1.pair_matched_target(numbers, target)

print(result)

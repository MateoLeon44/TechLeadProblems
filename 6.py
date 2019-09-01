def two_sum(list, k):
    hash = {}
    for i in list:
        complement = k -i
        hash[complement] = i
    for i in list:
        if i in hash.keys():
            return True
    return False
  # Fill this in.

print(two_sum([4,7,1,-3,2], 5))
# True
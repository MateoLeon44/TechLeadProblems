class Solution:
    def singleNumber(self,nums):
        res = 0
        for num in nums:
            res ^= num # res = res^num
            print(res)
        return res
    def singleNumberMySolution(self, nums):
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
        for key,val in dict.items():
            if(val == 1):
                return key

#print(Solution().singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1
print(Solution().singleNumberMySolution([4, 3, 2, 4, 1, 3, 2]))
'''
0100
0011
    =>  0111
        0010
            =>0101
              0100 
                  =>0001 
                    0001
                        =>0000
                          0011
                              =>0011
                                0010
=>0001
=1
'''
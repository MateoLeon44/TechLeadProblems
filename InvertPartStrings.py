#Input: "The cat in the hat"
#Output: "ehT tac ni eht tah"

class Solution:
    def reverseWords(self, str):
        # Fill this in.
        stack = []
        solution = ""
        for x in str:
            if(x == " " or x == "." or x == str[-1]):
                while len(stack) != 0:
                    print(stack)
                    m = stack.pop()
                    solution += m
                solution += x
            else:
                stack.append(x)
        return solution
            
    


print(Solution().reverseWords("The cat in the hat"))
# ehT tac ni eht tah
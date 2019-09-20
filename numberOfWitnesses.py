def witnesses(heights):
    
    max = heights[len(heights)-1]
    counter = 1
    b = []
    b.append(heights[len(heights)-1])
    for i in range(len(heights)-2, -1,-1):
        print("i: " + str(heights[i]) + ", i+1: " + str(heights[i+1]))
        if heights[i]>heights[i+1]:
            if heights[i] > max:
                max = heights[i]
                counter += 1
                b.append(heights[i])
    print(b)
    return counter
       
    
print(witnesses([6,5,4,3,2,1,3,1,4,1]))
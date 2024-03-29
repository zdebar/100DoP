#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# House Robber Problem  in Python
houses = [6,7,1,30,8,2,4]
count = 0
memory = [0,0,0,0,0,4,4]
print(memory)

def houseRobber(houses, currentIndex):
    global count
    count += 1
    global memory
    if currentIndex >= len(houses)-2:
        return memory
    else:
        stealFirstHouse = houses[currentIndex] + (houseRobber(houses, currentIndex + 2))[currentIndex+2]
        skipFirstHouse = (houseRobber(houses, currentIndex+1))[currentIndex+1]
        memory[currentIndex] = max(stealFirstHouse, skipFirstHouse)
        return memory


print(houseRobber(houses, 0))
print(count)
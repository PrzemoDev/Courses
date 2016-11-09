#-------------------------------------------------------------------------------
# Name:        Functional Programming - Module Quiz 6 - SoloLearn
# Purpose:     Study
#
# Created:     05-11-2016
# Copyright:   (c) PrzemoDev
#-------------------------------------------------------------------------------
nums = {1,2,3,4,5,6}
nums = {0,1,2,3} & nums  # & intersection gets items only in both sets
nums = list(filter(lambda x:x>1, nums)) # "filter" removes unmatched itemst

print(len(nums))

def power(x,y):
    if y == 0:
        return(1)
    else:
        return(x * power(x,y-1))  # 2*2 (y=2) => 2*4 (y=1)
print(power(2,3))

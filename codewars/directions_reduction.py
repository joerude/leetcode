# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python
import codewars_test as test

def dirReduc(arr):
    d = {'NORTH':'SOUTH', 'SOUTH':'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}
    i = 0
    
    if (len(arr) == 2 and arr[0] == d[arr[1]]) or len(arr) == 0: 
        return []
    
    while True:
        if i + 1 == len(arr):
            return arr
        
        if d[arr[i]] == arr[i + 1]:
            del arr[i:i+2]
            i = 0
        else:
            i += 1
            


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
test.assert_equals(dirReduc(a), ['WEST'])
u=["NORTH", "WEST", "SOUTH", "EAST"]
test.assert_equals(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])
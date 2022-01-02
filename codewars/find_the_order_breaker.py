# https://www.codewars.com/kata/5fc2a4b9bb2de30012c49609

# Find the Order Breaker

def order_breaker(array):
    lst = []
    for i, v in enumerate(array):
        if i + 1 == len(array):
            break
        if i == 0:
            if v > array[i + 1]:
#                 print(v)
#                 break
                  return v
            else: continue
        if (v > array[i - 1] and v > array[i + 1]) or (v < array[i - 1] and v < array[i + 1]):
            # print(v)
            lst.append(v)
    
    for i in lst:
        new = array[:]
        new.remove(i)
        if new == sorted(new):
            return i
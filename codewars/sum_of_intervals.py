def sum_of_intervals(inter):
    int_sum =  lambda x: x[1] - x[0]
    
    print('lst', inter)
    
    if len(inter) == 1:
        return inter[0][1] - inter[0][0]
        
    yes, no = [], []
    pivot = inter[0]

    for i in inter:
        if i[0] <= pivot[0] and i[1] <= pivot[1]:
            pivot = i
    
    print('pivot', pivot)
    print()
    

    for i in inter:
        if i[0] > pivot[0] and i[1] > pivot[1] and pivot[1] > i[0]:
            no.append([pivot[0], i[1]])
            
        elif i[0] > pivot[1]:
            yes.extend([pivot, i])
            
        # print(inter)
    
    
    print('no', no)
    print('yes', yes)
    
    
    total = map(lambda x: x[1] - x[0], yes + no)
    
    print(sum(list(total)))
    
    return sum(list(total))
    

# sum_of_intervals([[1, 5]]) ok

# sum_of_intervals([[1, 5], [6, 10]]) ok +-

sum_of_intervals([[1,4],[7, 10],[3, 5]])  # --> 7

# sum_of_intervals( [[1,2],[6, 10],   [11, 15]] );
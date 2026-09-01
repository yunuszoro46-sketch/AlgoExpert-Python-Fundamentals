lst = [-2, 0, 4, 5, 1, 2]



for idx in range(len(lst)-1):
    current_items=lst[idx]
    next_items=lst[idx+1]

    sum_of_items=current_items+next_items
    print(sum_of_items)


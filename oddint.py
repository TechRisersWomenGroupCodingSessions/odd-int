def get_odd_int(num_list): # [1,2,2]
    for i in num_list:
        if not isinstance(i, int):
            return 'Not valid input'
        
        if num_list.count(i) % 2 == 1:
            return i

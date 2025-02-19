def isOdd(num_list): # [1,2,2]
    dist_vals=list(set(num_list)) # [1,2]
    dict_vals_count = {key: 0 for key in dist_vals}
    print(f"Default value of dict: {dict_vals_count}")
    for i in dist_vals:
        # print(f"Loop of i: {i}")
        for j in num_list:
            # print(f"Loop of j: {j}")
            if i == j:
                dict_vals_count[i] += 1;
    print(f"value of dict after loop {dict_vals_count}")
  
    for key, value in dict_vals_count.items():
        if value % 2 == 1:
          return key
    


    

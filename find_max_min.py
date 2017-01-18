def find_min_max(num_list):
    
    # setting varibales 
    seen = set()
    num_list.sort()
    sorted_output = []
    output = []
    
    #iteration through sorted list
    for n in num_list:
        if n not in seen:
            seen.add(n)
            sorted_output.append(n)
        else:
            pass
    
    # adding min and max to output list
    sort_len = len(sorted_output)
    if sort_len > 1:
        output.append(sorted_output[0])
        output.append(sorted_output[sort_len - 1])
    else:
        # if values are same return length or original input
        output.append(len(num_list))
    
    return output

if __name__ == '__main__':
    print(find_min_max([4, 66, 6, 44, 7, 78, 8, 68, 2]))
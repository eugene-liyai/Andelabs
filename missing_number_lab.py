def find_missing(arr1, arr2):

    # sorting the input file to make itteration easier
    arr1.sort()
    arr2.sort()

    # handling empty list
    if arr1 == [] and arr2 == []:
        return 0

    # iterating through the set of list passed
    if len(arr1) > len(arr2):
        for num1, num2 in zip(arr1, arr2):
            if num1 != num2:
                return num1
        return arr1[-1]
    elif len(arr1) == len(arr2):
        for i, j in zip(arr1, arr2):
            if i != j:
                return i
            else:
                return 0
    else:
        for num1, num2 in zip(arr2, arr1):
            if num1 != num2:
                return num1
        return arr2[-1]
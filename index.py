def binary_search(input_array, value):
    pointer = len(input_array) / 2 
    indexerhigh = 0 
    for x in range(len(input_array)):
        if input_array[pointer] == value :
            return pointer
        elif input_array[pointer] < value :
            indexerhigh = pointer
            pointer = (pointer + len(input_array)) / 2
        elif input_array[pointer] > value:
            if pointer == len(input_array) - 1 :
                return -1 
            elif pointer - indexerhigh == abs(1):
                return - 1 
            else:
                pointer = (indexerhigh + pointer)/ 2
                
test_list = [1,3,9,11,15,19,29,38,41,52,90]
test_val1 = 25
test_val2 = 15
test_val3 = 3
test_val4 = 90
test_val5 = 52
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
print binary_search(test_list, test_val3)
print binary_search(test_list, test_val4)
print binary_search(test_list, test_val5)

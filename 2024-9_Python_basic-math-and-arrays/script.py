mas = [86, 101, 110, 116, 44, 55, 66, 22]

def average(array):
    total = 0
    for i in array:
        total = total + i
    return total / len(array)

def median(array):
    sorted_array = sorted(array)
    
    if(len(sorted_array) % 2 == 0):
        #even
        middle_element1 = sorted_array[int((len(sorted_array) / 2) - 1)]
        middle_element2 = sorted_array[int(len(sorted_array) / 2)]

        answer = (middle_element1 + middle_element2) / 2
    else:
        #odd
        answer = sorted_array[int(len(sorted_array) / 2)]

    return answer

def find_in_array(array, input):
    index = 0
    for i in array:
        if(input == i):
            return 'Element Found In Index: ' + str(index)
        index = index + 1
    return "Element Not Found!"



print("Average: ", average(mas))
print("Median: ", median(mas))
user_input = int(input("Enter an ellement you would like to find: "))
print("Provided Array: ", mas)
print(find_in_array(mas, user_input))

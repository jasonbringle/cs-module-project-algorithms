'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    #This houses the total of all items minus the integer we are currently on
    total = 0
    #This houses each individual total for all the numbers
    final = []
    i = 0
    j = 0
    #Loop through all the numbers
    for i in range(len(arr)):
        #Reset j to 0 so when while loop starts it starts at zero
        j = 0
        #Append any values in total to the final array
        final.append(total)
        #Reset total to 0 so the next set of operations adds to a clean variable
        total = 0
        #For each item while look at the number
        while j in range(len(arr)):
            # and determine if it is greater than 1
            if total >= 1:
                #If the number doesnt equal the for loop iterator
                if j != i :
                    #Add the number in the while loop to the total
                    total *= arr[j]
                    #Increment j to move to the next number
                    j += 1
                else:
                    #Skip the operation if the j = i.  This is how we prevent from including the current number in our operation.
                    j += 1
            #If total is 0 then it is at the start of the operation and needs to add a 1 to begin the operation.
            else:
                total += 1
    #Append the final number
    final.append(total)
    #Pop off the zero at the start which is created on first run on line 17
    final.pop(0)
    #return array
    return final
    


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

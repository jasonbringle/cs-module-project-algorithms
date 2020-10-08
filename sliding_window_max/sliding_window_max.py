'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    #Array to put numbers in
    arrK = []
    maxNums = []
    i = 0
    j = 0
    #For each number in range of the array - k +1 (this prevents looping with non-existant indexes)
    for i in range(len(nums)-k+1):#O(N)
        #Use an iterator in range of k
        while j in range(k):#O(k*N)
            #Append the number to the array by using the for and while loop iterators.
            arrK.append(nums[i+j])#O(C)
            #increment the j variable to move to the next number in the array
            j += 1#O(C)
            #Check if the length of the array is as big as the window (k)
            if len(arrK) == k:#O(C)
                #apped the maximum number in the temporary array to the maxNums array
                maxNums.append(max(arrK)) #O(C) 
                #reset the temporary array
                arrK = []#O(C)
                #reset j to zero so when it starts incrementing again it will use i in the for loop as a reference
                j = 0 #O(C)
                #Break out from while loop to return to for loop and get the next set of k numbers
                break
    
        #Not my solution
    # maxNums = [max(nums[i:i+k]) for i in range(len(nums)-k+1)]

    return maxNums


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

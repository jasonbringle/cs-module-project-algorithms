'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # # Your code here
    # #Array to put numbers in
    # arrK = []
    # maxNums = []
    # i = 0
    # j = 0
    # #For each number in range of the array - k +1 (this prevents looping with non-existant indexes)
    # for i in range(len(nums)-k+1):#O(N)
    #     #Use an iterator in range of 
    #     while j in range(k):#O(k*N)
    #         arrK.append(nums[i+j])#O(C)
    #         j += 1#O(C)
    #         if len(arrK) == k:#O(C)
    #             maxNums.append(max(arrK)) #O(C) 
    #             arrK = []#O(C)
    #             j = 0 #O(C)
    #             break
        
    maxNums = [max(nums[i:i+k]) for i in range(len(nums)-k+1)]

    return maxNums


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

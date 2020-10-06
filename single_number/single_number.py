'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    #sort the array
    arr.sort()
    #Since the array is sorted then any pairs will be next to each other... we iterate over the pairs. (2)
    for i in range(0,len(arr),2):
        #If the pairs are equal we pass by them
        if arr[i] == arr[i+1]:
            pass
        #If they are not then we return the integer in the array
        else:
            return arr[i]
"""
***THIS IS NOT MY SOLUTION**********
def single_number(arr):
    # Your code here
    list_of_nums = {}
    for i in range(len(arr)):
        if arr[i] in list_of_nums:
            list_of_nums[arr[i]] += 1
        else: 
            list_of_nums[arr[i]] = 1
    for entry in list_of_nums:
        if list_of_nums[entry] == 1:
            return entry
"""


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    #Checking for base case at the outset. This says there is one possible way to eat 0 cookies. 0
    if n == 0:
        return 1
    #This says there is one way to eat one cookie
    if n == 1:
        return 1
    #This says there are 2 ways to eat 2 cookies
    if n == 2:
        return 2
    
    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    
    


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 3

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

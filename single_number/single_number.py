'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Create an empty list to store unique elements
    dupeList = []
    
    # Iterate over the original list and for each element
    # add it to dupeList, if its not already there.
    for i in arr:
        if i in dupeList:
            dupeList.remove(i)

        else:
            dupeList.append(i)
    # Return the list of unique elements        
    return dupeList[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
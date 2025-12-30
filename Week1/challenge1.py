# ***** Team Contribution Multiplier ******

def ProductOfArrayExceptSelf(array: list[int]):
    """ function that takes an integer array contributions and returns an integer array impact, 
    where each element represents the product of all elements except itself. """
    n = len(array)
    impact = [1] * n
    #  looping left to right
    left_result = 1
    for i in range(n):
        impact[i] *= left_result
        left_result *= array[i]  
    #  looping right to left
    right_result = 1
    for i in range(n-1, -1 , -1): 
        impact[i] *= right_result
        right_result *= array[i]

    return impact

contributions = [1, 2, 3, 4]
# contributions = [-1, 1, 0, -3, 3]
# contributions = [5, 6, 7, 1]
print(ProductOfArrayExceptSelf(contributions))
# Output1: impact = [24, 12, 8, 6]
# Output2: impact = [0, 0, 9, 0, 0]
# Output3: impact = [42, 35, 30, 0]

    
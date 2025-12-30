# ***** Balanced Performance Score *****

def BalancedPerformanceScore(array1: list[int], array2: list[int]):
    """ a function that takes two sorted integer arrays scoresA and scoresB 
    and returns the median value as a floating-point number."""
    if len(array1) > len(array2): # setting short length = array1  
        array1, array2 = array2, array1

    n, m = len(array1), len(array2)  # lengths for arrays 
    low, high = 0, n  # array1

    while low <= high:
        midA = (low + high) // 2  # partition index in array1 (shorter one)
        midB = ((n + m + 1) // 2 ) - midA  # partition index in array2 as left side has half of total elements
        #  setting left and right of partion in array1 
        leftA  = array1[midA - 1] if midA > 0 else float('-inf')
        rightA = array1[midA]     if midA < n else float('inf')
        #  setting left and right of partion in array2
        leftB  = array2[midB - 1] if midB > 0 else float('-inf')
        rightB = array2[midB]     if midB < m else float('inf')

        # Correct partition found
        if leftA <= rightB and leftB <= rightA:
            if (n + m) % 2 == 0: # if middle values are even
                return (max(leftA, leftB) + min(rightA, rightB)) / 2
            else: # if middle value is odd
                return max(leftA, leftB)

        # Move partition
        elif leftA > rightB: # If leftA is too big, move partition in array1 to the left
            high = midA - 1
        else: # If leftB is too big, move partition in array1 to the right
            low = midA + 1
    


scoresA = [1, 3]
scoresB = [2]
# ------------------
# scoresA = [1, 2]
# scoresB = [3, 4]
print(BalancedPerformanceScore(scoresA, scoresB))
# Output1: 2.0
# Output2: 2.5

    
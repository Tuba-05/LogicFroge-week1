# # # *Challenge 3: Balanced Performance Score*

# ---

# Two student teams worked on the **same coding lab**, but their scores were recorded **separately** and are already **sorted**.

# You are given:

# - `scoresA` → sorted scores of Team A
# - `scoresB` → sorted scores of Team B

# Your task is to find the **median score** after considering **both teams together**.

# ⚠️ You are **not allowed to fully merge** the two lists.

# ---

# ### 🧩 Problem Statement/ Function Requirement

# > Write a function that takes two sorted integer arrays scoresA and scoresB and returns the median value as a floating-point number.
# > 

# The solution must run in:

# > O(m + n) time
# > 

# ---

# - Examples
    
#     **Example 1**
    
#     ```
#     Input:  scoresA = [1, 3], scoresB = [2]
#     Output: 2.0
    
#     ```
    
#     **Example 2**
    
#     ```
#     Input:  scoresA = [1, 2], scoresB = [3, 4]
#     Output: 2.5
#     Explanation 
#     ```
    
#     ---
    
#     - If the total number of elements is **odd**, the median is the **middle value**
#     - If **even**, the median is the **average of the two middle values**

# ---

# - Constraints
    
#     `0 ≤ m, n ≤ 1000` 
    
#     `1 ≤ m + n ≤ 2000` 
    
#     Arrays are already **sorted**
    
#     Values range from `10⁶` to `10⁶`
    

# ---

# - Hint
    
#     Use **two-pointer traversal** approach:
    
#     - Start with one pointer at the beginning of each array
#     - Move the pointer with the smaller current value
#     - Keep a count of how many elements have been seen
#     - Stop when you reach the median position
    
#     You do **not** need to store the merged array. You may simulate merging using indices, but must not create a merged array.
# ------------------------------------------------------------------------------------------------------------------------------
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
scoresA = [1, 2,]
scoresB = [3, 4]
print(BalancedPerformanceScore(scoresA, scoresB))
# Output1: 2.0
# Output2: 2.5

    
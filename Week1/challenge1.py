# # # Challenge 1: *Team Contribution Multiplier*

# You are part of a **software engineering team** working on a **group project**.

# Each team member contributes a **performance score** (could be positive, negative, or zero — just like real life 😄).

# Your task is to **analyze impact**.

# For every team member, calculate the **overall team performance if that member takes a break**.

# ---

# ### 🧩 Problem Statement (Student-Friendly)

# You are given an integer array `contributions`, where:

# - `contributions[i]` represents the **contribution score** of the `i-th` team member.

# Create a new array `impact` such that:

# > impact[i] is the product of all contribution scores except contributions[i].
# > 

# ## Function Signature Requirement

# Write a function that takes an integer array `contributions` and returns an integer array `impact`, where each element represents the product of all elements except itself.

# ---

# - **Rules from the Team Lead**
#     - You are **NOT allowed to use division** ❌
#     - Your solution must run in **linear time** → **O(n)**
#     - Extra space should be minimal
#     - The result always fits within a **32-bit integer**

# ---

# - Examples
    
#     ### Example 1
    
#     ```
#     Input: contributions = [1, 2, 3, 4]
#     Output: impact = [24, 12, 8, 6]
#     ```
    
#     👉 If member `0` steps away, the team impact is `2 × 3 × 4 = 24`
    
#     ---
    
#     ### Example 2
    
#     ```
#     Input: contributions = [-1, 1, 0, -3, 3]
#     Output: impact = [0, 0, 9, 0, 0]
#     ```
    
#     👉 A single `0` contribution affects the whole team — just like missing deadlines 😬
    

# ---

# - Think Like an Engineer
    
#     Instead of recalculating everything again and again:
    
#     - First, compute **everything to the left** of each index
#     - Then, compute **everything to the right**
#     - Multiply both values to get the final impact
    
#     ➡️ This can be done in **two clean passes** over the array.
    

# ---

# - Bonus Challenge (For Curious Minds)
    
#     💡 **Can you solve this using O(1) extra space?**
    
#     > The output array does not count as extra space.
#     >
# -----------------------------------------------------------
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

    
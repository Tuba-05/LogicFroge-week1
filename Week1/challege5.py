# # # Challenge 5: *Fix the Broken Expression*

# ---

# You are given a string `expr` containing:

# - lowercase letters
# - parentheses `'('` and `')'`

# Some parentheses may be **misplaced**.

# A string is valid if every opening `'('` has a matching closing `')'` in the correct order.
# Your task is to remove the **minimum number of parentheses** so that the resulting string is **valid**.

# Return **all unique valid strings** that can be formed with the **minimum removals**.

# You may return the answers in **any order**.

# ## Function Requirement

# > Write a function that takes a string expr and returns a list of all valid strings with minimum removals.
# > 

# ---

# - Examples
    
#     ```
#     Input:  "()())()"
#     Output: ["(())()", "()()()"]
    
#     Input:  "(a)())()"
#     Output: ["(a())()", "(a)()()"]
    
#     ****`Input:  ")("
#     Output: [""]`
    
#     Input:  "()"
#     Output: ["()"]
    
#     Input:  "abc"
#     Output: ["abc"]
    
#     Input:  "((("
#     Output: [""]
#     ```
    

# ---

# - Constraints
#     - `1 ≤ length of expr ≤ 25`
#     - At most **20 parentheses**
#     - Letters must remain unchanged

# ---

# - Hint
    
#     First, count how many `'('` and `')'` must be removed
#     Then try removing parentheses step by step while keeping the string valid, and stop once minimum removals are reached.
#     Avoid duplicate result
    
# ---
# -----------------------------------------------------------
# ***** Fix the Broken Expression *****
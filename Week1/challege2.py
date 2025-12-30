# ****** Password Recovery Window ******

#  LOGIC:-
# 1. Initialize 3 variables: [left, right] pointers for window, [window] to store charecters
# 2. First move right until charecters in window matches to pattern then slightly shrink window by 
#    removing one character at a time from left to check the window still valid if not then widow 
#    starts from right

def function(log, pattern):
    """ function that takes two strings log and pattern and returns the minimum window substring 
    of log. If no valid window exists, return an empty string. """
    if len(log) < len(pattern):
        return f'""'
    left = 0
    right = 0
    # left = log[0]
    # right = log[-1]
    window = ""
    current_ch_count = 0

    while True:
        shrink_window = ""
        # for char in pattern:


        # ------------------------------------------------------ 
        for i in range(left, (len(log)-1)):
            window += log[i]
            print('loop1',window)
            right = i
            if (char for char in pattern) in window:
                break
            else: continue

        for j in range(len(window)):
            print('loop2',window[j::])
            if not pattern in window[j::]:
                right = left
                break
            else:
                if len(window[j::]) >=3 :
                    if window[j+1::] in pattern: continue
                    else:
                        shrink_window = window[j::1]
                
        if shrink_window in pattern:       
            break        
    return shrink_window   

log = "ADOBECODEBANC"
pattern = "ABC"
print(function(log, pattern))

#  **Example 1**
# Input:  log = "ADOBECODEBANC", pattern = "ABC"
# Output: "BANC"

# **Example 2**
# Input:  log = "a", pattern = "a"
# Output: "a"

# **Example 3**
# Input:  log = "a", pattern = "aa"
# Output: ""

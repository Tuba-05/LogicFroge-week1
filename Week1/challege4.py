# # # **Challenge 4 : The Deep Storage Inventory Search**

# You are a Software Engineer at a massive automated warehouse. The warehouse stores crates in a square grid (`n x n`).

# - **The Sorting:** To save time, the warehouse robots always keep crates sorted: they get heavier as you move **Right** and heavier as you move **Down**.
# - **The Mission:** Your manager needs the **$k^{th}$ lightest crate** in the entire warehouse to fulfill a priority order.

# ### **The Technical Hurdle**

# You could pull all the crates out and sort them in a long line, but that takes too much memory (O(n^2)). The warehouse computer is old—it needs a solution with **better memory efficiency**.

# ---

# ### What You Need to Do

# Given an `n x n` matrix where:

# - Each row is sorted in ascending order
# - Each column is sorted in ascending order

# Return the **kᵗʰ smallest element** in the matrix.

# ---

# ### Function Requirement

# > Write a function that takes a 2D integer matrix matrix and an integer k, and returns the kᵗʰ smallest element.
# > 

# ---

# ### **Example Case**

# - **Input:** `matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]], k = 8`
# - **Sorted List view:** `[1, 5, 9, 10, 11, 12, 13, 13, 15]`
# - **8th Smallest:** `13`

# ---

# - **Guide: Two Ways to Solve It**
    
#     ### **Approach A: The "Priority Queue" (The Multi-Line Merge)**
    
#     Think of each row as a sorted line of students. You want to find the kth smallest overall.
    
#     1. Take the first element of every row and put it in a **Min-Heap**.
#     2. Pop the smallest element.
#     3. Replace it with the *next* element from the same row.
#     4. Repeat k times. The kth element you pop is your winner!
#     - **Efficiency:** O(k log n) time and O(n) space.
    
#     ### **Approach B: The "Binary Search" (The Guess & Check)**
    
#     This is the "Boss Level" solution for the follow-up. Instead of searching positions, we search the **Value Range**.
    
#     1. **Low:** The lightest crate (top-left).
#     2. **High:** The heaviest crate (bottom-right).
#     3. **The Guess:** Pick a middle weight (`mid`).
#     4. **The Count:** Use a "Staircase Search" to quickly count how many crates in the warehouse are lighter than `mid`. Because the rows/columns are sorted, you can do this count in O(n) time by starting at the bottom-left and moving up or right!
#     5. **Adjust:** If the count is too low, your `mid` was too small. If too high, your `mid` was too big.
# --------------------------------------------------------------------------------------------------------------
#  ***** The Deep Storage Inventory Search *****


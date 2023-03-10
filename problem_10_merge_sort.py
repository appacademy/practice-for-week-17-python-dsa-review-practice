# Merge Sort

# Recall the merge sort algorithm:

# Find midpoint to divide list in half
# Call merge_sort recursively on the first half
# Call merge_sort recursively on the second half
# Merge the two sorted halves with merge

# Implement the merge_sort function with the merge helper function.

# Your code here

lst = [5, 2, 38, 91, 16, 427]

sorted_lst = merge_sort(lst)        # Out of place solution
print(sorted_lst)

merge_sort(lst)                     # In place solution
print(lst)
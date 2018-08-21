# Given an array of integers (pos and neg), find the largest continuous sum
# Example: [1, 2, -1, 3, 4, 10, 10, -10, -1], would be 29 as 1 + 2 - 1 + 3 + 4  + 10 + 10 is the largest you can get in order 
# Complexity is O(N)

def large_cont_sum(arr):
    if len(arr) == 0:
        return 0
    
    max_num = current_sum = arr[0]
    
    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_num = max(current_sum, max_num)
    print(max_num)
    return max_num


if __name__ == '__main__':
	large_cont_sum([1, 2, -1, 3, 4, 10, 10, -10, -1])
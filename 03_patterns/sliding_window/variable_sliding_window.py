"""
When to use it:Finding the longest subarray with at most $K$ distinct characters.
Finding the shortest subarray with a sum greater than or equal to a target.
"""

def variable_sliding_window(arr, target):
    # 1. Tracker and result structures
    window_tracker = 0

    # Simpler alternative to float('inf'):
    # A valid subarray length can never exceed the length of the array itself.
    min_length = len(arr) + 1

    left = 0

    # 2. Expand the window using the right pointer
    for right in range(len(arr)):
        window_tracker += arr[right]  # Adjust logic based on problem

        # 3. Shrink the window from the left while the condition is violated
        while window_tracker > target:  # Change condition based on problem
            window_tracker -= arr[left]
            left += 1

        # 4. Update your result once the window is valid
        if window_tracker == target:  # Change condition based on problem
            current_window_len = right - left + 1
            min_length = min(min_length, current_window_len)

    # If min_length is still greater than len(arr), no valid window was found
    return min_length if min_length <= len(arr) else 0
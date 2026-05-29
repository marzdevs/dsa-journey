"""
When to use it: Find the maximum/minimum sum of a subarray of size $K$.
Problems like Contains Duplicate II or Number of Sub Arrays of Size K and Avg Greater than or Equal to Threshold.
"""

def fixed_sliding_window(arr, k):
    window_tracker = 0
    max_result = 0  # Initialize to 0 (or a very small integer like -100000 if negative numbers exist)

    left = 0

    for right in range(len(arr)):
        # Add the current element to your tracker
        window_tracker += arr[right]

        # Check if we have hit the exact window size 'k'
        if (right - left + 1) == k:
            # Update your global result
            max_result = max(max_result, window_tracker)

            # Remove the element at the left pointer and slide the window forward
            window_tracker -= arr[left]
            left += 1

    return max_result
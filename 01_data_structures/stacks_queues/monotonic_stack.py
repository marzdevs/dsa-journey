def monotonic_decreasing_stack(nums):
    stack = []

    for num in nums:
        # We need our while loop right here
        while stack and stack[-1] > num:
        stack.append(num)

    return stack
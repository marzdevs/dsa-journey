nums = [1, 2, 3]

# access
print(nums[1]) # 0 1 2 index

# append
nums.append(4) # add 4 to last item 0(1) doesnt require much and is fast

# insert
nums.insert(0, 99)
print(nums) # shifts everything to right to add 99

# delete
nums.pop()
print(nums) # removes last

# traversal
for n in nums:
    print(n) # prints each one seperatly in new line
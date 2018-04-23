userInput = input("Enter a bunch of numbers: \n")

#Split into seperate strings:
tokens = userInput.split()

# Convert Strings to ints and store in nums[] list
nums = []
for token in tokens:
    nums.append(int(token))
    index = nums.index(int(token))
    print('%d: %d' % (index, nums[index]))

# # Print each position and number
# print()
# for index in range(len(nums)):
#     value = nums[index]
#     print('%d: %d' % (index, value))

# Determine max even number
max_num = None
for num in nums:
    if (max_num == None) and (num % 2 == 0):
        # First even num found
        max_num = num
    elif (max_num != None) and (num > max_num) and (num % 2 == 0):
        # Larger even num found
        max_num = num

print('Max even #:', max_num)





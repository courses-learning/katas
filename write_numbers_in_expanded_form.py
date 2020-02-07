"""You will be given a number and you will need to return it as a string in
Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'

NOTE: All numbers will be whole numbers greater than 0."""


def expanded_form(n):
    nums = list(str(n))
    nums.reverse()
    powers = [str(int(nums[i]) * (10 ** i)) for i in range(len(nums))]
    powers.reverse()
    return (" + ".join(num for num in powers if num != '0'))

print(expanded_form(259
))

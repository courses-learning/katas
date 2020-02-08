"""You are given an array strarr of strings and an integer k. Your task is to
return the first longest string consisting of k consecutive strings taken in
the array.

Example:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta",
"abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
"""


def longest_consec(strarr, k):
    long_val = 0
    long_str = ""
    for i in range(len(strarr) - k + 1):
        word = "".join(strarr[i:(i + k)])
        length = len(word)

        if length > long_val and k > 0:
            long_val = length
            long_str = word
    return long_str

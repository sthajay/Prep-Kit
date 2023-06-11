# Encode and Decode Strings
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        decoded_string = ''
        for el in strs:
            decoded_string += str(len(el)) + '#' + el
        return decoded_string
    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """

    def decode(self, str):
        res, i = [], 0
        while i < len(str):
            j = i
            while str[j] != '#':
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1:j + 1 + length])
            i = j + 1 + length
        return res


# Time Complexity = O(n)
str = Solution.encode(['lint', 'code', 'love', 'you'])
ans = Solution.decode(str)
print(ans)

# Other Solution => Brute Solution (Using Dictionary/ Object to store the value)
# obj = {}
# # strs = ['lint', 'code', 'love', 'you']
# strs = ["we", "say", ":", "yes"]
# count = 1
# # Encoding
# for el in strs:
#     obj[count] = len(el)
#     count += 1

# encoded_string = ''.join(strs)
# print(encoded_string)

# prev_length =0
# #Decoding
# decoded_string=[]
# for k,v in obj.items():
#     decoded_string.append(encoded_string[prev_length: v + prev_length])
#     prev_length = v + prev_length
# print(decoded_string)

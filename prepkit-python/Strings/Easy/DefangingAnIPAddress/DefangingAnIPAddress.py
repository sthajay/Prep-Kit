# 1108. Defanging an IP Address

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
    # Other solution
        # return ('[.]').join(address.split('.'))
        # return ('').join(['[.]' if el == '.' else el for el in address])


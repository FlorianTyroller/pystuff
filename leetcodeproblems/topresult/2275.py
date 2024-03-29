class Solution:
    """
    def custom_base_to_int(self,s, base):
        result = 0
        multiplier = 1
        for char in reversed(s):
            digit = ord(char) - ord('0') if char.isdigit() else ord(char) - ord('a') + 10
            result += digit * multiplier
            multiplier *= base
        return result

    def largestCombination(self, candidates: list[int]) -> int:
        z_l = []
        s = 0
        ba = len(candidates) + 1
        if ba > 36:
            for j in candidates:
                z_c = 0
                n = self.custom_base_to_int(bin(j)[2::], ba)
                s+=n
            hr = 0
            while s > 0:
                s, remainder = divmod(s, ba)
                if remainder > hr:
                    hr = remainder
            return hr
        for j in candidates:
            z_c = 0
            n = int(bin(j)[2::], ba)
            s+=n
        hr = 0
        while s > 0:
            s, remainder = divmod(s, ba)
            if remainder > hr:
                hr = remainder
        return hr

    """

    def largestCombination(self, candidates: list[int]) -> int:
        l = [0]*25
        s = 2**24
        for j,s in enumerate([2**i for i in range(24,-1,-1)]):
            for i,n in enumerate(candidates):
                if n >= s:
                    l[j] += 1
                    candidates[i] -= s
        return max(l)

if __name__ == "__main__":
    s = Solution()
    print(s.largestCombination([1,2,3,4,5])) #3
    print(s.largestCombination([16,17,71,62,12,24,14])) #4
    print(s.largestCombination([8,8])) #2
    a = [39,79,15,70,18,8,67,34,71,80,90,22,27,41,95,15,42,70,43,92,77,13,44,71,79,33,46,62,20,81,94,56,79,53,29,71]
    print(s.largestCombination(a)) #23
    
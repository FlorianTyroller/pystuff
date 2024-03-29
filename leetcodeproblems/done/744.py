class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        mind = 99
        minl = ""
        t = ord(target)

        for l in letters:
            dif = ord(l) - t
            if dif > 0 and dif < mind:
                mind = dif
                minl = l
        if minl:
            return minl
        return letters[0]

if __name__ == "__main__":
    s = Solution()
    print(s.nextGreatestLetter(["c", "f", "j"], "c"))
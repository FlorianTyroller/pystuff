class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        pixelc = 0
        linec = 0

        for l in s:
            w = widths[ord(l)-97]
            if pixelc + w > 100:
                pixelc = w
                linec += 1
            else:
                pixelc += w
        
        return [linec + 1, pixelc]


if __name__ == "__main__":
    s = Solution()
    print(s.numberOfLines(2, 2))
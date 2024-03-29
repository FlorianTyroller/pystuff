class Solution:
    def repeatedCharacter(self, s: str) -> str:
        r = ""
        for c in s:
            if c in ls:
                return c
            else:
              r += c  
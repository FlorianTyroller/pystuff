class Solution:
    def kthPalindrome(self, queries: list[int], intLength: int) -> list[int]:
        
        start = 10**((intLength+1)//2-1)
        even = True if intLength % 2 == 0 else False
        ans = []
        for q in queries:
            s = start + (q-1)
            s = str(s)
            if len(s) > len(str(start)):
                ans.append(-1)
                continue
            if even:
                s = s + s[::-1]
            else:
                s = s + s[::-1][1:]
            ans.append(int(s))
        return ans

if __name__ == "__main__":
    s = Solution()


    print(s.kthPalindrome([1,2,3,4,5,90], 3))
    print(s.kthPalindrome([2,4,6], 4))
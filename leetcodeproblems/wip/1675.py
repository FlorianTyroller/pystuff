"""
You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

If the element is even, divide it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
If the element is odd, multiply it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.

"""

class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:
        ex_num = []
        e_num = []
        all_nums = set()
        for i,n in enumerate(nums):
            ex_num.append(set())
            e_num.append(set())
            while self.is_even(n):
                ex_num[i].add(n)
                e_num[i].add(n)
                all_nums.add(n)
                n //= 2
            ex_num[i].add(n)
            e_num[i].add(n)
            all_nums.add(n)
            ex_num[i].add(n*2)
            e_num[i].add(n*2)
            all_nums.add(n*2)
        
        # remove biggest num:
        stop = False
        mx_total = -999
        mn_total = 999
        a_nums = all_nums.copy()

        while True:
            mn = max(all_nums)
            if stop:
                break
            for el in ex_num:
                if stop:
                    break
                if mn in el:
                    if len(el) == 1:
                        mx_total = mn
                        stop = True
                    else:
                        el.remove(mn)
            if not stop:
                all_nums.remove(mn)
        
        stop = False
        
        while True:
            mn = min(a_nums)
            if stop:
                break
            for el in e_num:
                if stop:
                    break
                if mn in el:
                    if len(el) == 1:
                        mn_total = mn
                        stop = True
                    else:
                        el.remove(mn)
            if not stop:
                a_nums.remove(mn)
        
        return abs(mx_total - mn_total)

    def is_even(self, n):
        if n%2==0:
            return True
        return False



def main():
    s = Solution()
    print(s.minimumDeviation([3,5]))
    print(s.minimumDeviation([4,1,5,20,3]))
    print(s.minimumDeviation([2,10,8]))
    pass

if __name__ == "__main__":
    main()


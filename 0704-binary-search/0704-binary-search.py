class Solution:
    def search(self, a: List[int], target: int) -> int:
        left=0
        right=len(a)-1
        while left<=right:
            mid=(left+right)//2  #int
            if a[mid]<target:
                left=mid+1
            elif a[mid]>target:
                right=mid-1
            else:
                return mid
        return -1  
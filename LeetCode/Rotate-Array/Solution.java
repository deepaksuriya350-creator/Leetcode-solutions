1class Solution {
2    public void rotate(int[] nums, int k) {
3        int n = nums.length;
4        k = k % n;
5
6        reverse(nums, 0, n - 1);
7        reverse(nums, 0, k - 1);
8        reverse(nums, k, n - 1);
9    }
10
11    private void reverse(int[] nums, int l, int r) {
12        while (l < r) {
13            int temp = nums[l];
14            nums[l] = nums[r];
15            nums[r] = temp;
16            l++;
17            r--;
18        }
19    }
20}
21
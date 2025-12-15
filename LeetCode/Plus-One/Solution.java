1class Solution {
2    public int[] plusOne(int[] digits) {
3        int n = digits.length;
4
5        for (int i = n - 1; i >= 0; i--) {
6            if (digits[i] < 9) {
7                digits[i]++;
8                return digits;
9            }
10            digits[i] = 0;
11        }
12
13        int[] result = new int[n + 1];
14        result[0] = 1;
15        return result;
16    }
17}
18
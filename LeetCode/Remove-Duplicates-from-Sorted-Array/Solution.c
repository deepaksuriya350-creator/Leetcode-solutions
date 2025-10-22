int removeDuplicates(int* nums, int numsSize) {
    if (numsSize == 0) return 0;

    int k = 1; // index for the next unique element
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] != nums[k - 1]) {
            nums[k] = nums[i];
            k++;
        }
    }
    return k;
}

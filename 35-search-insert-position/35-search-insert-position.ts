function searchInsert(nums: number[], target: number): number {
    // range search will be from 0 to len of the nums
    let l = 0, r = nums.length - 1;

    while(l <= r) {
        // middle will = (left + right) % 2
        // use left + (right - left) % 2 to avoid overflow
        let m = l + (r - l) % 2;

        // if equal target, return index
        if (nums[m] == target) {
            return m;
        }
        
        if (nums[m] < target) {
            // if middle value smaller then target
            // move the left to middle + 1 index
            l = m + 1;
        } else {
            // if middle value bigger then target
            // move the right to before the middle
            // (exclude the middle because already check)
            r = m - 1;
        }
    }
    
    return l  
};
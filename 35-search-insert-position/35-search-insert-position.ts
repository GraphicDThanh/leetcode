function searchInsert(nums: number[], target: number): number {
    const len = nums.length;
    if(len == 0) return -1;
    if (len == 1) {
        if (nums[0] < target) {
            return 1
        }
        return 0
    }
    
    // range search will be from 0 to len of the nums
    let l = 0, r = nums.length - 1;
    
    while(l < r) {
        // middle will = (left + right) // 2
        // use left + (right - left) // 2 to avoid overflow
        let m = l + (r - l) // 2;
        
        // if equal target, return index
        if (nums[m] == target) {
            return m;
        } else if (nums[m] < target) {
            // if middle value smaller then target
            // move the left to middle index
            l = m;
        } else {
            // if middle value bigger then target
            // move the right to before the middle
            // (exclude the middle because already check)
            r = m - 1;
        }
    }

    if (nums[r] == target) return r;
    if (nums[l] == target) return l;
    
    // if not found equal then return the closest index
    // where could insert
    if (nums[r] > target) {
        // there is special case where r is 0 then return 0 instead of -1
        if (r == 0) return 0
        
        return r - 1
    } else {
        return l + 1
    }
    
};
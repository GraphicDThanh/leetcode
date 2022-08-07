var searchInsert = function(nums, target) {
    let count = 0
    while (nums[count] < target) {
        count++
    }
    return count
};
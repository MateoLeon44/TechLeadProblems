var sortColors = function(nums) {
    let left = 0;
    let right = nums.length - 1;
    let zero = 0;
    while(left <= right) {
        if(nums[left] === 0) {
            let temp = nums[zero];
            nums[zero] = nums[left];
            nums[left] = temp;
            left++;
            zero++;
        } else if(nums[left] === 2) {
            let temp = nums[right];
            nums[right] = nums[left];
            nums[left] = temp;
            right--;
        } else {
            left++
        }
        
    }
    return nums;
};

var arr = [1,2,3,1,3,2]
console.log(sortColors(arr))
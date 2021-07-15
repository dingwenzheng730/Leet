/**
 * Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Input: [5]
Output: [5]

Input: [1,2,3,5,6]
Output: [1,2,3,5,6]

Precondition: 
nums.length = n
n >= 1
no int overflow

Postcondition:
nums should be changed
return nothing
keep relative order of non-zeros

C1: n = 1
C2: n > 1 and contains 0
C3: n> 1 and not 0 
C4: n > 1, contains 0 but no move needed

void moveZeroes(vector<int>& nums) {
    for (int lastNonZeroFoundAt = 0, cur = 0; cur < nums.size(); cur++) {
        if (nums[cur] != 0) {
            swap(nums[lastNonZeroFoundAt++], nums[cur]);
        }
    }
}
Algo:
Brute Force:
When meeting 0, reconstruct the array
Runtime: O(n)
Space: O(n)

Two pointer:
keep char from slow to fast all 0, when fast hits the end, done
Runtime: O(n)
Space: O(1)
*/

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
 var moveZeroes = function(nums) {
    for(let fast=0,slow=0; fast < nums.length; fast++){
        if (nums[fast] != 0) {
            let temp = nums[fast];
            nums[fast] = nums[slow];
            nums[slow] = temp
            slow ++;
        }
    }
    
};
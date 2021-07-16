/**
 * Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Input: [1]
Output: 0 

Input: [1,2,2]
Output: 1
public class Solution {
    public int triangleNumber(int[] nums) {
        int count = 0;
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; i++) {
            int k = i + 2;
            for (int j = i + 1; j < nums.length - 1 && nums[i] != 0; j++) {
                while (k < nums.length && nums[i] + nums[j] > nums[k])
                    k++;
                count += k - j - 1;
            }
        }
        return count;
    }
}
Precondition: 
n=nums.length
n >= 1
all positive number or 0
no int overflow

Postcondition:
nums can be changed
return int

C1: n < 3
C2: n =3
C3: n > 3

Algo:
Brute Force: for all 3 combinations, check if it is valid O(n^3)

Sort and three pointer
Sort O(nlogn)
loop over two pointer, adjust one pointer accordingly


 */
/**
 * @param {number[]} nums
 * @return {number}
 */
 const triangleNumber = function(nums) {
    let result = 0;
    nums.sort((a,b)=>{return a-b});
    for (let i=0; i<nums.length-2;i++) {
       let k = i + 2;
       for(let j=i+1; j<nums.length-1 && nums[i] != 0; j++) {
           while ((nums[k] < nums[i] + nums[j]) && k <nums.length) {
               k++;
           }
           result += (k - j - 1);
       }
   }
   return result;
};
class Solution {
    public boolean hasDuplicate(int[] nums) {
        // Arrays.sort(nums);
        // for (int i = nums.length - 1; i > 0; i--){
        //     if (nums[i] == nums[i-1]){
        //         return true;
        //     }
        // }
        // return false;
        Set<Integer> seen = new HashSet<>();
        for (int num : nums){
            if (seen.contains(num)){
                return true;
            }
            seen.add(num);
        }
        return false;
    }
}
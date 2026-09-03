class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const res = new Set();
        for (const i of nums){
            if (res.has(i)){
                return true
            }
            res.add(i);
            
        }
        return false;
    }
}

class Solution {
    public int missingNumber(int[] nums) {
        LinkedList<Integer> allNums = new LinkedList<>();
        for (int i = 0; i < nums.length + 1; i++){
            allNums.add(Integer.valueOf(i));
        }
        for (int i = 0; i < nums.length; i++){
            int value = nums[i];
            allNums.remove((Integer.valueOf(value)));
        }
        return (allNums.peek());
    }
}

import java.util.Arrays;

public class Solution {

    static int[] nums = {2,7,11,15};
    static int target = 9;

    public static void main(String[] args) {
        twoSum(nums,target);
    }

    public static int[] twoSum(int[] nums, int target) {

        int i = 0;
        int j = 0;

        int[] output = new int[0];
        for (int outerLoopIndex = 0; outerLoopIndex < nums.length; outerLoopIndex++) {
            i = nums[outerLoopIndex];
            for (int innerLoopIndex = outerLoopIndex + 1; innerLoopIndex < nums.length; innerLoopIndex++) {
                j = nums[innerLoopIndex];

                if (i + j == target) {
                    output = new int[]{innerLoopIndex, outerLoopIndex};
                    System.out.println(Arrays.toString(output));
                }
            }
        }
        return output;
    }
}

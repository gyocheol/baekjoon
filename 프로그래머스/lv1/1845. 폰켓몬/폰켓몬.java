import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int max = nums.length / 2;
        HashSet<Integer> setNums = new HashSet<>();
        for (int n : nums) {
            setNums.add(n);
        }
        return max < setNums.size() ? max : setNums.size();
    }
}
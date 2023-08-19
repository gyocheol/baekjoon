import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> ans = new ArrayList<Integer>();
        int lastNum = -1;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != lastNum) {
                lastNum = arr[i];
                ans.add(lastNum);
            }
        }
        return ans.stream().mapToInt(i->i).toArray();
    }
}
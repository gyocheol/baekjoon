import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list, int n) {
        // Arrays.copyOfRange()
        return Arrays.copyOfRange(num_list, 0, n);
        
        // // for문
        // int[] ans = new int[n];
        // for (int i = 0; i < n; i++) {
        //     ans[i] = num_list[i];
        // }
        // return ans;
    }
}
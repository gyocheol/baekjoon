class Solution {
    public int solution(int n) {
        int ans = 0;
        // 홀수
        if (n%2 == 1) {
            for (int i = 1; i < n+1; i+=2) {
                ans += i;
            }
        }
        // 짝수
        else {
            for (int i = 2; i < n+1; i+=2) {
                ans += Math.pow(i, 2);
            }
        }
        return ans;
    }
}
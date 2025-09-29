class Solution {
    public String solution(String my_string, int k) {
        // Java 11 이후에 나온 repeat 사용
        return my_string.repeat(k);
        
        // // Java 8 이전 버전
        // String ans = "";
        // for (int i=0; i < k; i++) {
        //     ans += my_string;
        // }
        // return ans;
    }
}
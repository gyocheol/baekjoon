class Solution {
    public int solution(String my_string, String is_prefix) {
        int ans = 0;
        if (my_string.length() < is_prefix.length()){
            return ans;
        }
        for (int i = 1; i < my_string.length(); i++) {
            String str = my_string.substring(0, i);
            if (str.equals(is_prefix)) {
                return 1;
            }
        }
        
        return ans;
    }
}
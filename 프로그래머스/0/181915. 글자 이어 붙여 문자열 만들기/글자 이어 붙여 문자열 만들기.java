class Solution {
    public String solution(String my_string, int[] index_list) {
        StringBuilder ans = new StringBuilder();
        for (int idx : index_list) {
            ans.append(my_string.charAt(idx));
        }
        return ans.toString();
    }
}
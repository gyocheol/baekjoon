import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<Integer, String> dict = new HashMap<>();
        int sumHash = 0;
        
        for (String part : participant) {
            dict.put(part.hashCode(), part);
            sumHash += part.hashCode();
        }
        for (String comp : completion) {
            sumHash -= comp.hashCode();
        }
        return dict.get(sumHash);
        
    }
}
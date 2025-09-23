import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] ans = new int[id_list.length];
        
        // id_list의 index를 미리 저장해 두기
        Map<String, Integer> indexMap = new HashMap<>();
        for (int i = 0; i < id_list.length; i++) {
            indexMap.put(id_list[i], i);
        }
        
        Map<String, Set<String>> map = new HashMap<>();
        for (String r : report) {
            String[] name = r.split(" ");
            String to = name[0];
            String from = name[1];
            
            map.computeIfAbsent(from, x -> new HashSet<>()).add(to);
        }
        for (Map.Entry<String, Set<String>> entry : map.entrySet()) {
            Set<String> reporters = entry.getValue();
            if (reporters.size() >= k) {
                for (String reporter : reporters) {
                    int idx = indexMap.get(reporter);
                    ans[idx] += 1;
                }
            }
        }
        
        return ans;
    }
}
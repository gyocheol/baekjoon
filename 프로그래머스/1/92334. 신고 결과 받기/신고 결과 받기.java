import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] ans = new int[id_list.length];
        
        // id_list의 index를 미리 저장해 두기
        Map<String, Integer> indexMap = new HashMap<>();
        for (int i = 0; i < id_list.length; i++) {
            indexMap.put(id_list[i], i);
        }
        
        Map<String, List<String>> map = new HashMap<>();
        for (String names : report) {
            String[] name = names.split(" ");
            String to = name[0];
            String from = name[1];
            
            // 신고를 받는 사람을 key로 두고 신고 하는 사람을 value로 저장
            map.putIfAbsent(from, new ArrayList<>());
            // 중복 신고 방지
            if (!map.get(from).contains(to)) {
                map.get(from).add(to);
            }
        }
        for (Map.Entry<String, List<String>> entry : map.entrySet()) {
            String reportedUser = entry.getKey();
            List<String> reporters = entry.getValue();
            
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
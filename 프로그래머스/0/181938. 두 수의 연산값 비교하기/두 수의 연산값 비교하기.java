class Solution {
    public int solution(int a, int b) {
        String abStr = ""+a+b;
        int ab = Integer.parseInt(abStr);
        int dbab = 2*a*b;
        
        return ab >= dbab? ab:dbab;
    }
}
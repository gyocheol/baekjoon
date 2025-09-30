class Solution {
    public int solution(int a, int b) {
        int ab = Integer.parseInt(""+a+b);
        int dbab = 2*a*b;
        
        return ab >= dbab? ab:dbab;
    }
}
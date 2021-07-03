public class darkPositive {
    public static void main(String args[]){
        int[] absolutes = {1,2,3};
        boolean[] signs = {false, false, true};

        Solution call = new Solution();
        call.solution(absolutes, signs);
    }
}

class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;
        int idx = 0;

        for(int i: absolutes){

            if (signs[idx] == true){
                answer += i;
            }
            else{
                answer += (i* -1);

            }
            idx++;
        }
        return answer;
    }
}
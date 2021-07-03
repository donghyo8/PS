import java.util.HashSet;

public class poneketmon {
    public static void main(String args[]){
        int[] nums = {3, 1, 2, 3};
        Solution call = new Solution();
        call.solution(nums);
    }
    
}

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        HashSet<Integer> hashset = new HashSet<>();
        int select_count = nums.length / 2;

        for(Integer i: nums){
            hashset.add(i);
        }

        System.out.println(hashset);
        for(Integer i: hashset){
            if (answer < select_count){
                answer++;
            }
        }
        return answer;
    }
}
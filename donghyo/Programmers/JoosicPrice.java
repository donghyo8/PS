import java.util.*;

public class JoosicPrice {
    public static void main(String args[]){
        int[] prices = {1, 2, 3, 2, 3};
        Solution call = new Solution();
        call.solution(prices);
    }
}

class Solution {
    public int[] solution(int[] prices) {
        int[] answer = {};
        ArrayList<Integer> arr = new ArrayList<>();

        for(int i = 0; i < prices.length; i++){
            int seconds = 0;

            for(int j = i + 1; j < prices.length; j++){
                if(prices[i] <= prices[j]){
                    seconds++;
                }
                else{
                    seconds++;
                    break;
                }
            }
            arr.add(seconds);
        }
        answer = arr.stream().mapToInt(i -> i).toArray();
        System.out.println(Arrays.toString(answer));
        return answer;
    }
}

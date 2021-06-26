import java.util.Arrays;

public class Immigration {
    public static void main(String args[]){
        int n = 6;
        int[] times = {7, 10};
        Solution call = new Solution();
        call.solution(n, times);
    }
}

class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        // int max_value = times[0];

        // for (int i = 1; i < times.length; i++){
        //     if (max_value < times[i]){
        //         max_value = times[i];
        //     }
        // }

        Arrays.sort(times);

        int left = 0;
        int right = n * times[times.length - 1];

        while (left <= right){
            int mid = (left + right) / 2;
            int sum = 0;

            for (int e : times){
                sum += mid / e;
            }
            System.out.println(sum);

            if (sum < n){
                left = mid + 1;
            }
            else {
                right = mid - 1;
                answer = mid;
            }
        }
        // System.out.println(answer);
        return answer;
    }
}
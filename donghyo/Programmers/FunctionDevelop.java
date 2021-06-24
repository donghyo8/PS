import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Collector;
import java.util.stream.Collectors;

public class FunctionDevelop {
    public static void main(String[] args) {
        int[] progresses = {95, 90, 99, 99, 80, 99};
        int[] speeds = {1, 1, 1, 1, 1, 1};

        Solution call = new Solution();
        call.solution(progresses, speeds);
    }
}

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> arr = new ArrayList<>();
        int[] answer = new int[progresses.length];
        int[] day = new int[progresses.length];
        int limit_percent = 100;
        int idx = 0;
        int answer_idx = 0;
        answer[0] = 1;

        while (idx <= progresses.length -1){
            int progresse = 0;
            int start = progresses[idx];

            while(progresse < limit_percent){
                progresse += start + speeds[idx];
                start = 0;
                day[idx]++;
            }
            if (day[idx] > 0 && idx >= 1){
                if(day[idx-1] >= day[idx]){
                    answer[answer_idx] += 1;

                }else{
                    answer_idx++;
                    answer[answer_idx] += 1;
                }     
                
            }
            idx++;
        }
        for(Integer e: answer){
            if (e != 0){
                arr.add(e);
            }
        }
        answer = arr.stream().mapToInt(i -> i).toArray();
        // System.out.println(Arrays.toString(answer));
        return answer;
    }
}

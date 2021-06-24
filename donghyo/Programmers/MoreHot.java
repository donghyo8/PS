import java.util.ArrayList;
import java.util.PriorityQueue;

public class MoreHot {
    public static void main(String args[]){
        int[] scoville = {1, 2, 3, 9, 10, 12};
        int K = 7;
        Solution call = new Solution();
        call.solution(scoville, K);
    }
}

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        
        for(Integer e : scoville){
            minHeap.add(e);
        }

        while(!minHeap.isEmpty()){
            int first_min_scoville = minHeap.poll();
            int seconds_min_scoville = minHeap.poll();
            int new_scoville = first_min_scoville + (seconds_min_scoville * 2);

            minHeap.offer(new_scoville);
            answer++;

            if(minHeap.peek() >= K){
                System.out.println(answer);
                return answer;
            }
        }
        return -1;
    }
}


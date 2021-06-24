import java.util.*;
 
public class Printer {
    public static void main(String[] args){
        int[] priorities = {1, 1, 9, 1, 1, 1};
        int location = 0;
        Solution call = new Solution();
        call.solution(priorities, location);

    }
}

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 1;
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        
        for(Integer e : priorities){
            maxHeap.add(e);
        }

        while(!maxHeap.isEmpty()){
            for(int idx = 0; idx < priorities.length; idx++){
                int temp = maxHeap.peek();

                if(priorities[idx] == temp){
                    System.out.println(temp);
                    if(idx == location){
                        System.out.println(answer);
                        return answer;
                    }
                    maxHeap.poll();
                    answer++;
                }
                
            }
        }
        return answer;
    }
}

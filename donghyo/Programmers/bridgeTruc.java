import java.util.Queue;
import java.util.Arrays;
import java.util.LinkedList;

public class bridgeTruc {
    public static void main(String[] args) {
        int bridge_length = 2;
        int weight = 10;
        int[] truck_weights = { 7, 4, 5, 6 };

        Solution call = new Solution();
        call.solution(bridge_length, weight, truck_weights);
    }
}

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> queue = new LinkedList<>();
        Queue<Integer> finish_truc = new LinkedList<>();
        boolean[] bridge_wait = new boolean[bridge_length];
        int limit_length = bridge_length - 1;
        int weight_sum = 0;
        int seconds = 1;
        int idx = 1;

        queue.add(truck_weights[0]);
        weight_sum = truck_weights[0];
        bridge_wait[limit_length] = true;

        while (!queue.isEmpty()) {
            seconds++;
            int i = 0;

            if (bridge_wait[0]) {
                finish_truc.add(queue.peek());
                weight_sum -= queue.poll();
            }

            while (i != limit_length) {
                bridge_wait[i] = bridge_wait[i + 1];
                i++;
            }
            bridge_wait[limit_length] = false;
            
            if (truck_weights.length > idx) {
                int next_truc = truck_weights[idx];

                if (weight >= weight_sum + next_truc) {
                    weight_sum += next_truc;
                    bridge_wait[limit_length] = true;
                    queue.add(next_truc);
                    idx++;
                }
            }
        }

        // System.out.println(finish_truc);
        // System.out.println(seconds);
        return seconds;
    }
}
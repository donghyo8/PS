import java.util.Queue;
import java.util.Arrays;
import java.util.LinkedList;

public class farthesNode {
    public static void main(String[] args) {
        int n = 6;
        int[][] vertex = { { 3, 6 }, { 4, 3 }, { 3, 2 }, { 1, 3 }, { 1, 2 }, { 2, 4 }, { 5, 2 } };

        Solution call = new Solution();
        call.solution(n, vertex);
    }
}

class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        int max_value = 0;
        boolean[][] graph = new boolean[n + 1][n + 1];
        int[] visited = new int[n + 1];
        Queue<Integer> queue = new LinkedList<>();

        queue.add(1);
        visited[1] = 1;

        for (int i = 0; i < edge.length; i++) {
            graph[edge[i][0]][edge[i][1]] = true;
            graph[edge[i][1]][edge[i][0]] = true;
        }

        while (!queue.isEmpty()) {
            int loc = queue.poll();

            for (int i = 1; i <= n; i++) {
                if (graph[i][loc] && visited[i] == 0) {
                    queue.add(i);
                    visited[i] = visited[loc] + 1;
                    max_value = Math.max(max_value, visited[i]);
                }
            }
        }
        for (int i = 1; i <= n; i++) {
            if (max_value == visited[i]) {
                answer++;
            }
        }
        // System.out.println(Arrays.deepToString(graph));
        // System.out.println(Arrays.toString(visited));
        // System.out.println(answer);
        return answer;
    }
}
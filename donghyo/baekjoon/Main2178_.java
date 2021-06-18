import java.util.Queue;
import java.util.LinkedList;

public class Main2178_ {
    public static void main(String[] args) {
        int N = 4, M = 6;
        int[][] matrix = { { 1, 0, 1, 1, 1, 1 }, { 1, 0, 1, 0, 1, 0 }, { 1, 0, 1, 0, 1, 1 }, { 1, 1, 1, 0, 1, 1 } };
        int[][] visited = new int[N][M];
        int res = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                visited[i][j] = 0;
            }
        }

        res += solution(matrix, visited, 0, 0, N, M);
        System.out.println(res);
    }

    public static int solution(int[][] matrix, int[][] visited, int i, int j, int N, int M) {
        Queue<int[]> queue = new LinkedList<>();
        int[] valid_x = { -1, 1, 0, 0 }, valid_y = { 0, 0, -1, 1 };
        int count = 0;

        queue.offer(new int[] { i, j });

        visited[i][j] = 1;

        while (!queue.isEmpty()) {
            int[] loc = queue.poll();

            if (loc[0] == N - 1 && loc[1] == M - 1){
                return visited[loc[0]][loc[1]];
            }

            for (int idx = 0; idx < 4; idx++) {
                int check_x = loc[0] + valid_x[idx];
                int check_y = loc[1] + valid_y[idx];

                if (0 <= check_x && check_x < N && 0 <= check_y && check_y < M) {
                    if(visited[check_x][check_y] == 0 && matrix[check_x][check_y] == 1){
                        visited[check_x][check_y] = visited[loc[0]][loc[1]] + 1;
                        queue.offer(new int[] {check_x, check_y});
                    }

                }
            }
        }
        return count;
    }
}

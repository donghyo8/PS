// 미로탐색

let solution = (matrix, N, M) => {
    let [valid_x, valid_y] = [[-1, 1, 0, 0], [0, 0, -1, 1]];
    let visited = Array.from(Array(N), () => Array());
    let queue = [];

    for (let i = 0; i < N; i++) {
        for (let j = 0; j < M; j++) {
            visited[i][j] = 0;
        }
    }
    visited[0][0] = 1;
    queue.push([0, 0]);

    while (queue.length) {
        [x, y] = queue.shift();

        if (x == N - 1 && y == M - 1) {
            return visited[x][y];
        }

        for (let i = 0; i < 4; i++) {
            let check_x = x + valid_x[i];
            let check_y = y + valid_y[i];

            if (0 <= check_x && check_x < N && 0 <= check_y && check_y < M) {
                if (visited[check_x][check_y] == 0 && matrix[check_x][check_y] == 1) {
                    visited[check_x][check_y] = visited[x][y] + 1
                    queue.push([check_x, check_y]);
                }
            }
        }
    }
}

let func = () => {
    let N = 4, M = 6;
    matrix = [[101111], [101010], [101011], [111011]];

    splitMatrix = [];
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            splitMatrix.push(String(matrix[i]).split(''))
        }
    }

    let result = solution(splitMatrix, N, M);
    console.log(result);

}
func();


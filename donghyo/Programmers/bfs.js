let dfs = (matrix, number, i, j) => {
    let [valid_x, valid_y] = [[-1, 1, 0, 0], [0, 0, -1, 1]];
    let N = matrix.length;
    let visited = Array.from(Array(N), () => Array());
    let stack = [];

    for (let i = 0; i < N; i++) {
        for (let j = 0; j < N; j++) {
            visited[i][j] = false;
        }
    }
    stack.push([i, j]);

    let [x, y] = stack.pop();

    if (visited[x][y] === false) {
        visited[x][y] = true;
    }

    for (let i = 0; i < 4; i++) {
        let check_x = x + valid_x[i];
        let check_y = y + valid_y[i];


        if (0 <= check_x && check_x < N && 0 <= check_y && check_x < N && matrix[check_x][check_y] === number) {
            matrix[check_x][check_y] = undefined;
            dfs(matrix, number, check_x, check_y)

        }

    }
}

function solution(v) {
    let answer = [0, 0, 0];

    for (let i = 0; i < v.length; i++) {
        for (let j = 0; j < v.length; j++) {
            if (v[i][j] === 0) {
                dfs(v, 0, i, j);
                answer[0] += 1;
            }
            else if (v[i][j] === 1) {
                dfs(v, 1, i, j);
                answer[1] += 1;
            }
            else if (v[i][j] === 2) {
                dfs(v, 2, i, j);
                answer[2] += 1;
            }
        }
    }
    return answer;
}
let v = [[0, 0, 1], [2, 2, 1], [0, 0, 0]];
console.log(solution(v));


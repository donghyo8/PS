// 2차원 배열 매트릭스로 변환하고 영역탐색
let func3 = (matrix, i, j, N) => {
    let [valid_x, valid_y] = [[-1, 1, 0, 0], [0, 0, -1, 1]];
    let visited = Array.from(Array(N), () => Array());
    queue = [];
    count = 0;

    for (let i = 0; i < N; i++) {
        for (let j = 0; j < N; j++) {
            visited[i][j] = 0;
        }
    }

    queue.push([i, j]);

    while (queue.length) {
        [x, y] = queue.shift();

        if (visited[x][y] === 0) {
            visited[x][y] = 1;
            count++;
        }

        for (let i = 0; i < 4; i++) {
            let check_x = x + valid_x[i];
            let check_y = y + valid_y[i];

            if (0 <= check_x && check_x < N && 0 <= check_y && check_x < N && matrix[check_x][check_y] === 1) {
                console.log(check_x, check_y)
                matrix[check_x][check_y] = 0;
                queue.push([check_x, check_y]);
            }
        }
    }
    return count
}
matrix = [[0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0]];
let component = 0;
let result = [];
let N = 7;

for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix.length; j++) {
        if (matrix[i][j] === 1) {
            result.push(func3(matrix, i, j, N));
            component++;
        }

    }
}
console.log(result);
console.log(component);
function solution(answers) {
    var answer = [];
    let supo1 = [1, 2, 3, 4, 5];
    let supo2 = [2, 1, 2, 3, 2, 4, 2, 5];
    let supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    let score = [0, 0, 0];

    for (let i = 0; i <= answers.length; i++) {
        if (answers[i] == supo1[i % 5]) {
            score[0] += 1;
        }
        if (answers[i] == supo2[i % 8]) {
            score[1] += 1;
        }
        if (answers[i] == supo3[i % 10]) {
            score[2] += 1;
        }
    }

    let max_student = Math.max(...score)
    console.log(score)

    for (let i = 0; i <= 3; i++) {
        if (score[i] == max_student) {
            answer.push(i + 1);
        }
    }
    console.log(answer)

    return answer;
}
solution([1, 3, 2, 4, 2]);
let solution = (bracket) => {
    let answer = '';
    let stack = [];

    for (let i in bracket) {
        if (stack.length === 0) {
            if (bracket[i] === '(') {
                stack.push(i);
            }
            else {
                answer = false;
                return answer
            }
        }
        else if (bracket[i] == '(') {
            stack.push(i);
        }
        else if (bracket[i] == ')') {
            stack.pop();
        }
    }
    if (stack.length === 0) {
        answer = true;
        return answer
    }
    answer = false;
    return answer
}
let s = "(()("
solution(s)
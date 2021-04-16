function solution(numbers) {
    var answer = '';

    numbers = numbers.map((element) => element + "").sort((a, b) => (b + a) - (a + b));
    numbers[0] === '0' ? answer += 0 : answer = numbers.join("");

    return answer;
}
solution([6, 10, 2]);
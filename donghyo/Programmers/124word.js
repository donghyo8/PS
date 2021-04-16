function solution(n) {
    var answer = '';
    let temp = [];
    
    while (n != 0) {
        if (n % 3 === 0) {
            temp.unshift(4);
            n = parseInt((n / 3)) - 1;

        } else {
            temp.unshift(n % 3);
            n = parseInt((n / 3));
        }
    }
    answer = temp.join('');
    return answer;
}
solution(4);
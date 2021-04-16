function solution(n) {
    var answer = 0;
    let preNumber = 0, nextNumber = 0;
    let result = [];
    let count = 0;

    if (n <= 1000000) {
        let i = 1;
        while (n) {
            let pre = n + i;
            preNumber = n.toString(2);
            nextNumber = pre.toString(2);
            i += 1

            let valid1 = preNumber.match(/1/g);
            let valid2 = nextNumber.match(/1/g);

            if (valid1.length === valid2.length){
                result.push(nextNumber);
                count++;
            }
            if(count === 1){
                answer = result;
                break;
            }
            
        }
    }

    answer = parseInt(answer, 2)
    return answer;
}

solution(78);
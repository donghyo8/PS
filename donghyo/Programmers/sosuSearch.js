// 순열
let permutation = (numbers) => {
    const result = new Set();

    const temp = (currFix, eachArr) => {
        for (let i = 0; i < eachArr.length; i++) {
            const tempEachArr = [...eachArr];
            const tempCurrFixVal = tempEachArr.splice(i, 1)[0];
            const tempCurrFix = currFix + tempCurrFixVal;
            result.add(Number(tempCurrFix));
            if (tempEachArr.length > 0) temp(tempCurrFix, tempEachArr);
        }
    };

    for (let i = 0; i < numbers.length; i++) {
        let target = numbers[i];
        result.add(Number(target));

        const eachArr = [...numbers];
        eachArr.splice(i, 1);

        temp(target, eachArr);
    }

    return new Array(...result);
}

// 에라토스테네스의 체
let decimal = (inputArr) => {
    
    for (let i=0; i<inputArr.length; i++){
        if(inputArr[i] === 0){
            inputArr.splice(i, 1);
        }
        if (inputArr[i] === 1){
            inputArr.splice(i, 1)
        }
    }
    console.log(inputArr)
    let result = inputArr.length;

    for (let i = 0; i < inputArr.length; i++) {
        if (inputArr[i] != 2) {
            for (let j = 2; j < (inputArr[i] ** 0.5) + 1; j++) {
                if (inputArr[i] % j == 0){
                    result -= 1;
                    break
                }
            }
        }
    }
    return result
}

function solution(numbers) {
    var answer = 0;

    let temp = permutation(numbers);
    answer = decimal(temp)

    console.log(answer)
    return answer;
}
solution("011")


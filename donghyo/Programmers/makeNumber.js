function solution(number, k) {
    var answer = '';
    let stack = [];
    let count = 0;

    for (let i = 0; i < number.length; i++) {
        while (stack.length != 0) {
            if (count == k) break;

            // 큰 숫자를 기준으로 stack에 집어넣으며 number의 값과 비교
            // number의 값보다 작으면 빼버림
            if (stack[stack.length - 1] < number[i]) {
                stack.pop();
                count++;

            } else break;
        }
        stack.push(number[i]);
    }
    answer = stack.join("").substr(0, number.length - k);
    return answer;
}

solution("1924", 3);

// function combination(arr, selectNum) {
//     const result = [];
//     if (selectNum === 1) return arr.map((v) => [v]);

//     arr.forEach((v, idx, arr) => {
//       const fixed = v;
//       const restArr = arr.slice(idx + 1);
//       const combinationArr = combination(restArr, selectNum - 1);
//       const combineFix = combinationArr.map((v) => [fixed, ...v]);
//       result.push(...combineFix);
//     });
//     return result;
//   }

    // let temp = [];
    // let result = [];
    // let newResult = [];

    // temp = number.split("");

    // if (number.length / 2 < 4){
    //     result = combination(temp, parseInt(number.length % 2) + parseInt(number.length / 2))
    // }
    // else{
    //     result = combination(temp, parseInt(number.length % 2) + parseInt(number.length / 2)+1)
    // }

    // for(let i=0; i<result.length; i++){
    //     newResult.push(result[i].join(""));
    // }

    // answer = Math.max.apply(null, newResult);
    // console.log(String(answer))
    // return String(answer);
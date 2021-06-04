function solution(n) {
    if (n === 1) return "11";
    else if (n >= 40) return 0;
    console.log(n);
    return antSequence(solution(n - 1)); 
}

function antSequence(n) {
    let arr1 = []; 
    let arr2 = []; 
    let answer = "";
    console.log(n)

    while (n.length !== 0) {
        if (n[0] === n[1]) { // 첫글자와 다음 글자가 같다면 맨 처음 숫자 저장
            arr2.push(n[0]);
            n = n.toString().replace(n[0], "");

        } else {
            arr2.push(n[0]); 
            n = n.toString().replace(n[0], ""); 
            arr1.push(arr2); 
            arr2 = []; 
        }
    }

    arr1.forEach(element => {
        answer += element[0] + element.length;
    });
    
    return String(answer);
}

solution(5);
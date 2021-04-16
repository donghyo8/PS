function solution(a, b) {
    var answer = '';
    let days = ["FRI", "SAT",'SUN', 'MON', 'TUE', "WED", "THU"];
    let month_End = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    let day_Total = 0; 

    for(let i=0; i< a-1; i++){
        day_Total += month_End[i];
    }

    day_Total += b - 1;
    answer = days[day_Total % 7];

    console.log(answer);
    return answer;
}

solution(5, 24);
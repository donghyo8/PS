class stack {

    constructor(arr) {
        this.arr = arr;
        this.idx = 0;
        this.temp = 0;
    }

    push = (number) => {
        this.arr[this.idx] = number;
        this.idx++;
    }

    pop = () => {
        return this.arr[--this.idx];
    }

    getMin = () => {
        let min = this.arr[0];
        for (let i = 1; i < this.arr.length; i++) {
            if (min > this.arr[i]) {
                min = this.arr[i];
            }
        }
        return min
    }

}

let obj = new stack(new Array(10));
obj.push(1);
obj.push(2);
obj.push(3);
console.log(obj.getMin());






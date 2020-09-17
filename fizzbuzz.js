function fizzbuzz(n, fizzNo, buzzNo) {
    let current = 1;
    do {
        let ans = ''
        if (current % fizzNo === 0) {
            ans += 'Fizz';
        }
        if (current % buzzNo === 0) {
            ans+= 'Buzz';
        }
        if (!ans) {
            ans = current;
        }
        console.log(ans);
        current ++;
    } while (current < n+1)
}

let num = prompt('Pick a number to begin FizzBuzz: ') 
let fizz = prompt('Fizz: ') 
let buzz = prompt('Buzz: ') 

fizzbuzz(Number(num), Number(fizz), Number(buzz));



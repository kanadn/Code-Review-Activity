// Optimized JavaScript program for fizz buzz problem
// optimized because % is a heavy op
let s = "";
let c3 = 0, c5 = 0;
for (var i = 1; i <= 100; i++) {
    c3++;
    c5++;
    if (c3 == 3) {
        s += "fizz";
        c3 = 0;
    }
    if (c5 == 5) {
        s += "buzz";
        c5 = 0;
    }
    if (s.length == 0)
        console.log(i);
    else
        console.log(s);
    s = "";
}

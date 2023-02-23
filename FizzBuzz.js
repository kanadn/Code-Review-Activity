for (let i=1; i<=100; i++){         
    // number divisible by 3? print 'Fizz'
    // in place of the number
    if ((i%3) == 0)
        console.log("Fizz" + " ");               
        
    // number divisible by 5, print 'Buzz'
    // in place of the number
    else if ((i%5) == 0)                   
        console.log("Buzz" + " "); 


    // number divisible by 3 and 5 will
    // always be divisible by 15, print
    // 'FizzBuzz' in place of the number
    if (i%15 == 0)   
        console.log("FizzBuzz" + " ");              
    
    else // print the number       
        console.log(i + " ");               
}
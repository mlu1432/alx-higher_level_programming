#!/usr/bin/node
function factorial(n) {
	  if (isNaN(n)) {
		      return (1);
		    } else if (n === 0 || n === 1) {
			        return (1);
			      } else if (n < 0) {
				          return (Infinity);
				        } else {
						    let result = 1;
						    for (let i = 2; i <= n; i++) {
							          result *= i;
							        }
						    return (result);
						  }
}

console.log(factorial(Number(process.argv[2])));

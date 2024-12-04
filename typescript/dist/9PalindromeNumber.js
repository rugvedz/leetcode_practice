"use strict";
function isPalindrome(x) {
    let isPal = true;
    const xString = x.toString();
    for (let i = 0; i < Math.floor(xString.length / 2); i++) {
        if (xString[i] != xString[xString.length - 1 - i]) {
            isPal = false;
        }
    }
    return isPal;
}
console.log(isPalindrome(121));

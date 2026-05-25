// 3 CORE DATATYPES IN TS



// 1. STRING DATATYPE

const str1 = 'This is created using single quotes! ${str2}';    // Single quotes (') don't support 
const str2 = 'This is created using double quotes!';            // variable interpolation (${}).
const str3 = `This is created using back ticks!`

// We can not create strings in multiple lines using single - or double quotes.
// With back ticks, writing code in many lines is possible.

const str4 = `This is created 
            using back ticks
             ${str1}, 
            written in two lines!`

console.log(str4);
console.log(str1); 



// 2. NUMBER DATATYPE

let num = 14;
const pi = 3.141592653;

// TypeScript numbers are ALWAYS floating numbers.
// E.g.: num (14) will be saved as a floating number (12.0).
// This also applies to JavaScript.



// 3. BOOLEAN DATATYPE


let isEligible = true;
let isEqual = false;

console.log(Boolean(0));        // Terminal output: false
console.log(Boolean(100));      // Terminal output: true

console.log(Boolean(''));       // Terminal output: false
console.log(Boolean(' '));      // Terminal output: true

console.log(Boolean(null));     // Terminal output: false
console.log(Boolean('Hello'));  // Terminal output: true

// 0, '' and null are falsy values.

// Using a comparison operator results in a boolean.

let isGreater = 10 > 15;
console.log(isGreater);         // Terminal output: false (10 < 15)

// "isGreater" is a boolean

//  Function: validateUnionType
function validateUnionType(value: any, allowedTypes: string[]): boolean {
  // loop over the allowed types
  for (const type of allowedTypes) {
    if (typeof value === type) {
      return true; // value matches one of the allowed types
    }
  }
  return false; // no match found
}

//  Testing the function

// Numbers and strings allowed
console.log("Test 1:", validateUnionType(42, ["number", "string"]));        // true
console.log("Test 2:", validateUnionType("hello", ["number", "string"]));  // true
console.log("Test 3:", validateUnionType(true, ["number", "string"]));     // false

// Object type allowed
console.log("Test 4:", validateUnionType({ name: "Alice" }, ["object"]));  // true

// Undefined not allowed
console.log("Test 5:", validateUnionType(undefined, ["number", "string"])); // false

// Boolean type allowed
console.log("Test 6:", validateUnionType(false, ["boolean", "string"]));    // true

// Function type allowed
console.log("Test 7:", validateUnionType(() => {}, ["function", "object"])); // true

// Symbol type allowed

console.log("Test 8:", validateUnionType(() => {}, ["function", "object"])); // true


// Null type checking (typeof null === "object")
console.log("Test 9:", validateUnionType(null, ["object"])); // true

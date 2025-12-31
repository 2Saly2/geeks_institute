var user = {
    name: "Nouhaila",
    age: 24,
    street: "Rue Hassan II",
    city: "Casablanca"
};
// Exercise 2: Type Guards with Union Types
function describeValue(value) {
    if (typeof value === "number")
        return "This is a number";
    return "This is a string";
}
console.log(describeValue(10));
console.log(describeValue("Hello"));
// Exercise 3: Type Casting
var someValue = "Hello TypeScript";
var strValue = someValue;
console.log(strValue.toUpperCase());
// Exercise 4: Type Assertions with Union Types
function getFirstElement(arr) {
    return arr[0];
}
console.log(getFirstElement(["apple", 10]));
console.log(getFirstElement([20, 30]));
// Exercise 5: Generic Constraints
function logLength(value) {
    console.log(value.length);
}
logLength("Hello");
logLength([1, 2, 3]);
function describeEmployee(emp) {
    if (emp.position === "Manager") {
        return "".concat(emp.name, " is a manager of ").concat(emp.department);
    }
    if (emp.position === "Developer") {
        return "".concat(emp.name, " is a developer in ").concat(emp.department);
    }
    return "".concat(emp.name, " works in ").concat(emp.department);
}
var emp1 = {
    name: "Omar",
    age: 30,
    position: "Manager",
    department: "IT"
};
console.log(describeEmployee(emp1));
// Exercise 7: Generic Constraints + Type Assertions
function formatInput(input) {
    var strValue = input.toString();
    return "Formatted: ".concat(strValue);
}
console.log(formatInput(100));
console.log(formatInput("Hello World"));

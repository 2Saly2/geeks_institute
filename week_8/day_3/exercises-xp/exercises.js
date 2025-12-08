// ===========================
// TypeScript Classes & Interfaces Exercises
// ===========================
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
//  Exercise 1: Class with Access Modifiers
var Employee = /** @class */ (function () {
    function Employee(name, salary, position, department) {
        this.name = name;
        this.salary = salary;
        this.position = position;
        this.department = department;
    }
    Employee.prototype.getEmployeeInfo = function () {
        return "Name: ".concat(this.name, ", Position: ").concat(this.position);
    };
    return Employee;
}());
// Test Exercise 1
var emp = new Employee("Alice", 50000, "Developer", "IT");
console.log(emp.getEmployeeInfo()); // Name: Alice, Position: Developer
// console.log(emp.name); // Error: private
// console.log(emp.department); // Error: protected
// ------------------------------------------------------
// Exercise 2: Readonly Properties in a Class
var Product = /** @class */ (function () {
    function Product(id, name, price) {
        this.id = id;
        this.name = name;
        this.price = price;
    }
    Product.prototype.getProductInfo = function () {
        return "Product: ".concat(this.name, ", Price: $").concat(this.price);
    };
    return Product;
}());
// Test Exercise 2
var prod = new Product(1, "Laptop", 1200);
console.log(prod.getProductInfo()); // Product: Laptop, Price: $1200
// prod.id = 5; // Error: Cannot assign to 'id' because it is a readonly property
// ------------------------------------------------------
// Exercise 3: Class Inheritance
var Animal = /** @class */ (function () {
    function Animal(name) {
        this.name = name;
    }
    Animal.prototype.makeSound = function () {
        return "Some generic sound";
    };
    return Animal;
}());
var Dog = /** @class */ (function (_super) {
    __extends(Dog, _super);
    function Dog() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Dog.prototype.makeSound = function () {
        return "bark";
    };
    return Dog;
}(Animal));
// Test Exercise 3
var dog = new Dog("Buddy");
console.log("".concat(dog.name, " says: ").concat(dog.makeSound())); // Buddy says: bark
// ------------------------------------------------------
// Exercise 4: Static Properties and Methods
var Calculator = /** @class */ (function () {
    function Calculator() {
    }
    Calculator.add = function (a, b) {
        return a + b;
    };
    Calculator.subtract = function (a, b) {
        return a - b;
    };
    return Calculator;
}());
// Test Exercise 4
console.log("Add 5 + 3 =", Calculator.add(5, 3)); // 8
console.log("Subtract 10 - 7 =", Calculator.subtract(10, 7)); // 3
function printUserDetails(user) {
    console.log("ID: ".concat(user.id));
    console.log("Name: ".concat(user.name));
    console.log("Email: ".concat(user.email));
    if (user.membershipLevel) {
        console.log("Membership Level: ".concat(user.membershipLevel));
    }
}
// Test Exercise 5
var premiumUser = {
    id: 101,
    name: "Bob",
    email: "bob@example.com",
    membershipLevel: "Gold"
};
printUserDetails(premiumUser);
// ------------------------------------------------------

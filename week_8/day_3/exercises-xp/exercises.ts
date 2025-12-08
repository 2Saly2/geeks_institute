// ===========================
// TypeScript Classes & Interfaces Exercises
// ===========================

//  Exercise 1: Class with Access Modifiers
class Employee {
  private name: string;
  private salary: number;
  public position: string;
  protected department: string;

  constructor(name: string, salary: number, position: string, department: string) {
    this.name = name;
    this.salary = salary;
    this.position = position;
    this.department = department;
  }

  public getEmployeeInfo(): string {
    return `Name: ${this.name}, Position: ${this.position}`;
  }
}

// Test Exercise 1
const emp = new Employee("Alice", 50000, "Developer", "IT");
console.log(emp.getEmployeeInfo()); // Name: Alice, Position: Developer
// console.log(emp.name); // Error: private
// console.log(emp.department); // Error: protected

// ------------------------------------------------------

// Exercise 2: Readonly Properties in a Class
class Product {
  readonly id: number;
  public name: string;
  public price: number;

  constructor(id: number, name: string, price: number) {
    this.id = id;
    this.name = name;
    this.price = price;
  }

  getProductInfo(): string {
    return `Product: ${this.name}, Price: $${this.price}`;
  }
}

// Test Exercise 2
const prod = new Product(1, "Laptop", 1200);
console.log(prod.getProductInfo()); // Product: Laptop, Price: $1200
// prod.id = 5; // Error: Cannot assign to 'id' because it is a readonly property

// ------------------------------------------------------

// Exercise 3: Class Inheritance
class Animal {
  public name: string;
  constructor(name: string) {
    this.name = name;
  }

  makeSound(): string {
    return "Some generic sound";
  }
}

class Dog extends Animal {
  makeSound(): string {
    return "bark";
  }
}

// Test Exercise 3
const dog = new Dog("Buddy");
console.log(`${dog.name} says: ${dog.makeSound()}`); // Buddy says: bark

// ------------------------------------------------------

// Exercise 4: Static Properties and Methods
class Calculator {
  static add(a: number, b: number): number {
    return a + b;
  }

  static subtract(a: number, b: number): number {
    return a - b;
  }
}

// Test Exercise 4
console.log("Add 5 + 3 =", Calculator.add(5, 3));       // 8
console.log("Subtract 10 - 7 =", Calculator.subtract(10, 7)); // 3

// ------------------------------------------------------

// Exercise 5: Extending Interfaces with Optional and Readonly Properties
interface User {
  readonly id: number;
  name: string;
  email: string;
}

interface PremiumUser extends User {
  membershipLevel?: string;
}

function printUserDetails(user: PremiumUser): void {
  console.log(`ID: ${user.id}`);
  console.log(`Name: ${user.name}`);
  console.log(`Email: ${user.email}`);
  if (user.membershipLevel) {
    console.log(`Membership Level: ${user.membershipLevel}`);
  }
}

// Test Exercise 5
const premiumUser: PremiumUser = {
  id: 101,
  name: "Bob",
  email: "bob@example.com",
  membershipLevel: "Gold"
};
printUserDetails(premiumUser);

// ------------------------------------------------------

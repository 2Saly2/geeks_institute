
// Exercise 1: Hello, World!
console.log("Exercise 1: Hello, World!");
console.log("Hello, World!\n");

// Exercise 2: Type Annotations
console.log("Exercise 2: Type Annotations");
let age: number = 25;
let name1: string = "Alice";
console.log("Name:", name1);
console.log("Age:", age, "\n");

// Exercise 3: Union Types
console.log("Exercise 3: Union Types");
let id: string | number;
id = 123;
console.log("ID as number:", id);
id = "ABC123";
console.log("ID as string:", id, "\n");

// Exercise 4: Control Flow with if...else
console.log("Exercise 4: Control Flow with if...else");
function checkNumber(num: number): string {
  if (num > 0) return "Positive";
  else if (num < 0) return "Negative";
  else return "Zero";
}
console.log(checkNumber(10));  // Positive
console.log(checkNumber(-5));  // Negative
console.log(checkNumber(0), "\n");   // Zero

// Exercise 5: Tuple Types
console.log("Exercise 5: Tuple Types");
function getDetails(name: string, age: number): [string, number, string] {
  const message = `Hello, ${name}! You are ${age} years old.`;
  return [name, age, message];
}
const details = getDetails("Alice", 25);
console.log(details, "\n");

// Exercise 6: Object Type Annotations
console.log("Exercise 6: Object Type Annotations");
type Person = {
  name: string;
  age: number;
};
function createPerson(name: string, age: number): Person {
  return { name, age };
}
const person = createPerson("Bob", 30);
console.log(person, "\n");

// Exercise 7: Type Assertions
console.log("Exercise 7: Type Assertions");
// Note: This needs to run in a browser environment
// <input id="myInput" type="text">
const inputElement = document.getElementById("myInput") as HTMLInputElement;
if (inputElement) {
  inputElement.value = "Hello, TypeScript!";
  console.log("Input value set via Type Assertion:", inputElement.value, "\n");
} else {
  console.log("Exercise 7 skipped: no input element found in DOM\n");
}

// Exercise 8: switch Statement with Complex Conditions
console.log("Exercise 8: switch Statement");
function getAction(role: string): string {
  switch (role) {
    case "admin":
      return "Manage users and settings";
    case "editor":
      return "Edit content";
    case "viewer":
      return "View content";
    case "guest":
      return "Limited access";
    default:
      return "Invalid role";
  }
}
console.log(getAction("admin"));
console.log(getAction("editor"));
console.log(getAction("viewer"));
console.log(getAction("guest"));
console.log(getAction("unknown"), "\n");

// Exercise 9: Function Overloading with Default Parameters
console.log("Exercise 9: Function Overloading");
function greet(): string;
function greet(name: string): string;
function greet(name?: string): string {
  if (name) return `Hello, ${name}!`;
  return "Hello, Guest!";
}
console.log(greet());
console.log(greet("Alice"));

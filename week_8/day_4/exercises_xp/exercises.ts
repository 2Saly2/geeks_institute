// Exercise 1: Intersection Types
type Person = { name: string; age: number; };
type Address = { street: string; city: string; };
type PersonWithAddress = Person & Address;
const user: PersonWithAddress = {
  name: "Nouhaila",
  age: 24,
  street: "Rue Hassan II",
  city: "Casablanca"
};

// Exercise 2: Type Guards with Union Types
function describeValue(value: number | string): string {
  if (typeof value === "number") return "This is a number";
  return "This is a string";
}
console.log(describeValue(10));
console.log(describeValue("Hello"));

// Exercise 3: Type Casting
let someValue: any = "Hello TypeScript";
let strValue: string = someValue as string;
console.log(strValue.toUpperCase());

// Exercise 4: Type Assertions with Union Types
function getFirstElement(arr: (number | string)[]): string {
  return arr[0] as string;
}
console.log(getFirstElement(["apple", 10]));
console.log(getFirstElement([20 as any, 30]));

// Exercise 5: Generic Constraints
function logLength<T extends { length: number }>(value: T): void {
  console.log(value.length);
}
logLength("Hello");
logLength([1, 2, 3]);

// Exercise 6: Intersection Types + Type Guards
type Job = { position: string; department: string; };
type Employee = Person & Job;
function describeEmployee(emp: Employee): string {
  if (emp.position === "Manager") {
    return `${emp.name} is a manager of ${emp.department}`;
  }
  if (emp.position === "Developer") {
    return `${emp.name} is a developer in ${emp.department}`;
  }
  return `${emp.name} works in ${emp.department}`;
}
const emp1: Employee = {
  name: "Omar",
  age: 30,
  position: "Manager",
  department: "IT"
};
console.log(describeEmployee(emp1));

// Exercise 7: Generic Constraints + Type Assertions
function formatInput<T extends { toString(): string }>(input: T): string {
  const strValue = input.toString() as string;
  return `Formatted: ${strValue}`;
}
console.log(formatInput(100));
console.log(formatInput("Hello World"));

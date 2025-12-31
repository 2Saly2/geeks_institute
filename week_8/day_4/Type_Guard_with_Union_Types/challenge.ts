
type User = {
  type: "user";
  name: string;
  age: number;
};

type Product = {
  type: "product";
  id: number;
  price: number;
};

type Order = {
  type: "order";
  orderId: string;
  amount: number;
};

// function handleData _ Type Guards
function handleData(data: (User | Product | Order)[]): string[] {
  return data.map(item => {
    if (item.type === "user") {
      return `👤 User: ${item.name}, Age: ${item.age}`;
    }
    if (item.type === "product") {
      return `🛍️ Product #${item.id}, Price: $${item.price}`;
    }
    if (item.type === "order") {
      return `📦 Order ${item.orderId} - Amount: $${item.amount}`;
    }
    return "⚠️ Unknown data type!";
  });
}


const mixedData: (User | Product | Order)[] = [
  { type: "user", name: "Sarah", age: 22 },
  { type: "product", id: 15, price: 199 },
  { type: "order", orderId: "ORD-88", amount: 350 },
];

console.log(handleData(mixedData));

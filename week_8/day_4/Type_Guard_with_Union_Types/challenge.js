// function handleData _ Type Guards
function handleData(data) {
    return data.map(function (item) {
        if (item.type === "user") {
            return "\uD83D\uDC64 User: ".concat(item.name, ", Age: ").concat(item.age);
        }
        if (item.type === "product") {
            return "\uD83D\uDECD\uFE0F Product #".concat(item.id, ", Price: $").concat(item.price);
        }
        if (item.type === "order") {
            return "\uD83D\uDCE6 Order ".concat(item.orderId, " - Amount: $").concat(item.amount);
        }
        return "⚠️ Unknown data type!";
    });
}
var mixedData = [
    { type: "user", name: "Sarah", age: 22 },
    { type: "product", id: 15, price: 199 },
    { type: "order", orderId: "ORD-88", amount: 350 },
];
console.log(handleData(mixedData));

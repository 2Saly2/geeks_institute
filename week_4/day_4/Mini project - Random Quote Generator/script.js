const quotes = [
  { id: 0, author: "Charles Lindbergh", quote: "Life is like a landscape. You live in the midst of it but can describe it only from the vantage point of distance." },
  { id: 1, author: "Albert Einstein", quote: "Imagination is more important than knowledge." },
  { id: 2, author: "Oscar Wilde", quote: "Be yourself; everyone else is already taken." },
  { id: 3, author: "Confucius", quote: "It does not matter how slowly you go as long as you do not stop." },
  { id: 4, author: "Maya Angelou", quote: "You will face many defeats in life, but never let yourself be defeated." }
];

let lastQuote = null;

document.getElementById("generate").addEventListener("click", () => {
  let randomIndex;
  do {
    randomIndex = Math.floor(Math.random() * quotes.length);
  } while (randomIndex === lastQuote);

  lastQuote = randomIndex;

  const { quote, author } = quotes[randomIndex];
  document.getElementById("quote-text").textContent = quote;
  document.getElementById("quote-author").textContent = author;
});

import express from "express";
import quizRouter from "./routes/quiz.js";

const app = express();
const PORT = 3000;

// Middleware
app.use(express.urlencoded({ extended: true }));

// Routes
app.use("/quiz", quizRouter);

// Server start
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

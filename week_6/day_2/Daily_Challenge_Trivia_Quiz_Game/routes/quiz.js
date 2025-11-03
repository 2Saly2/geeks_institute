import express from "express";
const router = express.Router();

const triviaQuestions = [
  { question: "What is the capital of France?", answer: "Paris" },
  { question: "Which planet is known as the Red Planet?", answer: "Mars" },
  { question: "What is the largest mammal in the world?", answer: "Blue whale" },
];


let currentQuestionIndex = 0;
let score = 0;

// 🟢 GET /quiz 
router.get("/", (req, res) => {
  const question = triviaQuestions[currentQuestionIndex];
  if (!question) {
    return res.redirect("/quiz/score");
  }

  res.send(`
    <h1>Trivia Quiz</h1>
    <form action="/quiz" method="POST">
      <p><strong>Question ${currentQuestionIndex + 1}:</strong> ${question.question}</p>
      <input type="text" name="answer" placeholder="Your answer" required />
      <button type="submit">Submit</button>
    </form>
  `);
});

// 🟡 POST /quiz
router.post("/", (req, res) => {
  const userAnswer = req.body.answer?.trim().toLowerCase();
  const correctAnswer = triviaQuestions[currentQuestionIndex].answer.toLowerCase();

  if (userAnswer === correctAnswer) {
    score++;
  }

  currentQuestionIndex++;

  if (currentQuestionIndex >= triviaQuestions.length) {
    return res.redirect("/quiz/score");
  }

  res.redirect("/quiz");
});

// 🔵 GET /quiz/score 
router.get("/score", (req, res) => {
  const totalQuestions = triviaQuestions.length;
  const finalScore = score;

  // Reset game for next player
  currentQuestionIndex = 0;
  score = 0;

  res.send(`
    <h1>Quiz Completed!</h1>
    <p>Your final score: ${finalScore} / ${totalQuestions}</p>
    <a href="/quiz">Play again</a>
  `);
});

export default router;

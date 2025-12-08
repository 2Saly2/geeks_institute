import ThemeSwitcher from "./components/ThemeSwitcher";
import CharacterCounter from "./components/CharacterCounter";

function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>React Exercises</h1>
      <h2>Exercise 1</h2>

      <ThemeSwitcher />

      <hr />

       <h2>Exercise 2</h2>
      <CharacterCounter />
    </div>
  );
}

export default App;

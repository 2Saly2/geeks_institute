import { useState, useContext } from "react";
import { TaskContext } from "./TaskContext";

export default function AddTask() {
  const { dispatch } = useContext(TaskContext);
  const [text, setText] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!text.trim()) return;

    dispatch({ type: "ADD_TASK", payload: text });
    setText("");
  };

  return (
    <form onSubmit={handleSubmit} className="add-task">
      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Add a task..."
      />
      <button type="submit">Add</button>
    </form>
  );
}

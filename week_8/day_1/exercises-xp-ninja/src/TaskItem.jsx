import { useContext } from "react";
import { TaskContext } from "./TaskContext";

export default function TaskItem({ task }) {
  const { dispatch } = useContext(TaskContext);

  return (
    <div className="task-item">
      <span
        onClick={() =>
          dispatch({ type: "TOGGLE_TASK", payload: task.id })
        }
        className={task.completed ? "done" : ""}
      >
        {task.text}
      </span>

      <button
        onClick={() =>
          dispatch({ type: "REMOVE_TASK", payload: task.id })
        }
        className="remove-btn"
      >
        ✖
      </button>
    </div>
  );
}

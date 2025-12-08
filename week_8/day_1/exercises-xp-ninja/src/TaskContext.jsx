import { createContext, useReducer } from "react";

export const TaskContext = createContext();

// -------- REDUCER FUNCTION --------
function taskReducer(state, action) {
  switch (action.type) {
    case "ADD_TASK":
      return [
        ...state,
        { id: crypto.randomUUID(), text: action.payload, completed: false },
      ];

    case "TOGGLE_TASK":
      return state.map((task) =>
        task.id === action.payload
          ? { ...task, completed: !task.completed }
          : task
      );

    case "REMOVE_TASK":
      return state.filter((task) => task.id !== action.payload);

    default:
      return state;
  }
}

// -------- PROVIDER --------
export function TaskProvider({ children }) {
  const [tasks, dispatch] = useReducer(taskReducer, []);

  return (
    <TaskContext.Provider value={{ tasks, dispatch }}>
      {children}
    </TaskContext.Provider>
  );
}

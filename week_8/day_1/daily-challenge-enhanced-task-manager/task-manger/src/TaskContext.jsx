import { createContext, useReducer } from "react";

export const TaskContext = createContext();

const initialState = {
  tasks: [],
  filter: "all" // all | completed | active
};

function taskReducer(state, action) {
  switch (action.type) {
    case "ADD_TASK":
      return {
        ...state,
        tasks: [
          ...state.tasks,
          { id: Date.now(), text: action.payload, completed: false }
        ]
      };

    case "REMOVE_TASK":
      return {
        ...state,
        tasks: state.tasks.filter(t => t.id !== action.payload)
      };

    case "TOGGLE_TASK":
      return {
        ...state,
        tasks: state.tasks.map(t =>
          t.id === action.payload ? { ...t, completed: !t.completed } : t
        )
      };

    case "EDIT_TASK":
      return {
        ...state,
        tasks: state.tasks.map(t =>
          t.id === action.payload.id
            ? { ...t, text: action.payload.text }
            : t
        )
      };

    case "SET_FILTER":
      return {
        ...state,
        filter: action.payload
      };

    default:
      return state;
  }
}

export function TaskProvider({ children }) {
  const [state, dispatch] = useReducer(taskReducer, initialState);

  return (
    <TaskContext.Provider value={{ state, dispatch }}>
      {children}
    </TaskContext.Provider>
  );
}

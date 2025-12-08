import { useContext, useRef, useState } from "react";
import { TaskContext } from "./TaskContext";

export default function App() {
  const { state, dispatch } = useContext(TaskContext);
  const inputRef = useRef();
  const [editingId, setEditingId] = useState(null);
  const editRef = useRef();

 
  const addTask = () => {
    const value = inputRef.current.value.trim();
    if (value !== "") {
      dispatch({ type: "ADD_TASK", payload: value });
      inputRef.current.value = "";
    }
  };

  
  const saveEdit = (id) => {
    const newText = editRef.current.value.trim();
    if (newText !== "") {
      dispatch({
        type: "EDIT_TASK",
        payload: { id, text: newText }
      });
      setEditingId(null);
    }
  };


  const filteredTasks = state.tasks.filter(t => {
    if (state.filter === "completed") return t.completed;
    if (state.filter === "active") return !t.completed;
    return true;
  });

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Task Manager</h1>

    
      <div style={styles.addBox}>
        <input ref={inputRef} placeholder="Add task..." style={styles.input} />
        <button onClick={addTask} style={styles.btn}>Add</button>
      </div>

      
      <div style={styles.filterBox}>
        <button onClick={() => dispatch({ type: "SET_FILTER", payload: "all" })}
                style={styles.btnSmall}>All</button>

        <button onClick={() => dispatch({ type: "SET_FILTER", payload: "completed" })}
                style={styles.btnSmall}>Completed</button>

        <button onClick={() => dispatch({ type: "SET_FILTER", payload: "active" })}
                style={styles.btnSmall}>Active</button>
      </div>

      
      <ul style={styles.list}>
        {filteredTasks.map(task => (
          <li key={task.id} style={styles.item}>
            
            {editingId === task.id ? (
              <>
                <input
                  ref={editRef}
                  defaultValue={task.text}
                  style={styles.editInput}
                />
                <button onClick={() => saveEdit(task.id)} style={styles.btnSmall}>Save</button>
              </>
            ) : (
              <>
                <span
                  style={{
                    ...styles.text,
                    textDecoration: task.completed ? "line-through" : "none"
                  }}
                  onClick={() => dispatch({ type: "TOGGLE_TASK", payload: task.id })}
                >
                  {task.text}
                </span>

                <button
                  onClick={() => setEditingId(task.id)}
                  style={styles.btnSmall}
                >
                  Edit
                </button>

                <button
                  onClick={() => dispatch({ type: "REMOVE_TASK", payload: task.id })}
                  style={styles.deleteBtn}
                >
                  X
                </button>
              </>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}


const styles = {
  container: {
    maxWidth: "600px",
    margin: "40px auto",
    padding: "20px",
    background: "#fff",
    borderRadius: "12px",
    boxShadow: "0 4px 10px rgba(0,0,0,0.1)",
    fontFamily: "Arial"
  },
  title: { textAlign: "center", marginBottom: "20px" },
  addBox: { display: "flex", gap: "10px" },
  input: { flex: 1, padding: "10px", borderRadius: "6px", border: "1px solid #ccc" },
  btn: { padding: "10px 20px", borderRadius: "6px", cursor: "pointer" },
  filterBox: { display: "flex", gap: "10px", margin: "20px 0" },
  btnSmall: { padding: "5px 10px", cursor: "pointer" },
  list: { listStyle: "none", padding: 0 },
  item: { display: "flex", alignItems: "center", gap: "10px", marginBottom: "10px" },
  text: { cursor: "pointer", flex: 1 },
  deleteBtn: { padding: "5px 10px", background: "red", color: "#fff", borderRadius: "6px", cursor: "pointer" },
  editInput: { padding: "6px", flex: 1 }
};

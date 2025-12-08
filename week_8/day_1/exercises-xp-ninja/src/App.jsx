import AddTask from "./AddTask";
import TaskList from "./TaskList";

export default function App() {
  return (
    <div className="container">
      <h1>Task Manager</h1>
      <AddTask />
      <TaskList />
    </div>
  );
}

import { useContext } from "react";
import { TaskContext } from "./TaskContext";
import TaskItem from "./TaskItem";

export default function TaskList() {
  const { tasks } = useContext(TaskContext);

  return (
    <div className="task-list">
      {tasks.length === 0 ? (
        <p className="empty">No tasks yet.</p>
      ) : (
        tasks.map((task) => <TaskItem key={task.id} task={task} />)
      )}
    </div>
  );
}

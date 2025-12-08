import { useRef, useState } from "react";

export default function CharacterCounter() {
  const inputRef = useRef();
  const [count, setCount] = useState(0);

  const handleInput = () => {
    const length = inputRef.current.value.length;
    setCount(length);
  };

  return (
    <div className="card">
      <h2 className="title">Character Counter</h2>

      <input
        ref={inputRef}
        onInput={handleInput}
        placeholder="Type something..."
        className="styled-input"
      />

      <p className="count">Characters: <span>{count}</span></p>
    </div>
  );
}

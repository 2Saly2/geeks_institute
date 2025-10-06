const gridContainer = document.getElementById("gridContainer");
const colorPicker = document.getElementById("colorPicker");
const eraserBtn = document.getElementById("eraserBtn");
const clearBtn = document.getElementById("clearBtn");
const saveBtn = document.getElementById("saveBtn");
const brushSize = document.getElementById("brushSize");
const gridSizeInput = document.getElementById("gridSize");
const gridSizeLabel = document.getElementById("gridSizeLabel");
const gridSizeLabel2 = document.getElementById("gridSizeLabel2");

let isDrawing = false;
let currentColor = colorPicker.value;
let isEraser = false;
let gridSize = parseInt(gridSizeInput.value);


function createGrid(size) {
  gridContainer.innerHTML = "";
  gridContainer.style.gridTemplateColumns = `repeat(${size}, 1fr)`;
  gridContainer.style.gridTemplateRows = `repeat(${size}, 1fr)`;
  for (let i = 0; i < size * size; i++) {
    const square = document.createElement("div");
    square.classList.add("border", "border-gray-200", "transition", "duration-100");
    square.style.backgroundColor = "#ffffff";
    gridContainer.appendChild(square);
  }
}
createGrid(gridSize);


gridContainer.addEventListener("mousedown", () => (isDrawing = true));
gridContainer.addEventListener("mouseup", () => (isDrawing = false));
gridContainer.addEventListener("mouseleave", () => (isDrawing = false));

gridContainer.addEventListener("mouseover", (e) => {
  if (isDrawing && e.target !== gridContainer) paintSquare(e.target);
});
gridContainer.addEventListener("mousedown", (e) => {
  if (e.target !== gridContainer) paintSquare(e.target);
});

function paintSquare(square) {
  const size = parseInt(brushSize.value);
  square.style.backgroundColor = isEraser ? "#ffffff" : currentColor;
}


colorPicker.addEventListener("input", (e) => {
  currentColor = e.target.value;
  isEraser = false;
  eraserBtn.classList.remove("bg-red-700");
});


eraserBtn.addEventListener("click", () => {
  isEraser = !isEraser;
  eraserBtn.classList.toggle("bg-red-700", isEraser);
});


clearBtn.addEventListener("click", () => {
  document.querySelectorAll("#gridContainer div").forEach((div) => {
    div.style.backgroundColor = "#ffffff";
  });
});


saveBtn.addEventListener("click", () => {
  html2canvas(gridContainer).then((canvas) => {
    const link = document.createElement("a");
    link.download = "my_drawing.png";
    link.href = canvas.toDataURL();
    link.click();
  });
});


gridSizeInput.addEventListener("input", (e) => {
  gridSize = parseInt(e.target.value);
  gridSizeLabel.textContent = gridSize;
  gridSizeLabel2.textContent = gridSize;
  createGrid(gridSize);
});

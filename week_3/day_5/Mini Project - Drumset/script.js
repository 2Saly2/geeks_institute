
window.addEventListener('keydown', function(e) {
  playSound(e.keyCode);
});


const buttons = document.querySelectorAll('.drum');
buttons.forEach(btn => {
  btn.addEventListener('click', function() {
    const key = this.getAttribute('data-key');
    playSound(key);
  });
});

function playSound(keyCode) {
  const audio = document.querySelector(`audio[data-key="${keyCode}"]`);
  const button = document.querySelector(`button[data-key="${keyCode}"]`);
  if (!audio) return; 

  audio.currentTime = 0; 
  audio.play();

  button.classList.add('playing');
  setTimeout(() => button.classList.remove('playing'), 200);
}

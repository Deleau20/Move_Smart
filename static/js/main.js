const textElement = document.getElementById('typing-text');
const text = "Nous vous rapprochons des unitées compétantes";
let index = 0;

function typeWriter() {
  if (index < text.length) {
    textElement.textContent += text.charAt(index);
    index++;
    setTimeout(typeWriter, 100); // Délai entre chaque caractère (100 millisecondes dans cet exemple)
  }
}

typeWriter();

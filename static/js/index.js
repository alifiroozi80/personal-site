var i = 0;
var txt = "I'm Ali, A Happy DevOps engineer :)";
var speed = 70;
$(document).ready(typeWriter());

function typeWriter() {
    if (i < txt.length) {
        document.getElementById("big-header").innerHTML += txt.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
    }
}
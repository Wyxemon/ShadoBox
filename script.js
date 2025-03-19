const input = document.getElementById("input");
const output = document.getElementById("output");

input.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        const userInput = input.value;
        const newLine = document.createElement("p");
        newLine.textContent = `hacking-user-tool > ${userInput}`;
        output.appendChild(newLine);
        input.value = ""; // Limpia el campo de entrada
        output.scrollTop = output.scrollHeight; // Mantén el scroll al final
    }
});

/*
window.onload = function() {
    document.getElementById('input').focus();
};
*/
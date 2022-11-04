const nome = document.getElementById("txt-nome");
const email = document.getElementById("txt-email");
const enviar = document.getElementById("bot");

function valida(event) {
    if (nome.value.trim() == "") {
        event.preventDefault()
        alert("O nome não pode ser vazio!")
    };
    if (email.value.trim() == "") {
        event.preventDefault()
        alert("O email não pode ser vazio!")
    };
};

bot.addEventListener("click", valida);
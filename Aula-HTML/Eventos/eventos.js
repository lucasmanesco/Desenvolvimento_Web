const div1 = document.querySelector("div.div1");
const bot = document.getElementById("button");
const bot2 = document.getElementById("button2");

bot.addEventListener("click", function(e) {
    div1.textContent = "Novo Texto Div";
    alert("Você clicou no botão nas coordenadas x=" + e.
    clientX + " y=" + e.clientY);
});

const txt = document.querySelector("#tx-nome");

function filtro(evt) {
    if (evt.key >= '0' && evt.key <= 9 ) {
        evt.preventDefault();
    }
};

function valida(event) {
    if (txt.value.trim() == "") {
        event.preventDefault();
    }
}

txt.addEventListener("keydown", filtro);

bot2.addEventListener("click", valida);
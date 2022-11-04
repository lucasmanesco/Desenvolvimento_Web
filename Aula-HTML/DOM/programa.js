const obj1 = document.getElementById("par2");

obj1.textContent = "Alterei o parárgrafo 2 no JS";
obj1.title = "Essa descrição foi definida no JS";
obj1.style.backgroundColor = "blue";

const obj2 = document.querySelector("div.comum");
obj2.textContent = "Inseri esse texto no JS";

const obj3 = document.createElement("p");
obj3.textContent = "JS é foda.";
obj3.style.color = "red";

const img = document.createElement("img");
img.src = "cachorro.webp";
img.alt = "Imagem de um doguinho";

obj2.appendChild(obj3);
obj2.appendChild(img);
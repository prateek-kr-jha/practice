const mainContainer = document.querySelector('.main');

const div = document.createElement('div');
div.setAttribute("id", "menu");
div.setAttribute("class", "black");
div.classList.add("block")

const heading = document.createElement("h2");
heading.textContent = "Menu";
div.appendChild(heading);
mainContainer.appendChild(div)

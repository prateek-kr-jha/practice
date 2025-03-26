const createMenuUI = () => {
  const mainContainer = document.querySelector('.main');
  const div = document.createElement('div');
  const a = document.createElement('a');
  a.setAttribute('href', './recipes/lasagna.html');
  a.textContent = 'Lasagna';
  div.classList.add("block")
  const heading = document.createElement("h2");
  heading.textContent = "Menu";
  div.appendChild(heading);
  div.appendChild(a);
  mainContainer.appendChild(div)
}

createMenuUI();
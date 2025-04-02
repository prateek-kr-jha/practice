const RECIPES = ['Lasagna', 'Ramen', 'Pasta', 'Butter Chicken']

const createMenuUI = () => {
  const mainContainer = document.querySelector('.main');

  const div = document.createElement('div');
  div.classList.add('block');
  const heading = document.createElement('h2');
  heading.textContent = 'Menu';
  div.appendChild(heading);
  const menuList = document.createElement('ul');
  
  RECIPES.forEach(recipe => {
    const li = document.createElement('li');
    const a = document.createElement('a');
    a.setAttribute('href', './recipes/lasagna.html');
    a.textContent = `${recipe}`;
    li.appendChild(a);
    menuList.appendChild(li);
    
  })
  div.appendChild(menuList);
  mainContainer.appendChild(div);
};

createMenuUI();

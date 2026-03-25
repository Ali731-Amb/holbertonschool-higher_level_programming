// 1. # = la cible, .my_list = classe CSS
const addButton = document.querySelector('#add_item');
const list = document.querySelector('.my_list');

// 2. Écouteur d'événement sur le bouton
addButton.addEventListener('click', function() {
    // 3. <li>
    const newItem = document.createElement('li');
    
    // 4. Ajout texte Item
    newItem.textContent = 'Item';
    
    // 5.newItem dans ul
    list.appendChild(newItem);
});
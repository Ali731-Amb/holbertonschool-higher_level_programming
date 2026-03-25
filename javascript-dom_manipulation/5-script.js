// 1. Sélection de l'élément cliquable et de la cible
const updateTrigger = document.querySelector('#update_header');
const headerElement = document.querySelector('header');

// 2. Écoute du clic
updateTrigger.addEventListener('click', function() {
    // 3.ajout new header !! 
    headerElement.textContent = 'New Header!!!';
});
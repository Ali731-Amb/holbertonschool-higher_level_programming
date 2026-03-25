// 1. Sélection des éléments
const toggleTrigger = document.querySelector('#toggle_header');
const headerElement = document.querySelector('header');

// 2. clic
toggleTrigger.addEventListener('click', function() {
    // 3. Si il est rouge, on enleve le rouge et on met le vert etc
    if (headerElement.classList.contains('red')) {
        headerElement.classList.remove('red');
        headerElement.classList.add('green');
    } else {
        headerElement.classList.remove('green');
        headerElement.classList.add('red');
    }
});
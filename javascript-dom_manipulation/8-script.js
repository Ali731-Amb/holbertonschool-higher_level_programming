// 1. wait for the document HTML soit complètement chargé
document.addEventListener('DOMContentLoaded', function() {
    const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
    const helloElement = document.querySelector('#hello');

    // 2. Appel à l'API
    fetch(url)
        .then(response => response.json())
        .then(data => {
            // 3. Extraction de la valeur "hello" et affichage
            helloElement.textContent = data.hello;
        })
        .catch(error => console.error('Erreur lors du fetch:', error));
});
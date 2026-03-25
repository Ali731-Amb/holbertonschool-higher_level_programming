// 1. Définition de l'URL de l'API
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// 2. fetch = demande a l'url et envoi une promise
fetch(url)
    .then(response => response.json()) // 3. Conversion de la réponse en JSON
    .then(data => {
        // 4. # = balise, prend que name dans les data 
        document.querySelector('#character').textContent = data.name;
    });
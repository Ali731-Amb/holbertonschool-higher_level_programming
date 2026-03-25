// 1. La ou on va chercher les info (URL)
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// 2. fetch = va voir l'url demande les infos et envoi une promise
fetch(url)
    .then(response => response.json()) // 3.la réponse en JSON
    .then(data => {
        // 4. # = balise character et data.name = va juste cherche le name
        document.querySelector('#character').textContent = data.name;
    });
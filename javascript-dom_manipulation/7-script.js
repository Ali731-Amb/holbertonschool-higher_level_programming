// 1. Définition de l'URL pour récupérer tous les films
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const listElement = document.querySelector('#list_movies');

// 2. Appel à l'API
fetch(url)
    .then(response => response.json()) // Conversion en objet JS
    .then(data => {
        // 3. L'API renvoie un objet contenant un tableau nommé "results"
        const movies = data.results;

        // 4. Boucle sur chaque film du tableau
        movies.forEach(movie => {
            // Création d'un nouvel élément de liste
            const li = document.createElement('li');
            
            // récupere le title 
            li.textContent = movie.title;
            
            // On l'ajoute à notre <ul>
            listElement.appendChild(li);
        });
    });
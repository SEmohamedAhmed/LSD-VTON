

document.addEventListener('DOMContentLoaded', function() {
    const container = document.querySelector('.container');
    const garments = [
        { id: '00057_00', price: 30, description: 'Oversize black T-shirt with short sleeves' },
        { id: '00127_00', price: 25, description: 'Slim fit black T-shirt with short sleeves' },
        { id: '00158_00', price: 35, description: 'Brown Blouse with long sleeves' },
        { id: '00260_00', price: 15, description: 'Pink shirt with short sleeves' },
        { id: '00278_00', price: 30, description: 'Slim fit black T-shirt with short sleeves' },
        { id: '00287_00', price: 20, description: 'Striped Turtleneck with black and white' },
        { id: '00397_00', price: 30, description: 'Plain red Henley shirt' },
        { id: '00460_00', price: 50, description: 'Polka dot Peplum with red and black' },
        { id: '01767_00', price: 25, description: 'Striped Henley shirt with black and white' },
        { id: '02094_00', price: 10, description: 'Black T-shirt with stripes in many colors' }
    ];

    // Create and append cards to the container
    garments.forEach(garment => {
        // const col = document.createElement('div');
        // col.className = 'col-6 col-lg-4';

        const card = document.createElement('div');
        card.classList.add('card');

        const cardInner = document.createElement('div');
        cardInner.classList.add('card-inner');

        // Create card front
        const cardFront = document.createElement('div');
        cardFront.classList.add('card-front');
        const img = document.createElement('img');
        img.src = `\\static\\clothes_samples\\${garment.id}.png`;
        img.alt = `Garment ${garment.id}`;
        cardFront.appendChild(img);

        // Create card back
        const cardBack = document.createElement('div');
        cardBack.classList.add('card-back');
        const pPrice = document.createElement('p');
        pPrice.textContent = `Price: $${garment.price}`;
        const pDescription = document.createElement('p');
        pDescription.textContent = `${garment.description}`;

        const button = document.createElement('button');
        button.classList.add('select-button');
        button.textContent = 'Try';
        button.dataset.src = `/static/clothes_samples/${garment.id}.png`;
        button.addEventListener('click', function() {
            localStorage.setItem('selectedImageSrc', button.dataset.src);
//            window.location.href = 'NewTryOn.html';
        });

        cardBack.appendChild(pDescription);
        cardBack.appendChild(pPrice);
        cardBack.appendChild(button);

        // Assemble card
        cardInner.appendChild(cardFront);
        cardInner.appendChild(cardBack);
        card.appendChild(cardInner);
        container.appendChild(card);
        // col.appendChild(card);
        // container.appendChild(col);
    });

    // go to the next page and keep the selected img saved 
    document.querySelectorAll('.select-button').forEach(button => {
        button.addEventListener('click', function() {
            console.log("Inside The Script");
            const imageSrc = this.getAttribute('data-src');
            const imageId = imageSrc.split('/')[3];
            console.log(imageId);
            localStorage.setItem('selectedImageSrc', imageSrc);
            localStorage.setItem('garmentId', imageId);
            console.log('garmentId is set using local storage = ');
            console.log(imageId);
            console.log(localStorage.getItem('garmentId'));
            window.location.href = '/model';
        });
    });
   


    // Load the selected image in the Model prediction page
    document.addEventListener('DOMContentLoaded', function() {
        console.log("Load Dom");
        const selectedImageSrc = localStorage.getItem('selectedImageSrc');
        if (selectedImageSrc) {
            document.getElementById('chosenGarment').src = selectedImageSrc;
        }
    });

    // Search functionality
    window.searchGarments = function() {
        const query = document.getElementById('search-bar').value.toLowerCase();
        const cards = document.querySelectorAll('.card');
        cards.forEach(card => {
            const cardBack = card.querySelector('.card-back');
            const description = cardBack.querySelector('p').textContent.toLowerCase();
            if (description.includes(query)) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    };
});

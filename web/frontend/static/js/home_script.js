// go to the next page and keep the selected img saved
document.querySelectorAll('.select-button').forEach(button => {
    button.addEventListener('click', function() {
        console.log("Inside The Script");
        const imageSrc = this.getAttribute('data-src');
        console.log(imageSrc);
        localStorage.setItem('selectedImageSrc', imageSrc);
        window.location.href = '/model';
    });
});

<!-- Load the selected image in the Model prediction page -->
document.addEventListener('DOMContentLoaded', function() {
    console.log("Load Dom");
    const selectedImageSrc = localStorage.getItem('selectedImageSrc');
    if (selectedImageSrc) {
        document.getElementById('chosenGarment').src = selectedImageSrc;
    }
});
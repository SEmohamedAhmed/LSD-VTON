

// Load the selected image in the Model prediction page
document.addEventListener('DOMContentLoaded', function() {
    console.log("Load Dom");
    const selectedImageSrc = localStorage.getItem('selectedImageSrc');
    if (selectedImageSrc) {
        document.getElementById('chosenGarment').src = selectedImageSrc;
    }

    const addedImage = document.getElementById('imageInput');
    addedImage.addEventListener('change',function(){     
     const addedImageId = document.getElementById('imageInput').files[0].name
      document.getElementById('user_picture').src = `\\static\\human_samples\\${addedImageId}`; //
      localStorage.setItem('personImage', addedImageId);
      console.log( "imageInput : ",document.getElementById('imageInput').files[0].name);
});

});


document.getElementById('tryOnButton').addEventListener('click', function() {
    console.log("After cliking on try on button in the Model page ");
    const fileInput = document.getElementById('imageInput');
    const UserFile = fileInput.files;

    const chosenGarment = document.getElementById('chosenGarment').src
    const splittedChosenGarmentURL = chosenGarment.split('/')
    const chosenGarmentID = splittedChosenGarmentURL[splittedChosenGarmentURL.length-1];    //Chosen garment id will look like eg. = 023.png

    if (UserFile.length > 0) {
        const firstFile = UserFile[0];
        choosenAvatarId= firstFile.name           //Chosen Avatar id will look like eg. = 023.png

        // Send data to the backend
        let tryon_path = 'here/will/put/tryon/result'
        fetch('http://localhost:80/tryon', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                choosenAvatarId: choosenAvatarId,
                chosenGarmentID: chosenGarmentID,
            }),
        })
        .then(response => response.text()) // Use response.text() to handle the response as text
        .then(data => {
            console.log(data); // This will log the string response
            // Here you can save the string result as needed
            // For example, saving to a variable, displaying it, or storing it in local storage
            tryon_path = data.replace(/"/g, ''); // Save the string result to a variable
            window.location.href = '/output';
            console.log("tryon_path:", tryon_path);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    } else {
        alert('Please select an image.');
        return;
    }
});


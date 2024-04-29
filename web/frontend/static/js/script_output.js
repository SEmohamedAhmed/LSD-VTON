document.addEventListener('DOMContentLoaded', function(){
    console.log('i am before cid&pid assigment\n');
    const cid = localStorage.getItem('garmentId');   // garment Id
    const pid = localStorage.getItem('personImage');   // Person Id
    console.log(cid);
    console.log(pid);
    document.getElementById('result').src = `\\static\\tryon_results\\tryon.png`;  //<-(dummy path){predicted image name}`
    document.getElementById('cloth').src = `\\static\\clothes_samples\\${cid}`;  //<-(dummy path){predicted image name}`
    document.getElementById('person').src = `\\static\\human_samples\\${pid}`;  //<-(dummy path){predicted image name}`

    // Have a great day Mody (:

});


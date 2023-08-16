let changeimg = document.getElementById("input-dropdown");
let myImg = document.getElementById("unit-icon");

function changeImage() {
    let index = changeimg.selectedIndex;
    myImg.src = changeimg.options[index].value;
}

changeImage();
changeimg.onchange = changeImage;

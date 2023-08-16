// 나라 스크랩 기능 (star)
let isStarFilled = false;

function toggleStarImage() {
  const starImage = document.querySelector(".star img");

  if (isStarFilled) {
    starImage.src = "./image/icon/star-line.svg";
  } else {
    starImage.src = "./image/icon/star-fill.svg";
  }

  isStarFilled = !isStarFilled;
}

// 품목 스크랩 기능 (heart)
let isHeartFilled = false;

function toggleHeartImage() {
  const heartImage = document.querySelector(".heart img");

  if (isHeartFilled) {
    heartImage.src = "../image/icon/heart-outline.svg";
  } else {
    heartImage.src = "../image/icon/heart.svg";
  }

  isHeartFilled = !isHeartFilled;
}

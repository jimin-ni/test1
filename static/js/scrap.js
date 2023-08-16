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

const modal_wrap = document.querySelector(".modal_wrap");
const modal_background = document.querySelector(".modal_background");
//모달창 보여주는 이벤트 리스너
document.querySelector("#modal_btn").addEventListener("click", () => {
  open();
}); //닫기 버튼눌러서 모달창 지우는 이벤트 리스너
document.querySelector(".modal_close").addEventListener("click", () => {
  close();
}); //모달창 바깥부분 눌러서 모달창 닫는 이벤트 리스너
window.addEventListener("click", (e) => {
  e.target === modal_background ? close() : false;
});
function close() {
  modal_wrap.classList.remove("show-modal");
  modal_background.classList.remove("show-modal");
}
function open() {
  modal_wrap.classList.add("show-modal");
  modal_background.classList.add("show-modal");
}

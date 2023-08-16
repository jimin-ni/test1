var mySwiper = new Swiper(".swiper-container", {
    // 슬라이드를 버튼으로 움직일 수 있습니다.
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },

    // 현재 페이지를 나타내는 점이 생깁니다. 클릭하면 이동합니다.
    pagination: {
        el: ".swiper-pagination",
        type: "bullets",
        clickable: "true",
    },

    // 현재 페이지를 나타내는 스크롤이 생깁니다. 클릭하면 이동합니다.
    // scrollbar: {
    //     el: ".swiper-scrollbar",
    //     draggable: true,
    // },

    // 3초마다 자동으로 슬라이드가 넘어갑니다. 1초 = 1000
    // autoplay: {
    //     delay: 3000,
    // },

    slidesPerView: 1, // 보여지는 슬라이드 수
    spaceBetween: 30, // 슬라이드 간의 거리(px 단위)
    loop: true, // 슬라이드 무한 반복
    // centeredSlides: true, // 다음 슬라이드의 모습이 50%만 보입니다.(중앙)
    slideToClickedSlide: true, // 해당 슬라이드 클릭시 슬라이드 위치로 이동
});

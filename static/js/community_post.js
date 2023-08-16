function publish() {
  var result = confirm("등록하시겠습니까?");
  if (result) {
    if (
      document.getElementById("page-title").value != "" &&
      document.getElementById("country-tags").value != "" &&
      document.getElementById("page-textarea").value != ""
    ) {
      alert("등록되었습니다.");
      window.location.replace("community.html");
    }
    if (document.getElementById("page-title").value == "") {
      alert("제목을 입력해 주세요.");
      return;
    }
    if (document.getElementById("page-textarea").value == "") {
      alert("내용을 입력해 주세요.");
      return;
    }
    if (document.getElementById("country-tags").value == "") {
      alert("태그를 입력해 주세요.");
      return;
    }
  } else {
    return;
  }
}

function cancel() {
  var back = confirm("글 작성을 취소하시겠습니까?");
  if (back) {
    alert("메인으로 돌아갑니다.");
    window.location.replace("community.html");
  } else {
    return;
  }
}

// 취소 버튼을 클릭했을 때 실행되는 함수
function cancelFileUpload() {
  // 파일 입력 필드의 값을 비움
  document.getElementById("fileInput").value = "";
}

// 취소 버튼 클릭 이벤트 리스너 연결
document
  .getElementById("cancelButton")
  .addEventListener("click", cancelFileUpload);

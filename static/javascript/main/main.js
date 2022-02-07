(() => {
  const stepElems = document.querySelectorAll(".step");
  const graphicElems = document.querySelectorAll(".graphic-item");
  let currentItem = graphicElems[0]; //현재 활성화된(visible 클래스가 붙은) .graphic-item을 지정
  let ioIndex;
  const test = document.querySelector(".abc");

  const io = new IntersectionObserver((entries, observer) => {
    // 문자열된 숫자를 숫자로 바꾸는 방법 : * 1 하기
    ioIndex = entries[0].target.dataset.index * 1;
  });

  for (let i = 0; i < stepElems.length; i++) {
    io.observe(stepElems[i]);
    stepElems[i].dataset.index = i; //index는 우리가 만든 index임 다른 이름으로 해도됨
    graphicElems[i].dataset.index = i;
  }

  function activate() {
    currentItem.classList.add("visible");
  }

  function inactivate() {
    currentItem.classList.remove("visible");
  }

  window.addEventListener("scroll", () => {
    let step;
    let boundingRect;

    for (let i = ioIndex - 1; i < ioIndex + 2; i++) {
      step = stepElems[i];
      if (!step) continue;
      boundingRect = step.getBoundingClientRect();

      if (
        boundingRect.top > window.innerHeight * 0.1 &&
        boundingRect.top < window.innerHeight * 0.8
      ) {
        inactivate();
        currentItem = graphicElems[step.dataset.index];
        activate();
      }

      //스크롤 끝일때
      if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        test.style.opacity = 0;
      }
      if (window.innerHeight + window.scrollY < document.body.offsetHeight) {
        test.style.opacity = 1;
      }
    }
  });

  window.addEventListener(
    "load",
    () => {
      setTimeout(() => scrollTo(0, 0), 100);
    },
    false
  );
  activate();
})();

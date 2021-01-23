// 전역변수 되도록이면 사용 x
(() => {

    // 3편 부터 다시 보기 에러는 안뜨는데 실행이 안됨
    // const actions = {
    //     birdFlies(key) {
    //         if (key) {
    //             // document.querySelector('[data-index="2"] .bird').style.transform = "translateX(110vw)";
    //             document.querySelector('[data-index="2"] .bird').style.transform = "translateX(${window.innerWidth}px)";
    //             console.log(window.innerWidth);
    //             console.log(key);
    //         } else {
    //             // document.querySelector('[data-index="2"] .bird').style.transform = "translateX(-100%)";
    //             document.querySelector('[data-index="2"] .bird').style.transform = "translateX(-100%)";
    //         }
    //     },
    //     birdFlies2(key) {
    //         if (key) {
    //             document.querySelector('[data-index="2"] .bird').style.transform = "translateX(${window.innerWidth}px, ${-window.innerHeight * 0.7}px)";
    //             // document.querySelector('[data-index="2"] .bird').style.transform = "translate("+window.innerWidth+")";
    //         } else {
    //             document.querySelector('[data-index="2"] .bird').style.transform = "translateX(-100%)";
    //         }
    //     }
    // };


    const stepElems = document.querySelectorAll('.step');
    const graphicElems = document.querySelectorAll(".graphic-item");
    let currentItem = graphicElems[0]; //현재 활성화된(visible 클래스가 붙은) .graphic-item을 지정
    let ioIndex;


    const io = new IntersectionObserver((entries, observer) => {
        // 문자열된 숫자를 숫자로 바꾸는 방법 : * 1 하기
        ioIndex = entries[0].target.dataset.index * 1;

    });

    // data - : html표준 뒤의 글은 자기 맘대로
    for (let i = 0; i < stepElems.length; i++) {
        io.observe(stepElems[i]);

        // 밑, 밑밑 같은 문장
        // stepElems[i].setAttribute('data-index',i);
        stepElems[i].dataset.index = i;
        graphicElems[i].dataset.index = i;
    }

    function activate() {
        currentItem.classList.add('visible');
        // if (action) {
        //     actions[action](true);
        // }
    }

    function inactivate() {
        currentItem.classList.remove('visible');
        // if (action) {
        //     actions[action](false);
        // }
    }

    window.addEventListener('scroll', () => {
        let step;
        let boundingRect;

        // for (let i = 0; i < stepElems.length; i++) {
        for (let i = ioIndex - 1; i < ioIndex + 2; i++) {
            step = stepElems[i];
            if (!step) continue;
            boundingRect = step.getBoundingClientRect();


            if ((boundingRect.top > window.innerHeight * 0.1) &&
                boundingRect.top < window.innerHeight * 0.3) {

                inactivate();
                currentItem = graphicElems[step.dataset.index];
                activate();
            }
        }
    });

    window.addEventListener('load', () => {
        setTimeout(() => scrollTo(0, 0),100);
    }, false);
    activate();


    // ---------modal---------
    // const modal_container = document.querySelector('.modal-container');
    // const info_input = document.querySelector('.info_input');
    // const close_btn = document.querySelector('.close-btn');

    // info_input.addEventListener('click', () => {
    //     modal_container.classList.add('show-modal');
    // })

    // close_btn.addEventListener('click', () => {
    //     modal_container.classList.remove('show-modal');
    // })

})();

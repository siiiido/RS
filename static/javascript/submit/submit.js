(() => {
    const ccx_li = document.querySelector(".ccx_li");
    const cco_li = document.querySelector(".cco_li");
    const anything_li = document.querySelector(".anything_li");
    const ccx_label = document.querySelector(".ccx_label");
    const cco_label = document.querySelector(".cco_label");
    const anything_label = document.querySelector(".anything_label");

    const left_label = document.querySelectorAll(".left_label");
    const right_label = document.querySelectorAll(".right_label");

    const read = document.querySelector(".read");

    const read_select = document.querySelector(".read_select");

    window.onload = () => {
        setTimeout(() => scrollTo(0, 0), 100);

        read_select.onchange = (e) => {
            if (e.target.value == "1") {
                read.readOnly = false;
                read.value = "";
            } else {
                read.value = e.target.value;
                read.readOnly = true;
            }
        }


    }


    window.addEventListener('click', (e) => {
        // console.log(e);
        if (e.target === ccx_label || e.target === ccx_li) {
            ccx_li.classList.add("sky");
            cco_li.classList.remove("sky")
            anything_li.classList.remove("sky")
        }
        else if (e.target === cco_label || e.target === cco_li) {
            cco_li.classList.add("sky");
            ccx_li.classList.remove("sky")
            anything_li.classList.remove("sky")
        }
        else if (e.target === anything_li || e.target === anything_label) {
            anything_li.classList.add("sky");
            ccx_li.classList.remove("sky")
            cco_li.classList.remove("sky")
        }

        for (let i = 0; i < 10; i++) {
            if (e.target === left_label[i]) {
                e.target.parentNode.nextElementSibling.classList.remove("sky");
                e.target.parentNode.classList.remove("black");
                e.target.parentNode.classList.add("sky");
                e.target.parentNode.nextElementSibling.classList.add("black");
            }
            else if (e.target === right_label[i]) {
                e.target.parentNode.classList.remove("black");
                e.target.parentNode.previousElementSibling.classList.remove("sky");
                e.target.parentNode.classList.add("sky");
                e.target.parentNode.previousElementSibling.classList.add("black");
            }
        }

    });



    window.addEventListener('submit', (e) => {

        // form 전체를 받아서 name으로 value를 찾자
        const form_field = document.querySelector('.form_field');

        // 대학교 value
        const option_value = form_field.html_university.options[form_field.html_university.selectedIndex].value;

        // 이미지
        const img_value = form_field.html_image.files[0];

        // 카카오 value
        const kakao_value = form_field.html_contact.value;
        // 대학교 선호
        const uni_radio = form_field.html_preference.value;

        const q1 = form_field.html_Q01.value;
        const q2 = form_field.html_Q02.value;
        const q3 = form_field.html_Q03.value;
        const q4 = form_field.html_Q04.value;
        const q5 = form_field.html_Q05.value;
        const q6 = form_field.html_Q06.value;
        const q7 = form_field.html_Q07.value;
        const q8 = form_field.html_Q08.value;
        const q9 = form_field.html_Q09.value;
        const q10 = form_field.html_Q10.value;



        if (option_value == '' || kakao_value == '' || img_value == null || uni_radio == '' ||
            q1 == '' || q2 == '' || q3 == '' || q4 == '' || q5 == '' || q6 == '' ||
            q7 == '' || q8 == '' || q9 == '' || q10 == '') {
            alert("모든 정보 입력 ㄱ");
            e.preventDefault();
        }

    });




})();




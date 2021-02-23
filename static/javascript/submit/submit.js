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



    const form = document.querySelector('.form_field');
    print(form);

    window.addEventListener('submit', (e) => {
        print("test submit");
        alert("test");
        e.target.preventDefault();
        print(form);

    });





    window.onload = function () {
        console.log("load start");


        const read_select = document.querySelector(".read_select");
        read_select.onchange = function (e) {
            if (e.target.value == "1") {
                read.readOnly = false;
                read.value = "";
                // print(read.value);
                // document.querySelector('.value_1').value = read.value;
                // read.innerHTML.value
            } else {
                read.value = e.target.value;
                read.readOnly = true;




            }
        }




        // ==================onload 했을때 이름,성별,연령대가 등록 x면 창 띄우기========================




    }



    window.addEventListener('click', (e) => {

        // console.log(e);
        if (e.target === ccx_label || e.target === ccx_li) {
            ccx_li.classList.add("clikc_radio_uni");
            cco_li.classList.remove("clikc_radio_uni")
            anything_li.classList.remove("clikc_radio_uni")
        }
        else if (e.target === cco_label || e.target === cco_li) {
            cco_li.classList.add("clikc_radio_uni");
            ccx_li.classList.remove("clikc_radio_uni")
            anything_li.classList.remove("clikc_radio_uni")
        }
        else if (e.target === anything_li || e.target === anything_label) {
            anything_li.classList.add("clikc_radio_uni");
            ccx_li.classList.remove("clikc_radio_uni")
            cco_li.classList.remove("clikc_radio_uni")
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



    console.log("add전");

    const form_field = document.querySelector('.form_field');

    form_field.addEventListener('submit', (e) => {
        const uni = form_field.html_university.value;

        console.log(uni);

        if(uni.value.length ===0 ){

            alert("누락");
            e.preventDefault();
            console.log('0');
        }

        if(uni.value ===""){
            console.log('null');
        }

    });








})();


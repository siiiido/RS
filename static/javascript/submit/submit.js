(() => {

    const ccx_li = document.querySelector(".ccx_li");
    const cco_li = document.querySelector(".cco_li");
    const anything_li = document.querySelector(".anything_li");

    const ccx_label = document.querySelector(".ccx_label");
    const cco_label = document.querySelector(".cco_label");
    const anything_label = document.querySelector(".anything_label");





    const left1 = document.querySelector(".left1");
    const right1 = document.querySelector(".right1");
    const left_label1 = document.querySelector(".left_label1");
    const right_label1 = document.querySelector(".right_label1");


    
    const left2 = document.querySelector(".left2");
    const right2 = document.querySelector(".right2");
    const left_label2 = document.querySelector(".left_label2");
    const right_label2 = document.querySelector(".right_label2");

    
    window.addEventListener('click', (e) => {
        console.log(e);
        if(e.target ===ccx_label || e.target ===ccx_li  ){
            ccx_li.classList.add("clikc_radio_uni");
            cco_li.classList.remove("clikc_radio_uni")
            anything_li.classList.remove("clikc_radio_uni")
        }
        else if(e.target ===cco_label || e.target ===cco_li  ){
            cco_li.classList.add("clikc_radio_uni");
            ccx_li.classList.remove("clikc_radio_uni")
            anything_li.classList.remove("clikc_radio_uni")
        }
        else if(e.target ===anything_li || e.target ===anything_label  ){
            anything_li.classList.add("clikc_radio_uni");
            ccx_li.classList.remove("clikc_radio_uni")
            cco_li.classList.remove("clikc_radio_uni")
        }

        


            // 어떻게 더 효율적으로?

        if (e.target === left_label1) {
            left1.classList.add("left_click_left");
            left1.classList.remove("right_click_left");
            right1.classList.add("left_click_right");
            right1.classList.remove("right_click_right");
        }
        else if(e.target === right_label1){
            left1.classList.remove("left_click_left");
            left1.classList.add("right_click_left");
            right1.classList.remove("left_click_right");
            right1.classList.add("right_click_right");
        }

        if (e.target === left_label2) {
            left2.classList.add("left_click_left");
            left2.classList.remove("right_click_left");
            right2.classList.add("left_click_right");
            right2.classList.remove("right_click_right");
        }
        else if(e.target === right_label2){
            left2.classList.remove("left_click_left");
            left2.classList.add("right_click_left");
            right2.classList.remove("left_click_right");
            right2.classList.add("right_click_right");
        }
    });




})();
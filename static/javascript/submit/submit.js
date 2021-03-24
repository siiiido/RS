(() => {
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
    };
  };

  const one = document.querySelector(".one_to_one");
  const oneLi = document.querySelector(".one_li");
  const two = document.querySelector(".two_to_two");
  const twoLi = document.querySelector(".two_li");
  const three = document.querySelector(".three_to_three");
  const threeLi = document.querySelector(".three_li");
  const four = document.querySelector(".four_to_four");
  const fourLi = document.querySelector(".four_li");

  const sendElem = document.querySelector(".send_content");
  const oneClick = document.querySelector(".clickOneToOne");
  const twoClick = document.querySelector(".clickTwoToTwo");
  const threeClick = document.querySelector(".clickThreeToThree");
  const fourClick = document.querySelector(".clickFourToFour");
  const click = document.querySelector(".click");
  function clickHandler(e) {
    if (e.target.value == one.value) {
      twoClick.style.display = "none";
      threeClick.style.display = "none";
      fourClick.style.display = "none";
      oneClick.style.display = "block";

      oneClick.innerHTML =
        " " +
        "<div class='uni_radio'>" +
        "      <label>매칭 상대방 학교</label>" +
        "      <div class='choose_uni_radio'>" +
        "        <li class='ccx_li'>" +
        "          <!-- input의 id와 label의 for가 같게해야 value가 넘어옴, id가 value보다 먼저 나와야함 -->" +
        "          <input id='ccx' name='html_preference' type='radio' value='DIFF' />" +
        "          <label for='ccx' class='ccx_label'>다른 학교</label>" +
        "        </li>" +
        "        <li class='cco_li'>" +
        "          <input id='cco' name='html_preference' type='radio' value='SAME' />" +
        "          <label for='cco' class='cco_label'>우리 학교</label>" +
        "        </li>" +
        "        <li class='anything_li'>" +
        "          <input" +
        "            id='anything'" +
        "            name='html_preference'" +
        "            type='radio'" +
        "            value='ALL'" +
        "          />" +
        "          <label for='anything' class='anything_label'>모든 학교</label>" +
        "        </li>" +
        "      </div>" +
        "    </div>" +
        "    <div class='whole_question'>" +
        "      <ul>" +
        "        <div class='radio_items'>" +
        "          <h5>{{quiz01.query}}</h5>" +
        "          <br />" +
        "          <div class='radio_li_con'>" +
        "            <li class='left'>" +
        "              <input id='q1_left' name='html_Q01' type='radio' value='left' />" +
        "              <label for='q1_left' class='left_label'>{{quiz01.selection1}}</label>" +
        "            </li>" +
        "            <li class='right'>" +
        "              <input id='q1_right' name='html_Q01' type='radio' value='right' />" +
        "              <label for='q1_right' class='right_label'>{{quiz01.selection2}}</label>" +
        "            </li>" +
        "          </div>" +
        "        </div>" +
        "        <div class='radio_items'>" +
        "          <h5>{{quiz02.query}}</h5>" +
        "          <br />" +
        "          <div class='radio_li_con'>" +
        "            <li class='left'>" +
        "              <input id='q2_left' name='html_Q02' type='radio' value='left' />" +
        "              <label for='q2_left' class='left_label'>{{quiz02.selection1}}</label>" +
        "            </li>" +
        "            <li class='right'>" +
        "              <input id='q2_right' name='html_Q02' type='radio' value='right' />" +
        "              <label for='q2_right' class='right_label'>{{quiz02.selection2}}</label>" +
        "            </li>" +
        "          </div>" +
        "        </div>" +
        "        <div class='radio_items'>" +
        "          <h5>{{quiz03.query}}</h5>" +
        "          <br />" +
        "          <div class='radio_li_con'>" +
        "            <li class='left'>" +
        "              <input id='q3_left' name='html_Q03' type='radio' value='left' />" +
        "              <label for='q3_left' class='left_label'>{{quiz03.selection1}}</label>" +
        "            </li>" +
        "            <li class='right'>" +
        "              <input id='q3_right' name='html_Q03' type='radio' value='right' />" +
        "              <label for='q3_right' class='right_label'>{{quiz03.selection2}}</label>" +
        "            </li>" +
        "          </div>" +
        "        </div>" +
        "        <div class='radio_items'>" +
        "          <h5>{{quiz04.query}}</h5>" +
        "          <br />" +
        "          <div class='radio_li_con'>" +
        "            <li class='left'>" +
        "              <input id='q4_left' name='html_Q04' type='radio' value='left' />" +
        "              <label for='q4_left' class='left_label'>{{quiz04.selection1}}</label>" +
        "            </li>" +
        "            <li class='right'>" +
        "              <input id='q4_right' name='html_Q04' type='radio' value='right' />" +
        "              <label for='q4_right' class='right_label'>{{quiz04.selection2}}</label>" +
        "            </li>" +
        "          </div>" +
        "        </div>" +
        "        <div class='radio_items'>" +
        "          <h5>{{quiz05.query}}</h5>" +
        "          <br />" +
        "          <div class='radio_li_con'>" +
        "            <li class='left'>" +
        "              <input id='q5_left' name='html_Q05' type='radio' value='left' />" +
        "              <label for='q5_left' class='left_label'>{{quiz05.selection1}}</label>" +
        "            </li>" +
        "            <li class='right'>" +
        "              <input id='q5_right' name='html_Q05' type='radio' value='right' />" +
        "              <label for='q5_right' class='right_label'>{{quiz05.selection2}}</label>" +
        "            </li>" +
        "          </div>" +
        "        </div>" +
        "        <div class='radio_items'>" +
        "          <h5>{{quiz06.query}}</h5>" +
        "          <br />" +
        "          <div class='radio_li_con'>" +
        "            <li class='left'>" +
        "              <input id='q6_left' name='html_Q06' type='radio' value='left' />" +
        "              <label for='q6_left' class='left_label'>{{quiz06.selection1}}</label>" +
        "            </li>" +
        "            <li class='right'>" +
        "              <input id='q6_right' name='html_Q06' type='radio' value='right' />" +
        "              <label for='q6_right' class='right_label'>{{quiz06.selection2}}</label>" +
        "            </li>" +
        "          </div>" +
        "        </div>" +
        "        <div class='radio_items'>" +
        "          <h5>{{quiz07.query}}</h5>" +
        "          <br />" +
        "          <div class='radio_li_con'>" +
        "            <li class='left'>" +
        "              <input id='q7_left' name='html_Q07' type='radio' value='left' />" +
        "              <label for='q7_left' class='left_label'>{{quiz07.selection1}}</label>" +
        "            </li>" +
        "            <li class='right'>" +
        "              <input id='q7_right' name='html_Q07' type='radio' value='right' />" +
        "              <label for='q7_right' class='right_label'>{{quiz07.selection2}}</label>" +
        "            </li>" +
        "          </div>" +
        "        </div>" +
        "        <div class='radio_items'>" +
        "          <h5>{{quiz08.query}}</h5>" +
        "          <br />" +
        "          <div class='radio_li_con'>" +
        "            <li class='left'>" +
        "              <input id='q8_left' name='html_Q08' type='radio' value='left' />" +
        "              <label for='q8_left' class='left_label'>{{quiz08.selection1}}</label>" +
        "            </li>" +
        "            <li class='right'>" +
        "              <input id='q8_right' name='html_Q08' type='radio' value='right' />" +
        "              <label for='q8_right' class='right_label'>{{quiz08.selection2}}</label>" +
        "            </li>" +
        "          </div>" +
        "        </div>" +
        "        <div class='radio_items'>" +
        "          <h5>{{quiz09.query}}</h5>" +
        "          <br />" +
        "          <div class='radio_li_con'>" +
        "            <li class='left'>" +
        "              <input id='q9_left' name='html_Q09' type='radio' value='left' />" +
        "              <label for='q9_left' class='left_label'>{{quiz09.selection1}}</label>" +
        "            </li>" +
        "            <li class='right'>" +
        "              <input id='q9_right' name='html_Q09' type='radio' value='right' />" +
        "              <label for='q9_right' class='right_label'>{{quiz09.selection2}}</label>" +
        "            </li>" +
        "          </div>" +
        "        </div>" +
        "        <div class='radio_items'>" +
        "          <h5>{{quiz10.query}}</h5>" +
        "          <br />" +
        "          <div class='radio_li_con'>" +
        "            <li class='left'>" +
        "              <input id='q10_left' name='html_Q10' type='radio' value='left' />" +
        "              <label for='q10_left' class='left_label'>{{quiz10.selection1}}</label>" +
        "            </li>" +
        "            <li class='right'>" +
        "              <input" +
        "                id='q10_right'" +
        "                name='html_Q10'" +
        "                type='radio'" +
        "                value='right'" +
        "              />" +
        "              <label for='q10_right' class='right_label'>{{quiz10.selection2}}</label>" +
        "            </li>" +
        "          </div>" +
        "        </div>" +
        "      </ul>" +
        "    </div>";

      twoLi.classList.remove("group_color");
      threeLi.classList.remove("group_color");
      fourLi.classList.remove("group_color");
      oneLi.classList.add("group_color");
    } else if (e.target.value == two.value) {
      threeClick.style.display = "none";
      fourClick.style.display = "none";
      oneClick.style.display = "none";
      twoClick.style.display = "block";

      twoClick.innerHTML =
        "" +
        "      <p class='group_ment'>2:2 매칭은 한 명의 카카오톡ID만 등록합니다</p>" +
        "          <p class='group_ment'>" +
        "            매칭 상대 역시 같은 그룹 매칭을 신청한 상대입니다" +
        "          </p>" +
        "          <!-- <p class='group_ment'>신청 이후 다른 매칭으로 중복 신청은 안됩니다</p> -->" +
        "          <p class='group_ment'>자세한 사항은 <a href='https://pf.kakao.com/_ExmxkkK/65944735'>새봄 페이지</a>를 참고해주세요!</p>" +
        "          <br />";

      threeLi.classList.remove("group_color");
      fourLi.classList.remove("group_color");
      oneLi.classList.remove("group_color");
      twoLi.classList.add("group_color");
    } else if (e.target.value == three.value) {
      twoClick.style.display = "none";
      fourClick.style.display = "none";
      oneClick.style.display = "none";
      threeClick.style.display = "block";

      threeClick.innerHTML = 
      "" +
      "      <p class='group_ment'>3:3 매칭은 한 명의 카카오톡ID만 등록합니다</p>" +
      "          <p class='group_ment'>" +
      "            매칭 상대 역시 같은 그룹 매칭을 신청한 상대입니다" +
      "          </p>" +
      "          <!-- <p class='group_ment'>신청 이후 다른 매칭으로 중복 신청은 안됩니다</p> -->" +
      "          <p class='group_ment'>자세한 사항은 <a href='https://pf.kakao.com/_ExmxkkK/65944735'>새봄 페이지</a>를 참고해주세요!</p>" +
      "          <br />";

      twoLi.classList.remove("group_color");
      fourLi.classList.remove("group_color");
      oneLi.classList.remove("group_color");
      threeLi.classList.add("group_color");
    } else if (e.target.value == four.value) {
      twoClick.style.display = "none";
      threeClick.style.display = "none";
      oneClick.style.display = "none";
      fourClick.style.display = "block";

      fourClick.innerHTML = 
      "" +
      "      <p class='group_ment'>4:4 매칭은 한 명의 카카오톡ID만 등록합니다</p>" +
      "          <p class='group_ment'>" +
      "            매칭 상대 역시 같은 그룹 매칭을 신청한 상대입니다" +
      "          </p>" +
      "          <!-- <p class='group_ment'>신청 이후 다른 매칭으로 중복 신청은 안됩니다</p> -->" +
      "          <p class='group_ment'>자세한 사항은 <a href='https://pf.kakao.com/_ExmxkkK/65944735'>새봄 페이지</a>를 참고해주세요!</p>" +
      "          <br />";

      twoLi.classList.remove("group_color");
      threeLi.classList.remove("group_color");
      oneLi.classList.remove("group_color");
      fourLi.classList.add("group_color");
    }

    const ccx_label = document.querySelector(".ccx_label");
    const ccx_li = document.querySelector(".ccx_li");
    const cco_li = document.querySelector(".cco_li");
    const anything_li = document.querySelector(".anything_li");
    const cco_label = document.querySelector(".cco_label");
    const anything_label = document.querySelector(".anything_label");

    // console.log(e);
    if (e.target === ccx_label || e.target === ccx_li) {
      ccx_li.classList.add("sky");
      cco_li.classList.remove("sky");
      anything_li.classList.remove("sky");
    } else if (e.target === cco_label || e.target === cco_li) {
      cco_li.classList.add("sky");
      ccx_li.classList.remove("sky");
      anything_li.classList.remove("sky");
    } else if (e.target === anything_li || e.target === anything_label) {
      anything_li.classList.add("sky");
      ccx_li.classList.remove("sky");
      cco_li.classList.remove("sky");
    }

    const left_label = document.querySelectorAll(".left_label");
    const right_label = document.querySelectorAll(".right_label");
    for (let i = 0; i < 10; i++) {
      if (e.target === left_label[i]) {
        e.target.parentNode.nextElementSibling.classList.remove("sky");
        e.target.parentNode.classList.remove("black");
        e.target.parentNode.classList.add("sky");
        e.target.parentNode.nextElementSibling.classList.add("black");
      } else if (e.target === right_label[i]) {
        e.target.parentNode.classList.remove("black");
        e.target.parentNode.previousElementSibling.classList.remove("sky");
        e.target.parentNode.classList.add("sky");
        e.target.parentNode.previousElementSibling.classList.add("black");
      }
    }
  }

  sendElem.addEventListener("click", clickHandler);

  window.addEventListener("submit", (e) => {
    // form 전체를 받아서 name으로 value를 찾자
    const form_field = document.querySelector(".form_field");

    //몇 명 매칭하는지
    const matchingGroup = form_field.html_option.value;

    // 대학교 value
    const option_value =
      form_field.html_university.options[
        form_field.html_university.selectedIndex
      ].value;

    // 이미지
    const img_value = form_field.html_image.files[0];

    // 카카오 value
    const kakao_value = form_field.html_contact.value;

    if (one.value == matchingGroup) {
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

      if (option_value == "") {
        alert("대학교를 선택해 주세요.");
        e.preventDefault();
      }
      if (kakao_value == "") {
        alert("카카오톡ID를 입력해 주세요");
        e.preventDefault();
      }
      if (img_value == null) {
        alert("학생증을 인증해 주세요");
        e.preventDefault();
      }
      if (uni_radio == "") {
        alert("선호 학교를 선택해 주세요");
        e.preventDefault();
      }
      if (q1 == "") {
        alert("첫번째 질문을 선택해 주세요");
        e.preventDefault();
      }
      if (q2 == "") {
        alert("두번째 질문을 선택해 주세요");
        e.preventDefault();
      }
      if (q3 == "") {
        alert("세번째 질문을 선택해 주세요");
        e.preventDefault();
      }
      if (q4 == "") {
        alert("네번째 질문을 선택해 주세요");
        e.preventDefault();
      }
      if (q5 == "") {
        alert("다섯번째 질문을 선택해 주세요");
        e.preventDefault();
      }
      if (q6 == "") {
        alert("여섯번째 질문을 선택해 주세요");
        e.preventDefault();
      }
      if (q7 == "") {
        alert("일곱번째 질문을 선택해 주세요");
        e.preventDefault();
      }
      if (q8 == "") {
        alert("여덟번째 질문을 선택해 주세요");
        e.preventDefault();
      }
      if (q9 == "") {
        alert("아홉번째 질문을 선택해 주세요");
        e.preventDefault();
      }
      if (q10 == "") {
        alert("열번째 질문을 선택해 주세요");
        e.preventDefault();
      }
    } else if (
      matchingGroup == two.value ||
      matchingGroup == three.value ||
      matchingGroup == four.value
    ) {
      if (option_value == "") {
        alert("대학교를 선택해 주세요.");
        e.preventDefault();
      }
      if (kakao_value == "") {
        alert("카카오톡ID를 입력해 주세요");
        e.preventDefault();
      }
      if (img_value == null) {
        alert("학생증을 인증해 주세요");
        e.preventDefault();
      }
    }
  });
})();

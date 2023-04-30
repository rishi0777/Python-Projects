///////////////////////////////////////////////////////////////////////////////////// GLOABAL VARIABLES
const timer_label = document.querySelector(".label");
const btn_alert = document.querySelector("#btn_alert");
const btn_confirm_continue = document.querySelector("#btn_confirm1");
const btn_confirm_abort = document.querySelector("#btn_confirm2");
const form = document.querySelector(".form1");
const btn_result = document.querySelector(".btn_result");
const text_area = document.querySelector("#exampleFormControlTextarea1");

var flag_timer = 0;
var already_submitted = false;
var flag1 = false;
let minutes = 1;
let seconds = 59;
let time = minutes * 60 + seconds;

//jab user back aur forward button ka use karke is page par aayega tab ye kaaam hoga
if (performance.navigation.type == 2) {
    already_submitted = true;
    main_flag_test = 0;
    text_area.blur();
    flag1 = true;
    btn_result.style.display = "none";
    text_area.style.value = "";
    timer_label.style.color = 'red';
    timer_label.innerHTML = '0 : 00';
    alert.render("", "DO NOT USE BACK BUTTONS TO ATTEMPT THE TEST", "REDIRECTING TO HOME PAGE IN 3 SECONDS", 'REDIRECT NOW');
    btn_alert.addEventListener('click', click_btn_alert);
    function click_btn_alert() {
        alert.ok("/")
    }
    setTimeout(function () {
        window.open("/", "_self")
    }, 3000);

}

check();
////////////////////////////////////////////////////////////////////////////////////////////main_flag_condition agar ek baar is page par aa chuke ho to phirse nahi aa skte jab tak test attempt na kar lo
function check() {
    if (main_flag_test == 1 && already_submitted == false) {

        ///////////////////////////////////////////////////////////////////////////////////// BROWSER BACK BUTTON
        function makeid(length) {
            var result = '';
            var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
            var charactersLength = characters.length;
            for (var i = 0; i < length; i++) {
                result += characters.charAt(Math.floor(Math.random() * charactersLength));

            }
            return result;
        }
        window.onpopstate = function (event) {
            if (flag1 == false) {
                history.pushState({ id }, `Selected: ${id}`, `/load=${id}`);
                alert.render("", "GO FAST TEST GOING ON", "ACTION NOT ALLOWED DURING THE TEST", "CONTINUE");
                flag1 = true
                btn_alert.addEventListener('click', click_btn_alert);
                function click_btn_alert() {
                    alert.remove_alert();
                    flag1 = false;
                };
            }
            else {

            }
        }

        id = makeid(10);
        history.pushState({ id }, `Selected: ${id}`, `./load=${id}`)

        if (minutes >= 0 && seconds != 0) {
            var timer_interval = setInterval(timer, 1000);
        }
        //////////////////////////////////////////////////////////////////////////////////////////////////// TIMER
        function timer() {
            if (flag1 == false) {
                minutes = Math.floor(time / 60);
                seconds = time % 60;
                seconds = seconds < 10 ? '0' + seconds : seconds;
                timer_label.innerHTML = minutes + ' : ' + seconds;
                time--;
                if (minutes == 0 && seconds < 10 && flag_timer == 0) {
                    timer_label.style.color = 'red';
                    flag_timer = 1;
                }
                if (minutes <= 0 && seconds <= 0) {
                    text_area.blur();
                    flag1 = true;
                    clearInterval(timer_interval);
                    seconds = 0;
                    minutes = 0;
                    btn_result.style.display = "none";
                    alert.render("", "GO FAST TIME UP", "REDIRECTING TO RESULT PAGE IN 3 SECONDS", 'RESULT');
                    btn_alert.addEventListener('click', function () {
                        form.submit();
                        alert.remove_alert();
                        text_area.blur();
                        flag1 = true;
                        btn_result.style.display = "none";
                        clearInterval(timer_interval);
                        timer_label.innerHTML = '0 : 00';
                        seconds = 0;
                        minutes = 0;
                    });

                    setTimeout(function () {
                        form.submit();
                        alert.remove_alert();
                        text_area.blur();
                        flag1 = true;
                        btn_result.style.display = "none";
                        clearInterval(timer_interval);
                        timer_label.innerHTML = '0 : 00';
                        seconds = 0;
                        minutes = 0;
                    }, 3000);
                }
            }
        }


        ////////////////////////////////////////////////////////////////////////////////////////////WHEN RESULT BUTTON CLICKED
        btn_result.addEventListener('click', call_alert);

        function call_alert() {
            flag1 = true;
            already_submitted = true;
            confirm.render("", "GO FAST TEST NOT COMLPETED", "DO YOU STILL WANT TO ABORT THE TEST", 'CONTINUE', 'ABORT');

            btn_confirm_continue.addEventListener('click', function () {
                confirm.continue();
                flag1 = false;
            });

            btn_confirm_abort.addEventListener('click', function () {
                text_area.blur();
                flag1 = true;
                btn_result.style.display = "none";
                clearInterval(timer_interval);
                timer_label.innerHTML = '0 : 00';
                seconds = 0;
                minutes = 0;
                confirm.continue();
                form.submit();
            });
        }

    }

    else {
        alert.render("", "DO NOT USE BACK BUTTONS TO ATTEMPT THE TEST", "YOU WILL BE REDIRECTED TO HOME PAGE IN 2 SECONDS", 'OK');
        already_submitted = true;
        main_flag_test = 0;
        flag1 = true;
        text_area.blur();
        btn_result.style.display = "none";
        text_area.style.value = "";
        timer_label.style.color = 'red';
        timer_label.innerHTML = '0 : 00';
        btn_alert.addEventListener('click', function () {
            open('/', '_parent').close();
        });

        setTimeout(function () {
            open('/', '_parent').close();
        }, 3000);
    }
}
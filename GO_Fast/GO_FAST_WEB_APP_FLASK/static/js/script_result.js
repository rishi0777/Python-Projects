//////////////////////////////////////////////////////////////////////////// GLOBAL VARIABLES
const btn_confirm_y = document.querySelector("#btn_confirm1");
const btn_confirm_n = document.querySelector("#btn_confirm2");
const btn_dwn_cert = document.querySelector("#dwn_cert");
const anim_trophy = document.querySelector("#anim_trophy");
const anim_done = document.querySelector("#anim_done");

const btn_head_home = document.querySelector("#head_home");
const btn_head_register = document.querySelector("#head_register");
const btn_head_about = document.querySelector("#head_about");

const btn_foot_mail = document.querySelector("#foot_mail");
const btn_foot_git = document.querySelector("#foot_git");
const btn_foot_linkedin = document.querySelector("#foot_linkedin");
const btn_foot_about = document.querySelector("#foot_about");

const test_result_label = document.querySelector("#test_result_label");
const main_heading = document.querySelector("#main_heading");
const eligible_label = document.querySelector("#e_label");
const btn_gen_cert = document.querySelector("#btn_gen_cert");
const improve_label = document.querySelector("#sh_improve");
const good_label = document.querySelector("#sh_good");

var flag_result = 1;
var check_accuracy = 40;
var check_speed = 5;


//jab user back aur forward button ka use karke is page par aayega tab ye kaaam hoga
if (performance.navigation.type == 2) {
    main_flag_result = 0;
    flag_result = 0;
    accuracy = 0;
    speed = 0;
    eligible_cert.style.display = "none";
    btn_dwn_cert.display = "none";

    alert.render("", "NOT VALID YOU HAVE ALREADY SEEN YOUR RESULT", "REDIRECTING TO HOME PAGE IN 3 SECONDS", 'REDIRECT NOW');
    btn_alert.addEventListener('click', click_btn_alert);
    function click_btn_alert() {
        alert.ok("/")
    }
    setTimeout(timeout, 3000);
    function timeout() {
        window.open("/", "_self")
    }

}

//////////////////////////////////////////////////////////////////////////////just before unloading the page
window.addEventListener("unload", function (event) {
    main_flag_result = 0;
    flag_result = 0;
    accuracy = 0;
    speed = 0;
    
});



////////////////////////////////////////////////////////////////////////////////////calling check func
check();

//////////////////////////////////////////////////////////////////////////////////////////////////////main_function
function check() {
    if (flag_result == 1) {

        //////////////////////////////////////////////////////////////////////////// CODE FOR BACK BUTTON
        function makeid(length) {
            var result = '';
            var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
            var charactersLength = characters.length;
            for (var i = 0; i < length; i++) {
                result += characters.charAt(Math.floor(Math.random() * charactersLength));

            }
            return result;
        }
        id = makeid(10);
        history.pushState({ id }, `Selected: ${id}`, `./result=${id}`)

        window.onpopstate = function (event) {
            history.pushState({ id }, `Selected: ${id}`, `./result=${id}`)
            if (accuracy >= check_accuracy && speed >= check_speed) {
                confirm.render("", "ELIGIBLE FOR DOWNLOADING CERTIFICATE", "DO YOU STILL WANT TO GO BACK", "NO", "YES");
                btn_confirm_y.addEventListener('click', function () {
                    confirm.continue();
                });
                btn_confirm_n.addEventListener('click', function () {
                    confirm.abort('/')
                });
            }
            else {
                confirm.render("", "GO FAST WARNING", "ALL YOUR DATA WILL BE LOST<br>DO YOU STILL WANT TO GO BACK", "NO LET ME SEE", "YES");
                btn_confirm_y.addEventListener('click', function () {
                    confirm.continue();
                });
                btn_confirm_n.addEventListener('click', function () {
                    confirm.abort('/')
                });
            }
        }

        //////////////////////////////////////////////////////////////////////////// CODE FOR DISPLAYING ANIMATION AND FORM
        if (accuracy >= check_accuracy && speed >= check_speed) {
            anim_trophy.style.display = "flex";
            eligible_label.style.display = "flex";
            good_label.style.display = "flex";
            btn_gen_cert.style.display = "flex";
            main_heading.style.color="#ffdd40";
            test_result_label.style.color="#ffdd40";
        }
        else {
            main_heading.style.color="#f35762";
            test_result_label.style.color="#f35762";
            anim_done.style.display = "flex";
            improve_label.style.display = "flex";
        }

        //////////////////////////////////////////////////////////////////////////// CODE FOR DIFFERENT BUTTONS
        btn_gen_cert.addEventListener("click", function () {
            if (flag_result == 1) {
                window.open('/submit/'+main_flag_test+'/cerificate/', "_self")
            }
        });

        
        btn_head_home.addEventListener('click', accuracy >= check_accuracy && speed >= check_speed ? call_alert_home : call_home);
        btn_head_register.addEventListener('click', accuracy >= check_accuracy && speed >= check_speed ? call_alert_register : call_register);
        btn_head_about.addEventListener('click', accuracy >= check_accuracy && speed >= check_speed ? call_alert_about : call_about);
        btn_foot_mail.addEventListener('click', accuracy >= check_accuracy && speed >= check_speed ? call_alert_mail : call_mail);
        btn_foot_linkedin.addEventListener('click', accuracy >= check_accuracy && speed >= check_speed ? call_alert_linkedin : call_linkedin);
        btn_foot_git.addEventListener('click', accuracy >= check_accuracy && speed >= check_speed ? call_alert_git : call_git);
        btn_foot_about.addEventListener('click', accuracy >= check_accuracy && speed >= check_speed ? call_alert_about : call_about);


        function call_alert_home() {
            confirm.render("", "GO FAST WARNING", "YOU ARE ELIGIBLE TO DOWNLOAD THE CERIIFICATE<br>DO YOU STILL WANT TO LEAVE", 'NO', 'LEAVE');
            btn_confirm_y.addEventListener('click', function () {
                confirm.continue();
            });
            btn_confirm_n.addEventListener('click', function () {
                confirm.abort('/');
            });
        }
        function call_home() {
            window.open('/', "_self")
        }

        function call_alert_register() {
            confirm.render("", "GO FAST WARNING", "YOU ARE ELIGIBLE TO DOWNLOAD THE CERIIFICATE<br>DO YOU STILL WANT TO LEAVE", 'NO', 'LEAVE');
            btn_confirm_y.addEventListener('click', function () {
                confirm.continue();
            });
            btn_confirm_n.addEventListener('click', function () {
                confirm.abort('/register');
            });
        }
        function call_register() {
            window.open('/register', "_self")
        }

        function call_alert_about() {
            confirm.render("", "GO FAST WARNING", "YOU ARE ELIGIBLE TO DOWNLOAD THE CERIIFICATE<br>DO YOU STILL WANT TO LEAVE", 'NO', 'LEAVE');
            btn_confirm_y.addEventListener('click', function () {
                confirm.continue();
            });
            btn_confirm_n.addEventListener('click', function () {
                confirm.abort('https://rishimishra.me');
            });
        }
        function call_about() {
            window.open('https://rishimishra.me', "_self")
        }

        function call_alert_mail() {
            confirm.render("", "GO FAST WARNING", "YOU ARE ELIGIBLE TO DOWNLOAD THE CERIIFICATE<br>DO YOU STILL WANT TO LEAVE", 'NO', 'LEAVE');
            btn_confirm_y.addEventListener('click', function () {
                confirm.continue();
            });
            btn_confirm_n.addEventListener('click', function () {
                confirm.abort('https://www.rishimishra.me/#contact');
            });
        }
        function call_mail() {
            window.open('https://www.rishimishra.me/#contact', "_self")
        }

        function call_alert_linkedin() {
            confirm.render("", "GO FAST WARNING", "YOU ARE ELIGIBLE TO DOWNLOAD THE CERIIFICATE<br>DO YOU STILL WANT TO LEAVE", 'NO', 'LEAVE');
            btn_confirm_y.addEventListener('click', function () {
                confirm.continue();
            });
            btn_confirm_n.addEventListener('click', function () {
                confirm.abort('https://www.linkedin.com/in/rishi-mishra/');
            });
        }
        function call_linkedin() {
            window.open('https://www.linkedin.com/in/rishi-mishra/', "_self")
        }

        function call_alert_git() {
            confirm.render("", "GO FAST WARNING", "YOU ARE ELIGIBLE TO DOWNLOAD THE CERIIFICATE<br>DO YOU STILL WANT TO LEAVE", 'NO', 'LEAVE');
            btn_confirm_y.addEventListener('click', function () {
                confirm.continue();
            });
            btn_confirm_n.addEventListener('click', function () {
                confirm.abort('https://github.com/rishi-777');
            });
        }
        function call_git() {
            window.open('https://github.com/rishi-777', "_self")
        }

    }
}



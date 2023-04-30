///////////////////////////////////////////////////////////////////////////////// GLOBAL VARIABLES
const btn_alert = document.querySelector("#btn_alert");
const btn_confirm_y = document.querySelector("#btn_confirm1");
const btn_confirm_n = document.querySelector("#btn_confirm2");

const btn_head_home = document.querySelector("#head_home");
const btn_head_register = document.querySelector("#head_register");
const btn_head_about = document.querySelector("#head_about");

const btn_foot_mail = document.querySelector("#foot_mail");
const btn_foot_git = document.querySelector("#foot_git");
const btn_foot_linkedin = document.querySelector("#foot_linkedin");
const btn_foot_about = document.querySelector("#foot_about");

const btn_gen_cert = document.querySelector("#generate_certificate");

var main_flag_cert = 1;
var flag_cert = 1;

///////////////////////////////////////////////////////////////////////////////////// Creating cert










//jab user back aur forward button ka use karke is page par aayega tab ye kaaam hoga
if (performance.navigation.type == 2) {
    main_flag_cert = 0;
    flag_cert = 0;
    btn_gen_cert.style.display = "none";

    alert.render("", "NOT ELIGIBLE", "REDIRECTING TO HOME PAGE IN 3 SECONDS", 'REDIRECT NOW');
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
    main_flag_cert = 0;
    flag_cert = 0;
    btn_gen_cert.style.display = "none";
});

check();
function check() {
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
    id = makeid(10);
    history.pushState({ id }, `Selected: ${id}`, `load/result/cert=${id}`)

    window.onpopstate = function (event) {
        history.pushState({ id }, `Selected: ${id}`, `load/result/cert=${id}`)

        confirm.render("", "DATA WILL BE LOST", "YOU WILL NOT BE ABLE TO<br>DOWNLOAD CERTIFICATE AGAIN", "DOWNLOAD", "GO BACK");
        btn_confirm_y.addEventListener('click', function () {
            confirm.continue();
        });
        btn_confirm_n.addEventListener('click', function () {
            confirm.abort('/')
        });

    }
    ////////////////////////////////////////////////////////////////////////////////////////////main_flag_condition agar ek baar is page par aa chuke ho to phirse nahi aa skte 
    if (flag_cert == 1) {
        btn_head_home.addEventListener('click', call_alert_home);
        btn_head_register.addEventListener('click', call_alert_register);
        btn_head_about.addEventListener('click', call_alert_about);

        btn_foot_mail.addEventListener('click', call_alert_mail);
        btn_foot_linkedin.addEventListener('click', call_alert_linkedin);
        btn_foot_git.addEventListener('click', call_alert_git);
        btn_foot_about.addEventListener('click', call_alert_about);

        
        function call_alert_home() {
            confirm.render("", "GO FAST WARNING", "YOU WILL NOT BE ABLE TO DOWNLOAD CERTIFICATE AGAIN WITHOUT GIVING THE TEST", 'CONTINUE', 'LEAVE');
            btn_confirm_y.addEventListener('click', function () {
                confirm.continue();
            });
            btn_confirm_n.addEventListener('click', function () {
                confirm.abort('/');
            });
        }
        function call_alert_register() {
            confirm.render("", "GO FAST WARNING", "YOU WILL NOT BE ABLE TO DOWNLOAD CERTIFICATE AGAIN WITHOUT GIVING THE TEST", 'CONTINUE', 'LEAVE');
            btn_confirm_y.addEventListener('click', function () {
                confirm.continue();
            });
            btn_confirm_n.addEventListener('click', function () {
                confirm.abort('/register');
            });
        }
        function call_alert_about() {
            confirm.render("", "GO FAST WARNING", "YOU WILL NOT BE ABLE TO DOWNLOAD CERTIFICATE AGAIN WITHOUT GIVING THE TEST", 'CONTINUE', 'LEAVE');
            btn_confirm_y.addEventListener('click', function () {
                confirm.continue();
            });
            btn_confirm_n.addEventListener('click', function () {
                confirm.abort('https://rishimishra.me');
            });
        }

        function call_alert_mail() {
            confirm.render("", "GO FAST WARNING", "YOU WILL NOT BE ABLE TO DOWNLOAD CERTIFICATE AGAIN WITHOUT GIVING THE TEST", 'CONTINUE', 'LEAVE');
            btn_confirm_y.addEventListener('click', function () {
                confirm.continue();
            });
            btn_confirm_n.addEventListener('click', function () {
                confirm.abort('https://www.rishimishra.me/#contact');
            });
        }
        function call_alert_linkedin() {
            confirm.render("", "GO FAST WARNING", "YOU WILL NOT BE ABLE TO DOWNLOAD CERTIFICATE AGAIN WITHOUT GIVING THE TEST", 'CONTINUE', 'LEAVE');
            btn_confirm_y.addEventListener('click', function () {
                confirm.continue();
            });
            btn_confirm_n.addEventListener('click', function () {
                confirm.abort('https://www.linkedin.com/in/rishi-mishra/');
            });
        }
        function call_alert_git() {
            confirm.render("", "GO FAST WARNING", "YOU WILL NOT BE ABLE TO DOWNLOAD CERTIFICATE AGAIN WITHOUT GIVING THE TEST", 'CONTINUE', 'LEAVE');
            btn_confirm_y.addEventListener('click', function () {
                confirm.continue();
            });
            btn_confirm_n.addEventListener('click', function () {
                confirm.abort('https://github.com/rishi-777');
            });
        }

    }

    else {
        alert.render("", "NOT ELIGIBLE", "YOU WILL BE REDIRECTED TO HOME PAGE IN 2 SECONDS", 'OK');
        btn_alert.addEventListener('click', click_btn_alert);
        function click_btn_alert() {
            open('/', '_parent').close()
        }
        setTimeout(timeout, 1500);
        function timeout() {
            open('/', '_parent').close()
        }
    }
}


///////////////////////////////////////////////////////// CUSTOM ALERT DIALOG
function CustomAlert(){
    this.render = function(dialog,head,body,btn_text){
        var winW = window.innerWidth;
        var winH = window.innerHeight;
        var dialogoverlay = document.getElementById('dialogoverlay');
        var dialogbox = document.getElementById('dialogbox');
        var alert_buttons = document.getElementById('alert_buttons');
        dialogoverlay.style.display = "block";
        dialogoverlay.style.height = winH+"px";
        dialogbox.width= 0.4*winW;
        dialogbox.style.left = (winW/2) -(0.4*winW/2) +"px";
        dialogbox.style.top = "100px";
        dialogbox.style.display = "flex";
        alert_buttons.style.display = "flex";
        document.getElementById('dialogboxhead').innerHTML = head;
        document.getElementById('dialogboxbody').innerHTML = body;
        document.getElementById('btn_alert').innerHTML =  btn_text;
    }
	this.ok = function(url){
        window.open(url, "_self")
		document.getElementById('dialogbox').style.display = "none";
	    document.getElementById('dialogoverlay').style.display = "none";
        document.getElementById('alert_buttons').style.display = "none";
	}
    this.remove_alert = function(){
        document.getElementById('dialogbox').style.display = "none";
	    document.getElementById('dialogoverlay').style.display = "none";
        document.getElementById('alert_buttons').style.display = "none";
    }
}
var alert = new CustomAlert();

///////////////////////////////////////////////////////// CUSTOM CONFIRM DIALOG
function CustomConfirm(){
	this.render = function(dialog,head,body,btn_text1,btn_text2){
		var winW = window.innerWidth;
        var winH = window.innerHeight;
        var dialogoverlay = document.getElementById('dialogoverlay');
        var dialogbox = document.getElementById('dialogbox');
        var confirm_buttons = document.getElementById('confirm_buttons');
        dialogoverlay.style.display = "flex";
        dialogoverlay.style.height = winH+"px";
        dialogbox.width= 0.4*winW;
        dialogbox.style.left = (winW/2) -(0.4*winW/2) +"px";
        dialogbox.style.top = "100px";
        dialogbox.style.display = "flex";
        confirm_buttons.style.display = "flex";
        document.getElementById('dialogboxhead').innerHTML = head;
        document.getElementById('dialogboxbody').innerHTML = body;
        document.getElementById('btn_confirm1').innerHTML =  btn_text1;
        document.getElementById('btn_confirm2').innerHTML =  btn_text2;
	}
	this.continue = function(){
		document.getElementById('dialogbox').style.display = "none";
		document.getElementById('dialogoverlay').style.display = "none";
        document.getElementById('confirm_buttons').style.display = "none";
	}
	this.abort = function(url){
		window.open(url, "_self")
        document.getElementById('confirm_buttons').style.display = "none";
	}
}
var confirm = new CustomConfirm();

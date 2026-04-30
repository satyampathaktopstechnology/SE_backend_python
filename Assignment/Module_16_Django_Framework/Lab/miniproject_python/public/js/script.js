$(document).ready(function(){
    
});



const CheckLogin = () => {
    var user = $("#username").val(); 
    var pass = $("#password").val();
    var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();

    if (!user || !pass) {
        $("#errorBox").text("All fields are required!");
        return;
    }

    $.post(loginUrl, {
        username: user,
        password: pass,
        csrfmiddlewaretoken: csrfmiddlewaretoken
    }, function (rt) {

        $("#errorBox").text(rt.message);

        if (rt.status == "success"){
            alert(rt.status)
            window.location.href = "/";
        }

    }).fail(function() {
        $("#errorBox").text("Credential Invalid. Try again.");
    });
}


let typingTimer;
const delay = 500; // debounce delay

const CheckUserName = () => {
    clearTimeout(typingTimer);

    typingTimer = setTimeout(() => {
        var Checkuser = $("#username").val();

        if (Checkuser.length < 3) {
            $("#usernameStatus")
                .text("Minimum 3 characters required")
                .css("color", "orange");
            return;
        }

        $("#usernameStatus")
            .text("Checking...")
            .css("color", "gray");

        $.get("/availableuser/", { Checkuser: Checkuser }, function (rt) {

            if (rt.status === "success") {
                $("#usernameStatus")
                    .text(rt.message)
                    .css("color", "green");
            } else {
                $("#usernameStatus")
                    .text(rt.message)
                    .css("color", "red");
            }

        }).fail(function () {
            $("#usernameStatus")
                .text("Error checking username")
                .css("color", "red");
        });

    }, delay);
};
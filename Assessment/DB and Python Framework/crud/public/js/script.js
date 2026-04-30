$(document).ready(function(){
    $('.cstf').hide()
});
const edit = (id) => {
    $('.cstf').fadeIn(500)
    $.get("editpage", { id: id }, function(rt) {
        console.log(rt);  // debug

        $("#edit_id").val(rt.id);
        $("#edit_username").val(rt.username);
        $("#edit_email").val(rt.email);
    });
}

const clearForm = () => {
    $("#edit_id").val('');
    $("#edit_username").val('');
    $("#edit_email").val('');
    $('.cstf').fadeOut(500)
}

const del = (id) => {
    if (confirm("Are you sure you want to delete this user?")) {
        $.get("/delete", { id: id }, function(rt) {
            alert("User deleted successfully!");
            location.reload(); // refresh table
        });
    } else {
        console.log("Delete cancelled");
    }
}
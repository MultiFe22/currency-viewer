function refresh(){
    var dates = document.getElementsByClassName("date-fields");
    // loop through all the date fields and check if its in the future
    for (var i = 0; i < dates.length; i++) {
        var date = dates[i].value;
        var date = new Date(date);
        var today = new Date();
        if (date > today) {
            // if the date is in the future, alert the user
            alert(`Date cannot be in the future ${dates[i].id}`);
            // and reset the date field to today's date
            dates[i].value = today.toISOString().slice(0,10);
            return false;
        }
    }

    var submitButton = 
    document.getElementById("sub");
    submitButton.click();
}
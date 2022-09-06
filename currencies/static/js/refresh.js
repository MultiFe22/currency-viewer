// functiion to check if the date range is valid, should be business days only
function checkDateRange(){
    var startDate = document.getElementById("start").value;
    var endDate = document.getElementById("end").value;
    startDate = new Date(startDate);
    endDate = new Date(endDate);
    
    if (startDate > endDate) {
        alert("Start date cannot be after end date");
        return false;
    }

    // count the number of business days between the two dates
    var count = 0;
    for (var d = startDate; d <= endDate; d.setDate(d.getDate() + 1)) {
        if (d.getDay() != 0 && d.getDay() != 6) {
            count++;
        }
    }

    // if the number of weekdays is less than 1 or greater than 5, alert the user
    if (count < 1 || count > 5) {
        alert("Date range must be between 1 and 5 business days");
        return false;
    }

    return true;
}

function refresh(){
    var dates = document.getElementsByClassName("date-fields");

    // check if the date range is valid
    if (!checkDateRange()) {
        return false;
    }
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

    var submitButton = document.getElementById("sub");
    submitButton.click();
}

$(document).ready(function() {
    let countryCodes = {};

    // Fetch country codes dynamically from Django API
    $.get("/api/country-codes/", function(data) {
        countryCodes = data;
    });

    // When country is selected, auto-fill phone code
    $("#id_country").change(function() {
        const selectedCountry = $(this).val();
        $("#phoneField").val(countryCodes[selectedCountry] || "");
    });

    // Form validation on submit
    $("#registerForm").submit(function(event) {
        let valid = true;
        $("input[required], select[required]").each(function() {
            if (!$(this).val()) {
                $(this).addClass("border-danger");
                valid = false;
            } else {
                $(this).removeClass("border-danger");
            }
        });

        if (!valid) {
            event.preventDefault();
            alert("Please fill in all required fields.");
        }
    });
});

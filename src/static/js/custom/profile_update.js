$("#profileUpdateForm").submit(function (event) {

    // Stop form from submitting normally
    event.preventDefault();

    // Get some values from elements on the page:
    let $form = $(this),
        url = $form.attr("action");

    // Send the data using post
    $.ajax(
        {
            url: url,
            type: "POST",
            data: $form.serializeArray(),
            dataType: "json",
            success: function (response) {
                Swal.fire(
                    'User',
                    'was updated successfully',
                    'success'
                )
            },
            error: function (response) {
                //TODO provide validation for user update fields

                let errors = response.responseJSON.errors
                console.log(errors)
                for (const errorsKey in errors) {
                    let main_element = document.getElementsByName(errorsKey);
                    let element = document.getElementById('error_' + errorsKey);
                    if (errors.hasOwnProperty(errorsKey)) {

                        let key = errors[errorsKey]
                        main_element[0].classList.add("is-invalid");
                        element.classList.add("invalid-tooltip");
                        element.innerHTML = key;

                    }
                }
            }
        }
    );
});

function check_input(id) {
    let main_element = document.getElementsByName(id);
    let element = document.getElementById('error_' + id);
    main_element[0].classList.remove("is-invalid");
    element.classList.remove("invalid-tooltip");
    element.innerHTML = '';
}
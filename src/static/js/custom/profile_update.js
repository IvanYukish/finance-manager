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
                for (const errorsKey in errors) {
                    if (errors.hasOwnProperty(errorsKey)) {

                        let key = errors[errorsKey]
                        console.log(key)
                    }
                }
            }
        }
    );
});

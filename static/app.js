$(function () {
    $('#addName').on('click', function (e) {
        e.preventDefault()

        $.ajax({
            url: '/process',
            type: 'POST',
            dataType: 'json',
            data: {
                firstName: $('#firstName').val(),
                lastName: $('#lastName').val()
            },
            success: function (response) {

                if (response.response_object['status'] === 1) {
                    $("#msg").text('');
                    $("#result").text(response.response_object['result']);
                } else {
                    $("#result").text('');
                    $("#msg").text(response.response_object['result']);
                }

                $('#firstName').val('')
                $('#lastName').val('')


            },
            error: function (error) {
                $('#msg').text(error.response_object);
                // console.log(error.response_object['result'])
            }

        })

    })

})

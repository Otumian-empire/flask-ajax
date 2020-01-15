$(function () {
    $('#addName').on('click', function (e) {
        e.preventDefault()

        $.ajax({
            url: '/insert',
            type: 'POST',
            dataType: 'json',
            data: {
                firstName: $('#firstName').val(),
                lastName: $('#lastName').val()
            },
            success: function (response) {

                if (response.response_object['status'] === 1) {
                    $("#msg").text('');
                    add_item(response.response_object['result'])

                } else {
                    $("#msg").text(response.response_object['result']);
                }

                $('#firstName').val('')
                $('#lastName').val('')

            },
            error: function (error) {
                $('#msg').text(error.response_object);
            }
        })

    })


    /**
     * add an item to the list
     */
    function add_item(data) {

        var span = $('<span></span>')
        span.text(data)

        var btn = $('<button></button>')
        btn.text('close')
        btn.addClass('close-btn')

        var clr = $('<div></div>')
        clr.addClass('clr')

        var li = $('<li></li>')
        li.append(span)
        li.append(btn)
        li.append(clr)

        $('#list').prepend(li)

        $('.close-btn').on('click', function () {

            // make request to remove item from the database
            $.ajax({
                url: '/delete/' + data,
                type: 'DELETE',
                dataType: 'json',
                success: function (response) {

                    if (response.response_object['status'] === 1) {

                        $(this).parent().remove()
                        // $("#msg").text('Task deleted');
                        location.reload(true)

                    }/*  else {
                        // $("#msg").text('Task not deleted');
                    } */

                    $('#firstName').val('')
                    $('#lastName').val('')

                },
                error: function (error) {
                    $('#msg').text(error.response_object);
                }
            })


        })
    }
})

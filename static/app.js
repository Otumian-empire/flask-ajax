$(function () {

    // read data
    $.ajax({
        url: '/read',
        type: 'POST',
        dataType: 'json',
        success: function (response) {

            tasks = response.response_object['result']

            var task_size = tasks.length

            for (i = 0; i < task_size; i++) {
                id = tasks[i][0]
                item = tasks[i][1] + " " + tasks[i][2]
                add_item(id, item)
            }

        },
        error: function (error) {
            $('#msg').text(error.response_object['result']);
        }

    })

    // submit name to database
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

                $('#firstName').val('')
                $('#lastName').val('')
                location.reload(true)

            },
            error: function (error) {
                $('#msg').text(error.response_object['result']);
            }
        })

    })


    /**
     * add an item to the list
     */
    function add_item(id, data) {

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
                url: '/delete/' + id,
                type: 'DELETE',
                dataType: 'json',
                success: function (response) {

                    if (response.response_object['status'] === 1) {

                        $(this).parent().remove()
                        location.reload(true)

                    }

                    $('#firstName').val('')
                    $('#lastName').val('')

                },
                error: function (error) {
                    $('#msg').text(error.response_object['result']);
                }
            })

        })

    }

})

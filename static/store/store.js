$(document).on('click', '#add-button', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: $('#add-button').data('url'),
        data: {
            productid: $('#add-button').val(),
            quantity: $('#select option:selected').val(),
            csrfmiddlewaretoken: CSRF_TOKEN,
            action: 'post'
        },
        success: function (json) {
            document.getElementById('basket-quantity').innerHTML = json.quantity
        },
        error: function (xhr, errmsg, err) {

        }
    });
})
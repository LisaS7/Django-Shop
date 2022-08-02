// Delete Item
$(document).on('click', '.delete-button', function (e) {
    e.preventDefault();
    var prodid = $(this).data('index');
    $.ajax({
        type: 'POST',
        url: $('.delete-button').data('url'),
        data: {
            productid: $(this).data('index'),
            csrfmiddlewaretoken: CSRF_TOKEN,
            action: 'post'
        },
        success: function (json) {
            $('.product-item[data-index="' + prodid + '"]').remove();
            document.getElementById("basket-quantity").innerHTML = json.quantity
            document.getElementById("subtotal").innerHTML = json.subtotal
            document.getElementById("total").innerHTML = json.total
        },
        error: function (xhr, errmsg, err) {

        }
    });
})


// Update Item
$(document).on('click', '.update-button', function (e) {
    e.preventDefault();
    var prodid = $(this).data('index');
    $.ajax({
        type: 'POST',
        url: $('.update-button').data('url'),
        data: {
            productid: $(this).data('index'),
            quantity: $('#select' + prodid + ' option:selected').text(),
            csrfmiddlewaretoken: CSRF_TOKEN,
            action: 'post'
        },
        success: function (json) {
            document.getElementById("basket-quantity").innerHTML = json.quantity
            document.getElementById("item-subtotal" + prodid).innerHTML = json.itemtotal
            document.getElementById("subtotal").innerHTML = json.subtotal
            document.getElementById("total").innerHTML = json.total
        },
        error: function (xhr, errmsg, err) {

        }
    });
})
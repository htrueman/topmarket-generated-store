function add_to_cart(id, quantity) {
    $.ajax({
        type: 'GET',
        url: add_to_cart_url,
        data: {
            'product_id': id,
            'quantity': quantity
        },
        success: function (data) {
            alert(data.message);
            window.location.reload();
        }
    });
}

function delete_cart_item(id) {
    $.ajax({
        type: 'GET',
        url: delete_item_cart_url,
        data: {
            'product_id': id
        },
        success: function (data) {
            if (data.deleted == true) {
                window.location.reload();
            } else if (data.deleted == false) {
                alert('Не удалось удалить товар с корзиныю Перезагрузите страницу');
            }
        }
    });
    e.preventDefault();
    return false;
}

function change_cart_item_quantity(id, obj) {
    var quantity = $(obj).val();
    $.ajax({
        type: "GET",
        url: change_cart_item_quantity_url,
        data: {
            'product_id': id,
            'quantity': quantity
        }
    });
    e.preventDefault();
}


// Orders ajax functions

$('#order_create_form').submit(function (e) {
    e.preventDefault();
    $.ajax({
        type: $(this).attr('method'),
        url: $(this).attr('action'),
        data: $(this).serialize(),
        success: function (data) {
            if ($("input").next('p').length) $("input").nextAll('p').empty();
                for (var name in data.errors) {
                    // object message error django
                    var $input = $("input[name='"+ name +"']");
                    $input.after("<p style='color: red'>" + data['errors'][name] + "</p>");
              }
            if (data.successed === true) {
                alert('Заказ успешно оформлен');
            }
        }
    })
});
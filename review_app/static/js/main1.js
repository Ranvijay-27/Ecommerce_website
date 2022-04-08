$(document).ready(function() {
    $('.increment-btn').click(function(e) {
        e.preventDefault();
        var inc_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(inc_value, 10);
        value = isNaN(value) ? 0 : value;
        if (value < 10) {
            value++;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }

    });
    $('.decrement-btn').click(function(e) {
        e.preventDefault();
        var dec_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(dec_value, 10);
        value = isNaN(value) ? 0 : value;
        if (value > 1) {
            value--;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }

    });

    $('.addtocartbtn').click(function(e) {
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name = csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/addtocart",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                csrfmiddlewaretoken: token

            },
            success: function(response) {

                alertify.success(response.status)

            }
        });


    });
    $('.addToWishlist').click(function(e) {
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name = csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/add-To-wishlist",
            data: {
                'product_id': product_id,

                csrfmiddlewaretoken: token

            },
            success: function(response) {
                alertify.success(response.status)

            }
        });

    });

    $('.changeQantity').click(function(e) {
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name = csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/update-cart",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                csrfmiddlewaretoken: token

            },
            success: function(response) {

                alertify.success(response.status)




            }
        });


    });


    $('.reviresubmit').click(function(e) {
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_text = $(this).closest('.product_data').find('.review_text').val();
        var product_rating = $(this).closest('.product_data').find('.rating_review').val();
        var product_name = $(this).closest('.product_data').find('.prod_name').val();
        var token = $('input[name = csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/review-rating",
            data: {
                'product_id': product_id,
                'product_text': product_text,
                'product_rating': product_rating,
                'product_name': product_name,
                csrfmiddlewaretoken: token

            },
            success: function(response) {

                alertify.success(response.status)


            }
        });


    });


    $('.delete-cart-item').click(function(e) {
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find('.prod_id').val();

        var token = $('input[name = csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/delete-cart-item",
            data: {
                'product_id': product_id,

                csrfmiddlewaretoken: token

            },
            success: function(response) {

                alertify.success(response.status)
                $('.carddata').load(location.href + " .carddata")

            }
        });


    });


    $('.changeQantity').click(function(e) {
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name = csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/update-product",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                csrfmiddlewaretoken: token

            },
            success: function(response) {

                alertify.success(response.status)


            }
        });


    });



    $('.changeQantity').click(function(e) {
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name = csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/update-cart",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                csrfmiddlewaretoken: token

            },
            // succuess: function(response) {
            //     // console.log(response)
            //     // alertify.succuess(response.status)

            // }
        });


    });


});
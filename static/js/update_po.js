function update_purchase_unit_price() {
    btn = document.querySelector('#update_po');
    data = {'order_id': btn.getAttribute('data-order_id'), 'line': []}
    document.querySelectorAll('.unit_price').forEach(element => {
        data.line.push({'id': element.getAttribute('data-line_id'), 'unit_price': element.value})
    });
    $.ajax({
        url: '/test',
        type: 'post',
        contentType: "application/json",
        data: JSON.stringify({
            "data": data
        }),
        beforeSend: function () {
            btn.setAttribute("disabled", "");
            btn.textContent = "Updating..."
        },
        success: function(response) {

            if (response.error) {
                document.querySelector('#alert_error').classList.remove('d-none');
                document.querySelector('#error_exp').textContent = response.error.message;
                document.querySelector('.close').addEventListener('click', function () {
                    location.reload();
                })
            }
            else {
                location.reload();
            }
        },
        // error: function(e) {
        //     console.log('>>>>>>>>>>>>>>>>>', e);
        // }
    });
}

function edit_purchase_unit_price() {
    document.querySelectorAll('.unit_price').forEach(ele => {
        ele.classList.remove("d-none");
    });
    document.querySelectorAll('.replace-input').forEach(ele => {
           ele.classList.add("d-none");
    })
    document.querySelector('#update_po').classList.remove('d-none');
    document.querySelector('#discard_po').classList.remove('d-none');
    document.querySelector('#edit_po').classList.add('d-none');
    
}

function update_subtotal(event) {
    var ele = event.target
    var subtotal = document.querySelector(`p[id='${ele.getAttribute('data-line_id')}']`);
    if (ele.value < 0) {
        ele.value = -(ele.value);
    }
    subtotal.textContent = (ele.value * subtotal.getAttribute('data-qty')).toFixed(2).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}

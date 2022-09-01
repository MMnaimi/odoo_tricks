function update_purchase_unit_price() {
    data = []
    btn = document.querySelector('#update_po');
    document.querySelectorAll('.unit_price').forEach(element => {
        data.push({'id': element.getAttribute('data-line_id'), 'unit_price': element.value})
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
            location.reload();
        },
        error: function(e) {
            location.assign('/404');
        }
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
    subtotal.textContent = ele.value * subtotal.getAttribute('data-qty');
}

function discard_update() {
    document.querySelectorAll('.unit_price').forEach(ele => {
        ele.classList.add("d-none");
    });
    document.querySelectorAll('.replace-input').forEach(ele => {
           ele.classList.remove("d-none");
    })
    document.querySelector('#update_po').classList.add('d-none');
    document.querySelector('#discard_po').classList.add('d-none');
    document.querySelector('#edit_po').classList.remove('d-none');
}


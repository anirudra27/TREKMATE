var updateBtns = document.getElementsByClassName('update-cart');

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        var user = '{{ request.user }}'; // Get the current user from the Django template
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('User:', user);
        console.log('Product ID:', productId);
        console.log('Action:', action);

        if (user === 'AnonymousUser') {
            console.log('User is not authenticated');
        } else {
            updateUserOrder(user, productId, action);
        }
    });
}

function updateUserOrder(user, productId, action) {
    console.log('User is authenticated, sending data...');

    var url = '/update_item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })
    .then(function(response) {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(function(data) {
        console.log('Update successful. Reloading page...');
        location.reload();
    })
    .catch(function(error) {
        console.error('Error updating user order:', error);
    });
}

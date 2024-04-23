var csrftoken = '{{ csrf_token }}';
    var total = '{{ order.get_cart_total|floatformat:2 }}';

    var form = document.getElementById('form');
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        console.log('Form Submitted...');
        document.getElementById('form-button').classList.add('hidden');
        document.getElementById('payment-info').classList.remove('hidden');
        initializePayment();
    });


    function initializePayment() {
        var config = {
            "publicKey": "test_public_key_12ee748969e54285b99b2897976e194b",
            "productIdentity": "1234567890",
            "productName": "Dragon",
            "productUrl": "http://gameofthrones.wikia.com/wiki/Dragons",
            "paymentPreference": ["KHALTI"],
            "eventHandler": {
                onSuccess(payload) {
                    var token = payload.token;
                    fetch('/process_payment/', {
                        method: 'POST',
                        body: JSON.stringify({ token: token }),
                        headers: { 'Content-Type': 'application/json' }
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            alert(data.message);
                        } else {
                            alert(data.message);
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
                },
                onError(error) {
                    console.log(error);
                },
                onClose() {
                    console.log('Widget is closing');
                }
            }
        };

        var checkout = new KhaltiCheckout(config);
        checkout.show({ amount: 250000 });
    }
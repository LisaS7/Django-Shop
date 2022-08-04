
var elem = document.getElementById('submit');
clientsecret = elem.getAttribute('data-secret');

var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
  ev.preventDefault();

  var custName = document.getElementById("custName").value;
  var custAdd = document.getElementById("custAdd").value;
  var custCity = document.getElementById("custCity").value;
  var custPlanet = document.getElementById("custPlanet").value;
  var custCommlink = document.getElementById("custCommlink").value;

  function make_key(length) {
    var result = '';
    var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for (var i = 0; i < length; i++) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
  }

  $.ajax({
    type: "POST",
    url: $('form#payment-form').data('url'),
    data: {
      order_key: make_key(12),
      name: custName,
      address: custAdd,
      city: custCity,
      planet: custPlanet,
      commlink: custCommlink,
      csrfmiddlewaretoken: CSRF_TOKEN,
      action: "post",
    },
    success: function (json) {
      console.log(json.success)
      console.log('payment processed')
      window.location.replace("http://127.0.0.1:8000/payment/orderplaced/");
    },
    error: function (xhr, errmsg, err) { },
  });



});
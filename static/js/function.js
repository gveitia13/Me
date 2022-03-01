$(function () {
  d = document
  d.querySelectorAll('button[name=_wash]')
    .forEach(e =>
      e.addEventListener('click', function (btn) {
        console.log(this)
        let id = this.id.slice(4)
        console.log(id)
        let param = new FormData()
        param.append('id', id)
        param.append('action', 'wash')

        ajaxFunction(location.pathname, param, response => {
          console.log(response)
          location.reload()
        },)
      }))
/*
  try {
    d.querySelector('#jazzy-logo img').src = '/static/img/logo-sm-blue-white.png'
  } catch (e) {
    console.log(e)
  }*/
  try {
    document.querySelector('div.login-logo').innerHTML =
      '<h2><img src="/static/img/logo-lg-red-black.png" style="width: 230px;height: auto;" alt="EnCAJA Lite"></h2>'
  } catch (e) {
    console.log(e)
  }
})

let ajaxFunction = function (url, parameters, callback, async = true) {
  $.ajax({
    url: url,
    type: 'POST',
    data: parameters,
    dataType: 'json',
    processData: false,
    contentType: false,
    async: async
  })
    .done(function (data) {
      console.log(data)
      if (!data.hasOwnProperty('error')) {
        callback(data)
        return false
      }
      /*      if (data['error'].toString().includes('UNIQUE'))
              message_error(`There is already a ${ent} with this name`)
            else message_error(data.error)*/
    })
    .fail(function (jqXHR, textStatus, errorThrown) {
      alert(textStatus + ': ' + errorThrown)
    })
    .always(function (data) {
    })
}
function sendNumber(fk_id_question) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/', true);
    xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
    xhr.onload = function() {
      if (xhr.status === 200) {
        console.log(xhr.responseText);
        document.getElementById('RESPOSTA').value = xhr.responseText;
      }
    };
    xhr.send(JSON.stringify({fk_id_question: fk_id_question}));
  }
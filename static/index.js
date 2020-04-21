function run(){
    $.ajax({
          data : {
             text : $('#text').val(),
                 },
             type : 'POST',
             url : '/result'
            })
        .done(function(data) {
          $('#output').text(data.output).show();
      });
      event.preventDefault();
}
$(document).ready(function(){
    $('#title').focus();
      $('#text').autosize();
  });
setTimeout(function() {
    $('#messages').fadeOut('fast');
}, 5000);

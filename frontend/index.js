$(document).ready(function() {
    $('#send-button').click(function() {
        var userInput = $('#user-input').val();
        $('#responses').append('<div>You: ' + userInput + '</div>');
        $.post('/chat', { user_input: userInput }, function(data) {
            $('#responses').append('<div>Agent: ' + data.response + '</div>');
            $('#user-input').val('');
            $('#chat-box').scrollTop($('#chat-box')[0].scrollHeight);
        });
    });
});

(function(){

    $("[name=checkpassword]").keyup(function(){
        $password = $('input[name=password]');
        $checkpassword = $('input[name=checkpassword]');
        $pw_message = $('#pw_message')

        if($checkpassword.val()!=$password.val()){
            $pw_message.text('비밀번호와 다릅니다')
            console.log("틀렸습니다");
            console.log($checkpassword.val());
            console.log($password.val());
        }else{
            $pw_message.text('비밀번호와 일치하였습니다.')
        };
    });
})();



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

    $("[name=username]").focusout(function(){
        $username = $('input[name=username');
        alert("efef");

        api_url = "/api/username/check/";

        $.ajax({
            url:api_url,
            method:'GET',
            date:{
                received_username: $username,
            },
            success:function(result){
                        alert("success");
                    }
        
        });

    
    
    });


})();



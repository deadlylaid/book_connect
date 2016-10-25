(function(){

    $submit_button = $('#button');

    $("[name=checkpassword]").keyup(function(){
        $password = $('input[name=password]');
        $checkpassword = $('input[name=checkpassword]');
        var pw_message = document.getElementById('pw_message');

        if($checkpassword.val()!=$password.val()){
            var checkpw_message = '<p class="text-danger"><strong>잠깐! </strong> 비밀번호가 일치하지 않아요!</p>';
            pw_message.innerHTML = checkpw_message;
            
            $submit_button.attr('disabled', true);
            //console.log("틀렸습니다");
            //console.log($checkpassword.val());
            //console.log($password.val());
        }else{
            var checkpw_message = '<p class="text-success">비밀번호가 일치합니다.</p>';
            pw_message.innerHTML = checkpw_message;
            $submit_button.attr('disabled', false);
        };
    });

    $("[name=username]").focusout(function(){
        $username = $('input[name=username').val();

        //console.log($username)

        api_url = "/api/username/check/";

        $.ajax({
            url:api_url,
            method:'POST',
            data:{
                received_username: $username,
            },
            success:function(result){
                        var check_username = document.getElementById("check_username");
                        if(result.overlap==true){
                            var newElement = '<p class="text-danger"><strong>잠깐! </strong>이미 있는 아이디에요! 누구도 생각 못한 환상적인 아이디를 생각해보아요!</p>';
                            check_username.innerHTML = newElement;
                            $submit_button.attr('disabled', true);
                        }else{
                            var newElement = '<p class="text-success"><strong>정말 멋진 아이디에요! </strong></p>';
                            check_username.innerHTML = newElement;
                        }
                    }
        
        });

    
    
    });


})();



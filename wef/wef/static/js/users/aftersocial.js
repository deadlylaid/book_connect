(function(){
    $check_phone_button = $('#check_phone_button');
    $phone_number = $('input[name=phonenumber]')
    console.log($phone_number)

    $check_phone_button.on('click', function(event){
        $phone_number = $('input[name=phonenumber]').val()

        api_url = '/api/phonenumber/sms/check/';

        if($phone_number.length<10){
            alert("올바른 휴대폰번호를 입력해주세요");
        }else{

            $.ajax({
                url: api_url,
                method: 'POST',
                data: {
                    phone_number: $phone_number,
                },
                success:function(result){
                            if(result.sms==true){
                                console.log(result);
                                alert("문자를 발송하였습니다. 서버 상황에 따라 최대 3분까지 소요될 수 있습니다.");
                                $auth = $("#auth");
                                $auth.append("<br><input type='text' name='tokenbox' placeholder='인증번호를 입력하세요' required> <input type='button' id='checktoken' value='인증확인'> ");

                                $created_button = $('#checktoken');
                                checktoken($created_button);

                            }else{
                                console.log(result);
                                alert("이미 등록되어있는 번호입니다.");
                            }
                        }
            });

        }

    });

    function checktoken(created_button){
        created_button.on('click', function(event){
            $token_num = $('input[name=tokenbox]');
            console.log($token_num.val())

            $.ajax({
                url: '/api/token/check/',
                method: 'PUT',
                data: { token_num: $token_num.val(), },
                success: function(result){
                    if(result.certification==true){
                        console.log("인증성공");
                        $check_phone_button.remove()
                        $insert_num = $('#auth');
                        $insert_num.empty();
                        $insert_num.html("인증이 완료되었습니다!!");

                    }else{
                        alert("인증번호가 일치하지 않습니다");
                    }
                },
            });

        });
    }

})();

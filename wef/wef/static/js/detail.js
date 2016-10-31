(function(){

    $(document).ready(function(){
        //판매하려는 책 목록의 수를 가져온다.
        $book_list_num = $("div").data("listNum");

        $("[id^=btn]").on('click', function(event){
            //id 값을 잡는다
            var button_id = $(this).attr("id");
            var button = $(this);
            var number = button_id.replace("btn", "");
            $post_id = $(".data").data("postId");

            // 책 이름을 잡기위해 li태그의 id를 잡는다
            var list = '#list'+number
            var list_book = $(list).text();
            var cancel = 'cancel'+number;
             
            console.log("책이름과 가격 = "+list_book)
            console.log("post_id = "+$post_id)

            api_url = "/api/"+ $post_id +"/soldout/";

            $.ajax({
                url: api_url,
                method :'PUT',
                data:{
                         post_id: $post_id,
                         book_list_id: number,
                     },
                success:function(book_list){
                            console.log(book_list);
                            console.log(book_list.is_soldout);
                            if(book_list.is_soldout==true){
                                $(list).addClass("redline");
                                $(list).addClass("list-group-item-danger");
                                $(button).val("번복하기");
                            }
                            else if(book_list.is_soldout==false){
                                $(list).removeClass("redline");
                                $(list).removeClass("list-group-item-danger");
                                $(button).val("sold out");
                            }
                        }
            });
        });

        $("[id^=msg]").on('click', function(event){
            //id 값을 잡는다
            var msg_button_id = $(this).attr("id");
            var msg_button = $(this);
            var msg_number = msg_button_id.replace("msg", "");

            // 책 이름을 잡기위해 li태그의 id를 잡는다
            var msg = '#list'+msg_number
            var book = $(msg).text();
            var bookname = book.split('(')[0];

            // post_id값으로 해당 포스트를 올린 유저를 알기위해
            $post_id = $(".data").data("postId");
            
            var send_check = confirm("문자 전송시 회원님의 휴대폰번호는 판매자에게 제공됩니다. 계속 하시겠습니까?")
                
            if (send_check == true){
                $.ajax({
                    url:'/api/sendbuysms/',
                    method:'POST',
                    data:{
                        bookname : bookname,
                        post_id : $post_id,
                    },
                    success: function(received_data){
                        if(received_data.send==true){  
                            alert("문자를 보냈습니다.");
                        }else{
                            alert("휴대폰 번호를 등록하지 않아서 문자를 보낼 수 없습니다.");
                        }
                    }
                });
            } else {
                alert("취소버튼을 눌렀다");
            }
        });


    });

})();

//bookname만 따로 잡기위해, bookprice를 따로잡기위해
//var bookname = list_book.split('(')[0];
//var bookprice = list_book.split('(')[1].substring(list_book.split('(')[1].length-3,list_book.split('(')[1]);

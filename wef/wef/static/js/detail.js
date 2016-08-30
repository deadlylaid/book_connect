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

            //bookname만 따로 잡기위해, bookprice를 따로잡기위해
            //var bookname = list_book.split('(')[0];
            //var bookprice = list_book.split('(')[1].substring(list_book.split('(')[1].length-3,list_book.split('(')[1]);

             
            console.log("책이름과 가격 = "+list_book)
            console.log("post_id = "+$post_id)

            api_url = "/api/"+ $post_id +"/soldout/";

            $.ajax({
                url: api_url,
                type:'PUT',
                data:{
                         post_id: $post_id,
                         book_list_id: number,
                     },
                success:function(book_list){
                            console.log(book_list);
                            console.log(book_list.is_soldout);
                            if(book_list.is_soldout==true){
                                $(list).addClass("redline");
                                $(button).val("번복하기");
                            }
                            else if(book_list.is_soldout==false){
                                $(list).removeClass("redline");
                                $(button).val("sold out");
                            }

                        }
            });

        });

    });

})();

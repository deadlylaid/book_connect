(function(){

    $(document).ready(function(){
        //판매하려는 책 목록의 수를 가져온다.
        $book_list_num = $("div").data("listNum");

        console.log($book_list_num);

    $("[id^=btn]").on('click', function(event){
        //id 값을 잡는다
        var button_id = $(this).attr("id");
        var number = button_id.replace("btn", "");
        $post_id = $("div").data("PostId");

        // 책 이름을 잡기위해 li태그의 id를 잡는다
        var list = '#list'+number
        var list_book = $(list).text();

        //bookname만 따로 잡기위해, bookprice를 따로잡기위해
        var bookname = list_book.split('(')[0];
        var bookprice = list_book.split('(')[1].substring(list_book.split('(')[1].length-3,list_book.split('(')[1]);

        var sold_out = 0;
        //test alert
        console.log(bookname)
        console.log(bookprice)
        console.log(list_book)

        //취소선을 포함한 css클래스를 추가하는 명령어
        $(list).addClass("redline");

//        $.ajax({
//            type:'POST',
//            url:,//
//            data:{
//                     post_id: $post_id,
//                 },
//            success:function(id){
//                  $(list).addClass("redline");
//                    }
//
//        });




    });


    });

})();

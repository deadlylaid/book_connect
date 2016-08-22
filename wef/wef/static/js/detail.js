(function(){

    $(document).ready(function(){
        //판매하려는 책 목록의 수를 가져온다.
        $book_list_num = $("div").data("listNum");
        console.log($book_list_num);

    $("[id^=btn]").on('click', function(event){
        //id 값을 잡는다
        var id = $(this).attr("id");
        var number = id.replace("btn", "");
        // 책 이름을 잡기위해 li태그의 id를 잡는다
        var list = '#list'+number
        var list_book = $(list).text();
        var bookname = list_book.split('(')[0];
        var bookprice = list_book.split('(')[1].substring(list_book.split('(')[1].length-3,list_book.split('(')[1]);
        //test alert
            console.log(bookname)
            console.log(bookprice)
    });


    });

})();

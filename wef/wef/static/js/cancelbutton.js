(function(){

    $(document).ready(function(){
        //판매하려는 책 목록의 수를 가져온다.
        $book_list_num = $("div").data("listNum");
        console.log($book_list_num);

    $("[id^=btn]").on('click', function(event){
        var id = $(this).attr("id");
        var number = id.replace("btn", "");
        //test alert
            alert(number)
    });


    });

})();

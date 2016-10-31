(function(){
    //도서 추가 버튼 가져오기
    var $addlist_button = $('input[name=addlist]');
    //도서 ul태그 가져오기
    var $booklist = $('.booklist');
    //post로 추가된 도서를 보내기 위한 hiddenlist도 가져오기
    var $hiddenlist = $('.hiddenlist');


    //도서 추가 버튼을 클릭하면 도서리스트에 추가되는 함수
    $addlist_button.on('click', function(event){
        //도서 이름, 도서 가격 input 가져오기
        var $book_name = $("input[name=bookname]");
        var $book_price = $("input[name=bookprice]");

        if(($book_name.val() == "")||($book_name.val() == null)){
            alert('판매할 도서를 적어주세요!');
        }
        else{
            if(($book_price.val() == "")||($book_price.val() == null)){
                $booklist.append('<li class="list-group-item bk-border-color">' + $book_name.val() + '(가격미정)</li>');
                $hiddenlist.append('<input type="hidden" name="book" value="'+$book_name.val()+'">')
                $hiddenlist.append('<input type="hidden" name="price" value="가격미정">')
            }
            else {
                $booklist.append('<li class="list-group-item bk-border-color">' + $book_name.val() + '(' + $book_price.val() + '원)</li>');
                $hiddenlist.append('<input type="hidden" name="book" value="'+$book_name.val()+'">')
                $hiddenlist.append('<input type="hidden" name="price" value="'+$book_price.val()+'">')
            }
            $book_name.val('');
            $book_price.val('');
        }
    });


})();

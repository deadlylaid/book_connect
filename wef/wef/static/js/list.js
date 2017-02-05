(function(){

        $search_input_box = $(".bookconnect-input-text");

        $search_input_box.focus(function(){

            var search_alert = document.getElementById('alert')
            search_alert.innerHTML='<p style="color:#e74c3c;">검색어는 띄어쓰기를 통해서 구분됩니다. <br />ex)행복한 결혼 -> 행복(x), 행복한(O)</p>';

        });

})();

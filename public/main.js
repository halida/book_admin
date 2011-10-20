function search(){
    var text = $('#search-text').attr('value');
    $.get('/search', {type:'book', text:text}, function(data){
	    var result = $('#search-result');
	    result.html("");
	    $.each(data.book, function(i, book){
		    result.append("<div>"+book.title+"</div>");
		});
	});
}


function onReturnPressed(target, f){
    $(target).bind("keypress", function(e){
       if (e.keyCode == 13) f();
	});
}

function init(){
}

function addBook(){
    var title = $('#book-form #title').attr('value');
    var author = $('#book-form #author').attr('value');
    var ISBN = $('#book-form #ISBN').attr('value');
    $.post("/book/update", {title:title, author:author, ISBN:ISBN}, function(data){
	    $('#book-form #title').attr('value', '');
	    $('#book-form #author').attr('value', '');
	    $('#book-form #ISBN').attr('value', '');
	});
}



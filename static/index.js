$(function() {
    $.ajax({
        url:"/api/articles",
        method: "GET",
        dataType: "json",
        success: function(data){
            var str = "";
            for(var i=0;i<data.articles.length;i++){
                console.log(data.articles[i])
                str += "Title: " + data.articles[i].title;
            }
            $("body").html(str)
        }
    });
});
$(function() {
    $.ajax({
        url:"api/articles/all",
        method: "GET",
        type: "json",
        success: function(data){
            data.articles.forEach(function(news){
                var title = "Title: " + news.title;
                var pubDate = "PubDate: " + news.pubDate;
                var link = news.link;
                console.log(title)
                $("body").append("<div class='card'><div class='card-header'><h5 class='font-weight-bold'>" + title + "</h1></div><div class='card-body'><blockquote class='blockquote mb-0'><p><a href='" + link + "'>" + link + "</a></p><footer class='blockquote-footer'>" + pubDate + "</footer></blockquote></div></div>")
            })
        },
        error: function(data){
            $("body").append("<div>Error</div>")
        }
    });
});
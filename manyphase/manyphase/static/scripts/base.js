
$(function(){
    //on initial page load, load the Home section
    var p = window.location.pathname
    if(p.length == 0 || p == '/'){
        ajaxLoad("/Home"); 
    }else{
        ajaxLoad(p); 
    }
    $(".nav-item, #logo").click(function(){
        //check for logo first
        var pageName = (this.id != 'logo') ? this.id : "Home"; 

        ajaxLoad("/"+pageName);
    });
    /*
    $(".nav-item, #logo").click(function(){
        // do ajax loading into the content div
        var pageName = (this.id != 'logo') ? this.id : "Home"; 
        $.ajax({
            url:"/ajax/"+pageName,
        }).done(function(data){
            var stateObj = {page:"id"}; 
            $("#main-block").html(data);
            //change history state
            history.pushState(stateObj, "ManyPhase-"+pageName, "/"+pageName);
            $(".nav-item").removeClass("current-page");
            $(".nav-item#"+pageName).addClass("current-page");

            if($("#slider").length)
                $("#slider").nivoSlider();
        });
        
    });
    */
    window.onpopstate = function(){
        var p = window.location.pathname
        if(p.length == 0 || p == '/'){
            page = "/Home";
        }else{
            page = p;
        }

        ajaxLoad(page, push=false);
    }
});

function ajaxLoad(pageName, push){
    push = typeof push !== 'undefined' ? push : true;

    $.ajax({
        url:"/ajax"+pageName,
    }).done(function(data){
        var stateObj = {page:pageName};
        $("#main-block").html(data);
        //change history state
        if(push == true)
            history.pushState(stateObj, "ManyPhase"+pageName, pageName);

        $(".nav-item").removeClass("current-page");
        $(".nav-item#"+pageName.substring(1)).addClass("current-page");

        if($("#slider").length)
            $("#slider").nivoSlider();
    });
}

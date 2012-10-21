
$(function(){
    //on initial page load, load the Home section
    var p = window.location.pathname
    if(p.length == 0 || p == '/'){
        ajaxLoad("/Home"); 
    }else{
        ajaxLoad(p); 
    }
    $(".nav-item, #logo").click(function(){
        // do ajax loading into the content div
        var id = (this.id != 'logo') ? this.id:"Home"; 
        $.ajax({
            url:"/ajax/"+id,
        }).done(function(data){
            var stateObj = {page:"id"}; 
            $("#main-block").html(data);
            //change history state
            history.pushState(stateObj, "ManyPhase-"+id, "/"+id);
            $("#slider").nivoSlider();
        });
        
    });

    window.onpopstate = function(){
        var p = window.location.pathname
        if(p.length == 0 || p == '/'){
            page = "/Home";
        }else{
            page = p;
        }

        ajaxLoad(page);
    }
});

function ajaxLoad(pageName){

    $.ajax({
        url:"/ajax"+pageName,
    }).done(function(data){
        var stateObj = {page:pageName};
        $("#main-block").html(data);
        //change history state
        history.pushState(stateObj, "ManyPhase"+pageName, pageName);
        $("#slider").nivoSlider();
    });
}

$(function(){
    $(".nav-item").click(function(){
        var stateObj = {}; 
        // do ajax loading into the content div
        var id = this.id; 
        $.ajax({
            url:"/ajax/"+id,
        }).done(function(data){
            $("#main-block").html(data);
            //change history state
            history.pushState(stateObj, "ManyPhase-"+id, "/"+id);
        });
        
    });
});


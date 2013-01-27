


$(function() {

    
    if (!Modernizr.inputtypes.date || $.browser.name== 'chrome'){
        $("#id_start_date").datepicker();
		$("#id_end_date").datepicker();
	
    }


    $('#description_charlimit').html('<span id="description_charsleft"></span> characters remaining');
    
    $('#id_description').NobleCount('#description_charsleft',{
    	on_negative: 'go_red',
    	on_positive: 'go_green',
    	max_chars: 250
    });
    
    
    if ($("#end_date input").val() == ""){
		    $("#end_date").hide();
		    var add_days;
		    add_days=$('<div><em>Is this a multi-day event? You can <a href="#">add an end date</a></em>.</div>').click(function(){
		        $("#end_date").show()
		        $(this).hide();
		        return false;
		    })
		    
		    $("#start_date").append(add_days)
		}

    $("#id_tags").tagEditor(
    {
        confirmRemoval: false,
        confirmRemovalText: 'Remove tag?',
        completeOnBlur: true
    });


  $('form').submit(function(){
      $('.placeholder').val('');
      })

});
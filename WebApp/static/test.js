var voice_chosen = false;
var song_chosen = false;

$('#song-upload').bind('change', function() { 
	song_chosen = true;
	var fileName = '';
	fileName = $(this).val();
	slash_idx = fileName.lastIndexOf('\\');
	if(slash_idx > -1) {
		fileName = fileName.substring(slash_idx + 1);
	}
	$('#song-selected').html(fileName);
})

$('#voice-upload').bind('change', function() { 
	voice_chosen = true;
	var fileName = '';
	fileName = $(this).val();
	slash_idx = fileName.lastIndexOf('\\');
	if(slash_idx > -1) {
		fileName = fileName.substring(slash_idx + 1);
	}
	$('#voice-selected').html(fileName);
})

$('#submit1').click(function(){
	console.log(song_chosen)
	if(song_chosen) {
		var status = $(this).siblings('.submit-status');
		status.addClass('complete');
		status.html('A file has been submitted &#10004;');
	}
})

$('#submit2').click(function(){
	if(voice_chosen) {
		var status = $(this).siblings('.submit-status');
		status.addClass('complete');
		status.html('A file has been submitted &#10004;');
	}
})
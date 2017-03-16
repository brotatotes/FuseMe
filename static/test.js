var song_chosen = false;
var voice_chosen = false;

$('#song-upload').bind('change', function() { 
	song_chosen = true;
	var fileName = '';
	fileName = $(this).val();
	slash_idx = fileName.lastIndexOf('\\');
	if(slash_idx > -1) {
		fileName = fileName.substring(slash_idx + 1);
	}
	$('#song-selected').html(fileName);
	var status = $(this).siblings('.submit-status');
	status.addClass('complete');
	status.html('File submitted &#10004;');
	console.log(song_chosen);
	$('#submit1').trigger('click');
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
	var status = $(this).siblings('.submit-status');
	status.addClass('complete');
	status.html('File submitted &#10004;');
	console.log(song_chosen);
	$('#submit2').trigger('click');
})

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
	var status = $(this).siblings('.submit-status');
	status.addClass('complete');
	status.html('A file has been uploaded &#10004;');
	$('#f1').submit();
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
	status.html('A file has been uploaded &#10004;');
	$('#f2').submit();
})

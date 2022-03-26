// API Notification iha header nian
setInterval(function() {
	$.get('/api/notif/badge/',function (data) {
		document.getElementById("notifBadge").innerHTML = data.notifCount;
		if (data.notifCount > 0 ) {
			var x = document.getElementById("myAudio"); 
			x.play(); 
		}
	});
}, 3000);

setInterval(function() {
	$.get('/api/notif/badge/',function (data) {
		document.getElementById("notifBadge").innerHTML = data.notifCount;
	});
}, 3000);

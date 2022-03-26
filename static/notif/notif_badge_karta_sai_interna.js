// API notification karta sai nian
setInterval(function() {
	$.get('/api/notif/badge-karta-sai-interna/',function (data) {
		document.getElementById("notifBadgeKartaSaiInterna").innerHTML = data.notifKartaSaiInternaCount;
	});
}, 3000);

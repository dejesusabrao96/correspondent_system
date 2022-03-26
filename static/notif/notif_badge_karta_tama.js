// API notification ba karta tama nian
setInterval(function() {
	$.get('/api/notif/badge-karta-tama/',function (data) {
		document.getElementById("notifBadgeKartaTama").innerHTML = data.notifKartaTamaCount;
	});
}, 3000);

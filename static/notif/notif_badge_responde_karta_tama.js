// API notification ba responde karta tama nian
setInterval(function() {
	$.get('/api/notif/badge-responde-karta-tama/',function (data) {
		document.getElementById("notifBadgeRespondeKartaTama").innerHTML = data.notifRespondeKartaTamaCount;
	});
}, 3000);

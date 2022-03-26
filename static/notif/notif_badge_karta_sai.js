// API notification karta sai nian
setInterval(function() {
	$.get('/api/notif/badge-karta-sai/',function (data) {
		document.getElementById("notifBadgeKartaSai").innerHTML = data.notifKartaSaiCount;
	});
}, 3000);

document.addEventListener("DOMContentLoaded", function () {
	const alertList = document.querySelectorAll(".alert");
	const alerts = [...alertList].map((element) => new bootstrap.Alert(element));
	const bsAlert = new bootstrap.Alert("#myAlert");
	setActiveLink();
	var myModal = new bootstrap.Modal(document.getElementById("subscribeModal"), {
		keyboard: false,
	});
	$(".toast").toast("show");
    

});

function setActiveLink() {
	var path = location.pathname;
	var pageName;

	if (path === "/") {
		pageName = "home";
	} else if (path.startsWith("/printables")) {
		pageName = "printables";
	}

	var liElement = document.querySelector(
		"li[data-link-name='" + pageName + "']"
	);
	if (liElement) {
		var aElement = liElement.querySelector("a.nav-link");
		if (aElement) {
			aElement.classList.add("bold");
		}
	}
}

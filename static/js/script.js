document.addEventListener("DOMContentLoaded", function () {
	setActiveLink();
	var myModal = new bootstrap.Modal(document.getElementById("subscribeModal"), {
		keyboard: false,
	});
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

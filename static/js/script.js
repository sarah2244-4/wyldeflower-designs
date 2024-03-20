document.addEventListener("DOMContentLoaded", function () {
	setActiveLink();
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
		liElement.classList.add("bold");
	}
}

document.addEventListener("DOMContentLoaded", function () {
	// Update quantity on click
	$(".update-link").click(function (e) {
		var form = $(this).prev(".update-form");
		form.submit();
	});

	// Remove item and reload on click
	$(".remove-item").click(function (e) {
		var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
		var itemId = $(this).attr("id").split("remove_")[1];
		var url = `/bag/remove/${itemId}/`;
		var data = {'csrfmiddlewaretoken': csrfToken };

		$.post(url, data)
		.done(function() {
			location.reload();
		});
	});
});

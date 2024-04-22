// Function to update quantity and handle enable/disable buttons
function updateQuantity(itemId, amount) {
	var inputElement = $(`#id_qty_${itemId}`);
	var currentValue = parseInt(inputElement.val());
	var newValue = currentValue + amount;

	// Validate newValue to stay within min and max bounds (1-99)
	if (newValue >= 1 && newValue <= 99) {
		inputElement.val(newValue);
		handleEnableDisable(itemId); // Update button enable/disable state
	}
}

// Event delegation for increment/decrement buttons
$(document).on("click", ".increment-qty", function (e) {
	e.preventDefault();
	var itemId = $(this).data("item_id");
	updateQuantity(itemId, 1); // Increment by 1
});

$(document).on("click", ".decrement-qty", function (e) {
	e.preventDefault();
	var itemId = $(this).data("item_id");
	updateQuantity(itemId, -1); // Decrement by 1
});

// Handle input change event to enable/disable buttons
$(document).on("input", ".qty_input", function () {
	var itemId = $(this).data("item_id");
	handleEnableDisable(itemId);
});

// Disable +/- buttons outside 1-99 range on page load
$(".qty_input").each(function () {
	var itemId = $(this).data("item_id");
	handleEnableDisable(itemId);
});

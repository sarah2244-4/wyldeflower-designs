// Timer variables to handle continuous increment/decrement
var timer;
var delay = 250; // Initial delay in milliseconds
var interval = 300; // Interval for subsequent increments/decrements in milliseconds

// Function to handle continuous incrementing
function incrementValue(inputElement) {
	var currentValue = parseInt($(inputElement).val());
	$(inputElement).val(currentValue + 1);
	handleEnableDisable($(inputElement).data("item_id"));
}

// Function to handle continuous decrementing
function decrementValue(inputElement) {
	var currentValue = parseInt($(inputElement).val());
	$(inputElement).val(currentValue - 1);
	handleEnableDisable($(inputElement).data("item_id"));
}

// Click and hold functionality for increment/decrement buttons
const clickAndHold = (btnEl, actionFn) => {
	let timerId;

	// Handle when clicking down
	const onMouseDown = () => {
		actionFn();
		timerId = setInterval(actionFn, interval);
	};

	// Stop or clear interval
	const clearTimer = () => {
		clearInterval(timerId);
	};

	// Handle when mouse is clicked
	btnEl.addEventListener("mousedown", onMouseDown);
	// Handle when mouse is raised
	btnEl.addEventListener("mouseup", clearTimer);
	// Handle mouse leaving the clicked button
	btnEl.addEventListener("mouseout", clearTimer);

	// Return a callback function to remove listeners (useful for cleanup)
	return () => {
		btnEl.removeEventListener("mousedown", onMouseDown);
		btnEl.removeEventListener("mouseup", clearTimer);
		btnEl.removeEventListener("mouseout", clearTimer);
	};
};

// Event handler for increment button press
$(".increment-qty").each(function () {
	const inputElement = $(this).closest(".input-group").find(".qty_input")[0];
	clickAndHold(this, () => incrementValue(inputElement));
});

// Event handler for decrement button press
$(".decrement-qty").each(function () {
	const inputElement = $(this).closest(".input-group").find(".qty_input")[0];
	clickAndHold(this, () => decrementValue(inputElement));
});

// Handle input change event to enable/disable buttons
$(".qty_input").change(function () {
	var itemId = $(this).data("item_id");
	handleEnableDisable(itemId);
});

// Disable +/- buttons outside 1-99 range
function handleEnableDisable(itemId) {
	var currentValue = parseInt($(`#id_qty_${itemId}`).val());
	var minusDisabled = currentValue < 2;
	var plusDisabled = currentValue > 98;
	$(`#decrement-qty_${itemId}`).prop("disabled", minusDisabled);
	$(`#increment-qty_${itemId}`).prop("disabled", plusDisabled);
}

// Ensure proper enabling/disabling of all inputs on page load
$(".qty_input").each(function () {
	var itemId = $(this).data("item_id");
	handleEnableDisable(itemId);
});

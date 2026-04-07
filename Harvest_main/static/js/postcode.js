// jshint esversion: 8

// Validate event postcode on form submission
document.getElementById('article-form').addEventListener('submit', function (e) {
    const isEvent = document.getElementById('is_event_related').checked;
    const postcode = document.getElementById('event_postcode').value.trim();
    const regex = /^[A-Za-z0-9 ]{3,10}$/;  // Alphanumeric + space, 3–10 characters

    // If event is checked but postcode is invalid, prevent form and show alert
    if (isEvent && !regex.test(postcode)) {
        e.preventDefault();
        alert("Please enter a valid postcode for the event (3–10 characters).");
        document.getElementById('event_postcode').classList.add('is-invalid');
    }
});

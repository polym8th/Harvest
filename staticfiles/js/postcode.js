document.getElementById('article-form').addEventListener('submit', function(event) {
    const isEventRelated = document.getElementById('is_event_related').checked;
    const postcodeInput = document.getElementById('event_postcode');
    const eventPostcode = postcodeInput.value.trim();

    // Clear previous visual indicator
    postcodeInput.classList.remove('is-invalid');

    if (isEventRelated && eventPostcode === '') {
        event.preventDefault();  // Stop form submission
        postcodeInput.classList.add('is-invalid');  // Add Bootstrap red border
        postcodeInput.focus();
        alert('Please enter a postcode for the event.');
    }
});
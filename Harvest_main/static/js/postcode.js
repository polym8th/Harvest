document.getElementById('article-form').addEventListener('submit', function(event) {
    var postcode = document.getElementById('event_postcode').value.trim();

    if (postcode === '') {
        event.preventDefault(); // Stop form from submitting
        alert('Please enter a postcode.');
        document.getElementById('event_postcode').focus();
    }
});
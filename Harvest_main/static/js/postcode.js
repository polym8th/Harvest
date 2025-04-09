// jshint esversion: 8
document.getElementById('article-form').addEventListener('submit', function (e) {
    const isEvent = document.getElementById('is_event_related').checked;
    const postcode = document.getElementById('event_postcode').value.trim();
    const regex = /^[A-Za-z0-9 ]{3,10}$/;

    if (isEvent && !regex.test(postcode)) {
        e.preventDefault();
        alert("Please enter a valid postcode for the event (3–10 characters).");
        document.getElementById('event_postcode').classList.add('is-invalid');
    }
});

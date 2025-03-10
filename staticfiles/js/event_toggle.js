document.getElementById('is_event_related').addEventListener('change', function() {
    const eventFields = document.getElementById('event-fields');
    eventFields.style.display = this.checked ? 'block' : 'none';
});
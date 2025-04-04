document.addEventListener("DOMContentLoaded", function() {
    const eventDateInput = document.getElementById("event_date");
    if (eventDateInput) {
        const now = new Date();
        const pad = (n) => n.toString().padStart(2, '0');
        const localDatetime = `${now.getFullYear()}-${pad(now.getMonth() + 1)}-${pad(now.getDate())}T${pad(now.getHours())}:${pad(now.getMinutes())}`;
        eventDateInput.min = localDatetime;
    }
});
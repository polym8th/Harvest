document.addEventListener("DOMContentLoaded", function() {
    const dropArea = document.getElementById("drop-area");
    const fileInput = document.getElementById("id_image");
    const preview = document.getElementById("preview");

    function handleFile(file) {
        if (!file.type.startsWith("image/")) {
            alert("Only image files (PNG, JPG, GIF) are allowed.");
            return;
        }
        if (file.size > 10 * 1024 * 1024) {
            alert("File size exceeds 10MB limit.");
            return;
        }

        // Update file input for form submission
        const dataTransfer = new DataTransfer();
        dataTransfer.items.add(file);
        fileInput.files = dataTransfer.files;

        // Show preview
        preview.innerHTML = `<img src="${URL.createObjectURL(file)}" style="max-width: 200px; margin-top: 10px;">`;
    }

    fileInput.addEventListener("change", function(e) {
        if (e.target.files.length > 0) {
            handleFile(e.target.files[0]);
        }
    });

    dropArea.addEventListener("dragover", function(e) {
        e.preventDefault();
        dropArea.style.borderColor = "blue"; // Highlight on drag
    });

    dropArea.addEventListener("dragleave", function() {
        dropArea.style.borderColor = "#ccc"; // Reset border color
    });

    dropArea.addEventListener("drop", function(e) {
        e.preventDefault();
        dropArea.style.borderColor = "#ccc";
        if (e.dataTransfer.files.length > 0) {
            handleFile(e.dataTransfer.files[0]);
        }
    });
});
document.addEventListener("DOMContentLoaded", function() {
    // Preview image before upload
    document.getElementById('id_image').addEventListener('change', function(e) {
        const preview = document.getElementById('preview');
        preview.innerHTML = '';
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                const img = document.createElement('img');
                img.src = e.target.result;
                img.style.maxWidth = '200px';
                img.style.marginTop = '10px';
                preview.appendChild(img);
            };
            reader.readAsDataURL(file);
        }
    });
});

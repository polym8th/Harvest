document.addEventListener('DOMContentLoaded', function() {
    const dropArea = document.getElementById('drop-area');
    const imageInput = document.getElementById('id_image');
    const preview = document.getElementById('preview');
    const form = imageInput ? imageInput.closest('form') : null;

    if (!dropArea || !imageInput || !preview || !form) return;

    // Prevent default drag behaviors
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, preventDefaults, false);
        document.body.addEventListener(eventName, preventDefaults, false);
    });

    // Highlight drop zone when item is dragged over it
    ['dragenter', 'dragover'].forEach(eventName => {
        dropArea.addEventListener(eventName, highlight, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, unhighlight, false);
    });

    // Handle dropped files
    dropArea.addEventListener('drop', handleDrop, false);

    // Handle file input change
    imageInput.addEventListener('change', function(e) {
        handleFiles(this.files);
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    function highlight(e) {
        dropArea.classList.add('highlight');
    }

    function unhighlight(e) {
        dropArea.classList.remove('highlight');
    }

    function handleDrop(e) {
        const dt = e.dataTransfer;
        const files = dt.files;

        if (files.length > 0) {
            imageInput.files = files;
            handleFiles(files);
        }
    }

    function handleFiles(files) {
        if (!files || files.length === 0) return;

        const file = files[0];
        
        // Check if file is an image
        if (!file.type.startsWith('image/')) {
            alert('Please upload an image file (PNG, JPG, GIF)');
            imageInput.value = ''; // Clear the input
            preview.innerHTML = '';
            return;
        }

        // Check file size (10MB max)
        if (file.size > 10 * 1024 * 1024) {
            alert('Please upload an image smaller than 10MB');
            imageInput.value = ''; // Clear the input
            preview.innerHTML = '';
            return;
        }

        // Show preview
        preview.innerHTML = '';
        const img = document.createElement('img');
        img.src = URL.createObjectURL(file);
        img.style.maxWidth = '200px';
        img.style.marginTop = '10px';
        preview.appendChild(img);

        // Clean up object URL after image loads
        img.onload = () => {
            URL.revokeObjectURL(img.src);
        };
    }

    // Handle form submission
    form.addEventListener('submit', function(e) {
        if (!imageInput.files || imageInput.files.length === 0) {
            e.preventDefault();
            alert('Please select an image for your article');
            return;
        }
    });
}); 
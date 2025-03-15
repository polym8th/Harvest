console.log("CKEditor script loaded!");  // ✅ Check if script loads

document.addEventListener("DOMContentLoaded", function () {
    let editorElement = document.querySelector("#id_content");
    if (!editorElement) {
        console.error("❌ CKEditor: #id_content not found!");
        return;
    }

    ClassicEditor.create(editorElement, {
        toolbar: [
            'heading', '|', 'bold', 'italic', 'underline', '|',
            'bulletedList', 'numberedList', '|', 'blockQuote',
            'insertTable', 'undo', 'redo', '|', 'imageUpload'
        ]
    }).catch(error => {
        console.error("CKEditor initialization error:", error);
    });
});

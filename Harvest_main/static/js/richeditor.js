// jshint esversion: 8
/* global ClassicEditor */

console.log("CKEditor script loaded!");  // ✅ Confirm script loads

document.addEventListener("DOMContentLoaded", function () {
    if (typeof ClassicEditor === "undefined") {
        console.error("❌ CKEditor is not loaded! Check the script order.");
        return;
    }

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

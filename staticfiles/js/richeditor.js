// jshint esversion: 8
/* global ClassicEditor */

console.log("CKEditor script loaded!");

document.addEventListener("DOMContentLoaded", function () {
    if (typeof ClassicEditor === "undefined") {
        console.error("CKEditor is not loaded! Check the script order.");
        return;
    }

    let editorElement = document.querySelector("#id_content");
    if (!editorElement) {
        console.error("CKEditor: #id_content not found!");
        return;
    }

    ClassicEditor.create(editorElement, {
        toolbar: [
            'heading', '|', 'bold', 'italic', 'underline', '|',
            'bulletedList', 'numberedList', '|', 'blockQuote',
            'insertTable', 'undo', 'redo' // removed 'imageUpload'
        ]
    }).then(editor => {
        editorElement.ckeditorInstance = editor;

        const form = editorElement.closest("form");
        if (form) {
            form.addEventListener("submit", function (e) {
                const content = editor.getData().trim();

                // Block form submission if content is empty
                if (!content) {
                    e.preventDefault();
                    alert("The article content is required.");
                    return false;
                }

                // Push editor content back into the hidden textarea
                editorElement.value = content;
            });
        }
    }).catch(error => {
        console.error("CKEditor initialization error:", error);
    });
});

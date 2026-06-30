// Simple validation
document.querySelector('form').addEventListener('submit', function(e) {
    const text = document.getElementById('text').value.trim();
    if (!text) {
        alert('Please enter some text to summarize.');
        e.preventDefault();
    }
});

function updateLength() {
    const text = document.getElementById('text').value || '';
    const wordCount = text.trim().split(/\s+/).filter(Boolean).length;
    document.getElementById('count').textContent = wordCount;
}

window.addEventListener('DOMContentLoaded', function() {
    updateLength();
    // Scroll to result if one exists
    const result = document.querySelector('.result');
    if (result) {
        setTimeout(() => {
            result.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 100);
    }
});

// Reset form functionality
function resetForm() {
    document.getElementById('text').value = '';
    updateLength();
}

// Paste functionality
function pasteText() {
    navigator.clipboard.read()
        .then(items => {
            for (let item of items) {
                if (item.types.includes("text/plain")) {
                    item.getType("text/plain").then(blob => {
                        blob.text().then(text => {
                            document.getElementById('text').value += text;
                            updateLength();
                        });
                    });
                }
            }
        })
        .catch(err => {
            // Fallback: try the older API
            if (navigator.clipboard && navigator.clipboard.readText) {
                navigator.clipboard.readText().then(text => {
                    document.getElementById('text').value += text;
                    updateLength();
                });
            }
        });
}

// File upload functionality
document.getElementById('fileInput').addEventListener('change', function(e) {
    const file = e.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(event) {
            document.getElementById('text').value = event.target.result;
            updateLength();
        };
        reader.readAsText(file);
    }
});

// Toggle buttons for format
document.querySelectorAll('.toggle-btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelectorAll('.toggle-btn').forEach(b => b.classList.remove('active'));
        this.classList.add('active');
    });
});
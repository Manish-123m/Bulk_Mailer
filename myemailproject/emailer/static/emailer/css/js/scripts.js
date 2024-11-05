// emailer/static/emailer/js/scripts.js
document.querySelector('form').addEventListener('submit', function() {
    const button = document.querySelector('button');
    button.disabled = true;
    button.textContent = 'Sending...';
});

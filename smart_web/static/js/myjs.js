function handleLanguageSelection() {
    var select = document.getElementById('languageSelect');
    
    select.addEventListener('change', function () {
        var selectedLanguage = this.value;
        
        if (selectedLanguage === 'en') {
            window.location.href = 'index.html'; // Replace with your English page URL
        } else if (selectedLanguage === 'es') {
            window.location.href = 'index_es.html'; // Replace with your Spanish page URL
        }
    });
}

// Call the function when the DOM is loaded
document.addEventListener('DOMContentLoaded', function () {
    handleLanguageSelection();
});

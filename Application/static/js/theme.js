document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.querySelector('.theme-toggle');
    const body = document.body;
    // Theme Toggle
    let isDarkMode = localStorage.getItem('darkMode') === 'true';

    // Set initial theme
    if (isDarkMode) {
        body.setAttribute('data-theme', 'dark');
        themeToggle.querySelector('i').classList.remove('fa-moon');
        themeToggle.querySelector('i').classList.add('fa-sun');
    }

    themeToggle.addEventListener('click', () => {
        isDarkMode = !isDarkMode;
        localStorage.setItem('darkMode', isDarkMode);

        if (isDarkMode) {
            body.setAttribute('data-theme', 'dark');
            themeToggle.querySelector('i').classList.remove('fa-moon');
            themeToggle.querySelector('i').classList.add('fa-sun');
        } else {
            body.removeAttribute('data-theme');
            themeToggle.querySelector('i').classList.remove('fa-sun');
            themeToggle.querySelector('i').classList.add('fa-moon');
        }
    });
});

function adjustPageWidth() {
    const screenWidth = window.innerWidth;
    const body = document.body;
  
    if (screenWidth >= 992 && screenWidth <= 1600) {
      body.style.transform = 'scale(0.9)';
    } else if (screenWidth >= 700 && screenWidth <= 767) {
      body.style.transform = 'scale(0.8)';
    } else if (screenWidth >= 600 && screenWidth < 700) {
      body.style.transform = 'scale(0.75)';
    } else if (screenWidth <= 600) {
      body.style.transform = 'scale(0.5)';
    } else {
      body.style.transform = 'none'; // Reset scaling if no conditions match
    }
  }
  
  // Call the function on window resize
  // window.addEventListener('resize', adjustPageWidth);
  
  // adjustPageWidth();
  
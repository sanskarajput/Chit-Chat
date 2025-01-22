document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.querySelector('.menu-toggle');
    const inputBox = document.querySelector('input');
    const leftMenu = document.querySelector('.left-menu');
    const navLinks = document.querySelector('.nav-links');
    
  
    // Menu Toggle
    menuToggle.addEventListener('click', () => {
        leftMenu.classList.toggle('active');
        if (document.innerWidth < 768) {
            menuToggle.querySelector('i').classList.toggle('fa-times');
            menuToggle.querySelector('i').classList.toggle('fa-bars');
        }
    });
  
    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!leftMenu.contains(e.target) && 
            !menuToggle.contains(e.target) && 
            window.innerWidth < 768) {
            leftMenu.classList.remove('active');
            navLinks.classList.remove('active');
            if (document.innerWidth < 768) {
                menuToggle.querySelector('i').classList.add('fa-bars');
                menuToggle.querySelector('i').classList.remove('fa-times');
            }
        }
    });
  
    // Handle window resize 
    let resizeTimer;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(() => {
            if (window.innerWidth >= 768) {
                leftMenu.classList.remove('active');
                navLinks.classList.remove('active');
                if (document.innerWidth <= 768) {
                    menuToggle.querySelector('i').classList.remove('fa-times');
                    menuToggle.querySelector('i').classList.add('fa-bars');
                }
            }
        }, 250);
    });
  
    // Add smooth scrolling to all links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
                // Close mobile menu after clicking a link
                if (window.innerWidth < 768) {
                    leftMenu.classList.remove('active');
                    navLinks.classList.remove('active');
                }
            }
        });
    });

    // filter functionality
    inputBox.addEventListener("input", (e) => {
        const searchQuery = e.target.value.toLowerCase();
        const all_lis = leftMenu.querySelectorAll("li");
        all_lis.forEach((li) => {
            const text = li.textContent.toLowerCase();
            if (text.includes(searchQuery)) {
                li.style.display = "inline";
            } else {
                li.style.display = "none";
            }
        })
        
    })
  });


  const chatting_with_element = document.getElementById('chatting-with'); 
  if (chatting_with_element) {
    chatting_with_element.scrollIntoView({
        behavior: 'smooth', // Smooth scrolling
        block: 'center'
    });
  }
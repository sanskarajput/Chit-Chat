 // Form toggling
 const toggleSwitch = document.querySelector('.toggle-switch');
 const toggleSpans = toggleSwitch.querySelectorAll('span');
 const signInForm = document.getElementById('signInForm');
 const signUpForm = document.getElementById('signUpForm');

 if (title === 'Sign Up') {
     toggleSwitch.classList.add('sign-up');
     toggleSpans[1].classList.add('active');
     signUpForm.classList.add('active');
     document.title = 'Sign Up';
 } else if (title === 'Sign In'){
     toggleSpans[0].classList.add('active');
     signInForm.classList.add('active');
     document.title = 'Sign In';
 }


 toggleSwitch.addEventListener('click', () => {
     toggleSwitch.classList.toggle('sign-up');
     toggleSpans.forEach(span => span.classList.toggle('active'));
     signInForm.classList.toggle('active');
     signUpForm.classList.toggle('active');
     // change page title
     document.title = toggleSwitch.classList.contains('sign-up')? 'Sign Up' : 'Sign In';
 });

 // Form validation
 const forms = document.querySelectorAll('form');
 forms.forEach(form => {
     form.addEventListener('submit', (e) => {
         
         if (form.parentElement.id === 'signUpForm') {
             const password = document.getElementById('password').value;
             const confirmPassword = document.getElementById('confirmPassword').value;
             
             if (password !== confirmPassword) {
                 alert('Passwords do not match!');
                 e.preventDefault();
                 return;
             }
         }
         
         console.log('Form submitted:', form.parentElement.id);
     });
 });
// validation.js

function validateForm(event) {
    var password = document.getElementById("password").value;
    var email = document.getElementById("email").value;
  
    // Perform checks on password and email
    if (!validatePassword(password)) {
      alert("Password must be at least 8 characters long");
      event.preventDefault(); // Prevent form submission
    }
  
    if (!validateEmail(email)) {
      alert("Invalid email address");
      event.preventDefault(); // Prevent form submission
    }
  }
  
  // Function to validate email using regular expression
  function validateEmail(email) {
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
  }
  
   
  // Function to validate email using regular expression
  function validatePassword(password) {
    return password.length >= 8;
  }
  

 var password = document.getElementById("password")
  , c_password = document.getElementById("c_password");

function validatePassword(){
  if(password.value != c_password.value) {
    c_password.setCustomValidity("Passwords Don't Match");
  } else {
    c_password.setCustomValidity('');
  }
}

password.onchange = validatePassword;
c_password.onkeyup = validatePassword;
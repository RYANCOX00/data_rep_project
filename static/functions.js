
//Block of code taken from: https://stackoverflow.com/questions/59704712/form-for-validation-and-open-link-in-same-page-->
function validateForm(){  // Javascript function
    var email = document.getElementById('email').value;  // saving the email address as a variable
    var password = document.getElementById('password').value;  // saving the password address as a variable
    if (email == 'user@finance.ie' && password == 'password'){  // if the email and password match the required login details
        document.getElementById('sucess').innerHTML = 'sucessful login';  // print 'sucessful login' in success paragraph. 
        
        
        window.location.href = 'main.html'   // redirect the page to the main page. 
        return false;} 
        
        else {document.getElementById('error').innerHTML = 'invalid credentials';  // otherwise if login is not successful, print 'invalid credentials'. 
        return false;}}

// end of reference
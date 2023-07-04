document.getElementById('signupForm').addEventListener('submit', function(e) {
    // Prevent the default form submission
    e.preventDefault();

    // Get form data
    var username = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    // Send a POST request to the API
    axios({
        method: 'post',
        url: 'http://localhost:8002/users/signup',
        data: {
            username: username,
            password: password,
            email: email
            // Add more fields as necessary
        }
    })
    .then(function (response) {
        // Handle success here
        console.log(response);
        alert('User created successfully');
    })
    .catch(function (error) {
        // Handle error here
        console.log(error);
        alert('An error occurred');
    });
});
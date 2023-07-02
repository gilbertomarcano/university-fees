document.getElementById('submit').onclick = function() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    axios.post('http://localhost:8002/users/auth', {
        username: username,
        password: password
    })
    .then(function (response) {
        alert("Login successful!");

        // Save the token to local storage
        localStorage.setItem('token', response.data.token);

        // Redirect to the users page
        window.location.href = "users.html";

    })
    .catch(function (error) {
        console.log(error);
        alert("Login failed!");
    });
};
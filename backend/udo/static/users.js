window.onload = function() {
    var token = localStorage.getItem('token');

    axios.get('http://localhost:8002/users/me', {
        headers: {
            'Authorization': 'Token ' + token
        }
    })
    .then(function (response) {
        document.getElementById('username').innerText = 'Username: ' + response.data.username;
        document.getElementById('first_name').innerText = 'First Name: ' + response.data.first_name;
        document.getElementById('last_name').innerText = 'Last Name: ' + response.data.last_name;
        document.getElementById('email').innerText = 'Email: ' + response.data.email;
    })
    .catch(function (error) {
        console.log(error);
        alert("Failed to load user info!");
    });

    document.getElementById('logout').onclick = function() {
        axios.post('http://localhost:8002/users/logout', {}, {
            headers: {
                'Authorization': 'Token ' + token
            }
        })
        .then(function (response) {
            // Clear the token from local storage
            localStorage.removeItem('token');

            // Redirect to the login page
            window.location.href = "login.html";
        })
        .catch(function (error) {
            console.log(error);
            alert("Logout failed!");
        });
    };
};
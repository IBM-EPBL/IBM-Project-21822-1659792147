
</body><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta name="Description" content="Enter your description here"/>
    <!-- Favicons -->
    <link href="{{ url_for('static', filename='/favicon.ico') }}" rel="icon">

    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Overpass">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.6.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <link rel="stylesheet" href="{{ url_for('static', filename='assets/css/style.css') }}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
    <title>News Tracker Application</title>
</head>

<body style="height: 685px; background-color:#1e1e21;">

    {% block navbar %}

    <div class="container-fluid" style="background-color: #000;">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top shadow-sm">

            <!--  Show this only on mobile to medium screens  -->
              <a class="navbar-brand d-lg-none" href="{{ url_for('home') }}"><b class="lg"><span class="logo">News Tracker</span>&nbsp;Application</b></a>
            
              <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
            
            <!--  Use flexbox utility classes to change how the child elements are justified  -->
              <div class="collapse navbar-collapse justify-content-between" id="navbarToggle">
            
                <ul class="navbar-nav">

                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-expanded="false">
                          Categories
                        </a>
                        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                          <a class="dropdown-item" href="{{ url_for('business') }}">Business</a>
                          <a class="dropdown-item" href="{{ url_for('tech') }}">Technology</a>
                          <a class="dropdown-item" href="{{ url_for('entertainment') }}">Entertainment</a>
                          <a class="dropdown-item" href="{{ url_for('science') }}">Science</a>
                          <a class="dropdown-item" href="{{ url_for('sports') }}">Sport</a>
                          <a class="dropdown-item" href="{{ url_for('health') }}">Health</a>
                        </div>
                    </li>
                </ul>
                
                
            <!--   Show this only lg screens and up   -->
                <a class="navbar-brand d-none d-lg-block" href="{{ url_for('home') }}"><b class="lg"><span class="logo">News Tracker</span>&nbsp;Application</b></a>
                
                
                
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="/">
                            Home
                        </a>
                    </li>
                </ul>
            </div>
        </nav>
    </div>

    {% endblock %}

    <<div class="container py-5" style="height:100%;">
        <div class="row">
            <div class="col-lg-5 col-md-8 mx-auto shadow rounded-5 " style="margin:15% 0; padding:20px; border-radius:10px;">
                <h2 class="text-center fw-bold mb-3 p-2">Account</h2>

                <div class="persons" style="height:200px;">
                    <div class="details">

                    </div>
                </div>
            </div>
        </div>
    </div>



    <div class="container-fluid footer">
        <p class="text-center footer-text">
            © <span class="logo">News Tracker</span> Application by PNT2022TMID22300 
        </p>
    </div>


    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.1/umd/popper.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.6.0/js/bootstrap.min.js"></script>    
    <script>

        const main = document.querySelector('.persons');
    
        function isUserLoggedIn(){
            const isUser = JSON.parse(localStorage.getItem('isLoggedIn'));
            if(isUser){
                const userData = JSON.parse(localStorage.getItem('user'));
    
                main.innerHTML = `
                    <div class="details">
                        <h3 class="text-center fw-bold mb-3 p-2">Welcome ${userData.name}</h3>
                        <p class="text-center fw-bold mb-3 p-2">Your email is ${userData.email}</p>
                        <div class="sign_btn_da" style="text-align:center;">
                            <a class="btn" id="logout_btn" style="margin:20px; font-size: 15px; color:#fff;">Log out</a>
                        </div>
                    </div>
                `;
                console.log(userData);
    
            }else{
                location.href = "/login";
            }
        }
    
        window.addEventListener('load', isUserLoggedIn);
    
        window.onload = function(){
            const logoutbtn = document.querySelector('.btn');
            logoutbtn.addEventListener('click', function logOutUser(event){
                localStorage.clear();
                location.reload();
            });    
        }
    
    </script>
</html>

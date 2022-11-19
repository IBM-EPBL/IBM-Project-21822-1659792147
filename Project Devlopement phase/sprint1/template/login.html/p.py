[6:02 pm, 19/11/2022] Gopika 🐒: {% extends 'base.html' %}

{% block content %}

<div class="container-fluid landing">
    <div class="row">
        {% for source, title, desc, author, img, p_date, url in articles %}
            <div class="col-md-4 d-flex justify-content-center">
                <div class="card mb-3 bg-dark text-white">
                    <img src="{{ img }}" class="card-img image-fluid" alt="...">
                    <div class="card-body">
                        <p class="card-text source">{{ source.name }}</p>
                        <a href="{{ url }}">
                            <h2 class="card-title"><b> {{ title }} </b></h2>
                        </a>
                        <p class="card-text">{{ desc }}</p>
                        <p class="card-text"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(255, 255, 255, 1);transform: ;msFilter:;"><path d="M12 2C6.579 2 2 6.579 2 12s4.579 10 10 10 10-4.579 10-10S17.421 2 12 2zm0 5c1.727 0 3 1.272 3 3s-1.273 3-3 3c-1.726 0-3-1.272-3-3s1.274-3 3-3zm-5.106 9.772c.897-1.32 2.393-2.2 4.106-2.2h2c1.714 0 3.209.88 4.106 2.2C15.828 18.14 14.015 19 12 19s-3.828-.86-5.106-2.228z"></path></svg> Author: {{ author }}</p>
                    </div>
                    <div class="card-footer">
                        <p class="card-text published"><svg class="p-svg" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(255, 255, 255, 1);transform: ;msFilter:;"><path d="M12 5c-4.411 0-8 3.589-8 8s3.589 8 8 8 8-3.589 8-8-3.589-8-8-8zm0 14c-3.309 0-6-2.691-6-6s2.691-6 6-6 6 2.691 6 6-2.691 6-6 6z"></path><path d="M11 9h2v5h-2zM9 2h6v2H9zm10.293 5.707-2-2 1.414-1.414 2 2z"></path></svg> Date Published: {{ p_date }}</p>
                    </div>
                </div>
            </div>
        {% endfor %}
    </div>
</div>

{% endblock %}
[6:03 pm, 19/11/2022] Gopika 🐒: <!DOCTYPE html>
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
                    <!-- <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('headlines') }}">Headlines</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link"href="{{ url_for('articles') }}">Articles</a>
                    </li> -->
                    <!-- <li class="nav-item">
                        <a class="nav-link"href="{{ url_for('sources') }}">Sources</a>
                    </li> -->
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
                <h2 class="text-center fw-bold mb-3 p-2">Log in</h2>
                <form name="google-sheet">
                    <div id="form_alerts"></div>
                    <div class="form-group mb-3">
                        <label for="email" class="form-label">Email</label>
                        <input type="email" id="email" name="email" class="form-control" placeholder="Enter your email address" required>
                    </div>
                    <div class="form-group mb-3">
                        <label for="password" class="form-label">Password</label>
                        <input type="password" id="password" name="password" class="form-control" placeholder="Enter your password" required>
                    </div>
                
                    <div style="text-align:center ;" >
                        <button class="an" type="submit">Login</button><br>
                        Don't have an account? <a href="/register">Sign Up</a>
                    </div>
                </form>
            </div>
        </div>
    </div>



    <div class="container-fluid footer">
        <p class="text-center footer-text">
            © <span class="logo">News Tracker</span> Application by PNT2022TMID22300 
        </p>
    </div>

    <script>
        
        const scriptURL = "aHR0cHM6Ly9zY3JpcHQuZ29vZ2xlLmNvbS9tYWNyb3Mvcy9BS2Z5Y2J6M1dYSHlUSV95eXNvc1pOQm1ITnpZbVZnMWNaNHBib08zS0t1Nkx1OHdPUHpSeTJ3b21BQVlKSVBpbEtkdWI2b0gvZXhlYw==";
        const form = document.forms['google-sheet']
        // console.log(mail,pass)
        
        form.addEventListener('submit', e => {
            e.preventDefault()
            fetch(atob(scriptURL))
            .then((response) => {
                return response.json()
                // if(response.status == 200){
                //     // window.location.href = "/home"
                // }
            })
            .then((data) => {

                function storeUserInfo(i){
                    const userName = data[i][0];
                    const userEmail = data[i][1];
                    const userRole = "User";
                    const userDisability = "None";
                    console.log(userName,userEmail,userRole,userDisability)
            
                    if(userName == "" || userEmail== "" || userRole == "" || userDisability == ""  ){
                        alert("Please enter the details");
                    }else{
                        userInfo = {
                            name: userName,
                            email: userEmail,
                            role: userRole,
                            disability: userDisability
                        }
                        localStorage.setItem('isLoggedIn', true);
                        localStorage.setItem('user', JSON.stringify(userInfo));
                        //alert("Login Successful");
                        //window.location.href = "/";
                    }
                }

                var ok = 0;
                const inputEmail= document.querySelector('#email').value;
                const inputPassword = document.querySelector("#password").value;
                for(var i=1;i<data.length;i++)
                {
                    if(data[i][1] == inputEmail && data[i][2] == inputPassword)
                    {
                        ok=0;
                        storeUserInfo(i);
                        if(true)
                        {
                            $("#form_alerts").html("<div class='alert alert-success'>Sign in successfully.</div>");

                            setInterval(function(){
                                window.location.href = "/"
                            }, 1000);
                            //window.location.href = "/home" 
                            break;
                        }
                    }
                    else{
                        console.log("Failure");
                        console.log(inputEmail);
                        ok=1;
                    }
                    }

                if(ok==1){
                    $("#form_alerts").html("<div class='alert alert-danger'>Account not found</div>");
                }
                    
            })
        })

    </script>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.1/umd/popper.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.6.0/js/bootstrap.min.js"></script>
</body>
</html>

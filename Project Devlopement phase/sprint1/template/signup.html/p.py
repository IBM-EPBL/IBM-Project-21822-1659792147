<!DOCTYPE html>
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

    <div class="container py-5 " style="height:100%;">
        <div class="row">
            <div class="col-lg-5 col-md-8 mx-auto shadow rounded-5" style="margin:10% 0; padding:20px; border-radius:10px;">
                <h2 class="text-center fw-bold mb-3">Sign up</h2>
                <form name="google-sheet">
                    <div id="form_alerts"></div>
                    <div class="form-group mb-3">
                        <label for="name" class="form-label">Name</label>
                        <input type="text" id="name" name="name" class="form-control" placeholder="Enter your name" required>
                    </div>
                    <div class="form-group mb-3">
                        <label for="email" class="form-label">Email</label>
                        <input type="email" id="email" name="email" class="form-control" placeholder="Enter your email address" required>
                    </div>
                    <div class="form-group mb-3">
                        <label for="password" class="form-label">Password</label>
                        <input type="password" id="password" name="password" class="form-control" placeholder="Enter your password" required>
                    </div>
                    <div style="text-align:center ;" >
                        <button class="an" type="submit">Sign up</button><br>
                        Already a member? <a href="/login">Login</a>
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
    

    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        

        const scriptURL = "aHR0cHM6Ly9zY3JpcHQuZ29vZ2xlLmNvbS9tYWNyb3Mvcy9BS2Z5Y2J6M1dYSHlUSV95eXNvc1pOQm1ITnpZbVZnMWNaNHBib08zS0t1Nkx1OHdPUHpSeTJ3b21BQVlKSVBpbEtkdWI2b0gvZXhlYw==";
        const form = document.forms['google-sheet']
        
        function send(){
            fetch(atob(scriptURL), { method: 'POST', body: new FormData(form)})
            .then(response => $("#form_alerts").html("<div class='alert alert-success'>Sign up successfully.</div>"))
            .catch(error => $("#form_alerts").html("<div class='alert alert-danger'>Details not sent.</div>"))
        }

        form.addEventListener('submit', e => {
            e.preventDefault()
            fetch(atob(scriptURL))
            .then((response) => {
                return response.json()
            })
            .then((data) => {
                var ok = 0;
                const inputEmail= document.querySelector('#email').value;
                const inputPassword = document.querySelector("#password").value;
                for(var i=1;i<data.length;i++)
                {
                    if(data[i][1] == inputEmail)
                    {
                        ok=0;
                        if(true)
                        {
                            $("#form_alerts").html("<div class='alert alert-danger'>Mail id already exist.</div>");
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
                    $("#form_alerts").html("<div class='alert alert-success'>Sign up successfully</div>");
                    console.log("Failure - Final");
                    send();
                    setInterval(function(){
                        window.location.href = "/login";
                    }, 1000);
                }
                    
            })
        })
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.1/umd/popper.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.6.0/js/bootstrap.min.js"></script>
</body>
</html>

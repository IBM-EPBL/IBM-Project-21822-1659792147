
{% extends 'base.html' %}

{% block content %}

<div class="container-fluid landing">
    <div class="row">
        {% for source, title, desc, author, img, p_date, url in headlines %}
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

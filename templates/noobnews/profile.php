{% extends 'noobnews/base.html' %}
{% load staticfiles %}
{% load crispy_forms_tags %} 
{% block body_block %}

<div class="col-md-6 img">
  <h3 style="color:white;">Profile</h3>
  <br /><br />
</div>

<!------ User picture and description ---------->
<div style="padding-top: 115px;">
  <link
    href="http://fontawesome.io/assets/font-awesome/css/font-awesome.css"
    rel="stylesheet"
    media="screen"
  />

  <div class="container">
    <div class="row user-menu-container square">
      <div class="col-md-7 user-details">
        <div class="row coralbg white">
          <div class="col-md-6 no-pad">
            <div class="user-pad">
              <h4 style="color:black;">
                <i></i> {{ user.userprofile.player_tag }}
              </h4>
              

              
                
                <button type="submit" class="btn btn-labeled btn-info">
                  <span class="btn-label"><i></i></span>Update my picture
                </button>
             
            </div>
          </div>
          <div class="col-md-6 no-pad">
            <div class="user-image">
              <img
                src="{{ user.userprofile.user_profile_image.url }}"
                class="img-responsive thumbnail"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!------ User information updates ---------->

  <div class="content-section">
    <form method="POST"  enctype="multipart/form-data">
      {% csrf_token %}
       <!-- Display each form -->
      

      {{ user_form_update|crispy }}
      {{ profile_form_update|crispy }}
     
      
        <button type="submit" class="btn btn-labeled btn-info">
          <span class="btn-label"><i></i></span>Update user info test
        </button>
     
    </form>
  </div>
</div>
</div>
{% endblock %}

# django-polls

# start： 

  py manage.py runserver 8080   // default `8000`

# background visit: 

  http://127.0.0.1:8080/admin/  //  `admin/django123`

# front-end visit: 

  http://127.0.0.1:8080  // mysite/urls.py config route

# knowledge

  * mysite folder is `django-admin startproject mysite`
      1. polls folder is one functional module
      2. other functional modules
  * polls > static > polls > *.css,*.js 
      1. static is system folder name
      2. second 'polls' is differentiating the application module resources
  * polls > templates > polls > *.html  too
  * mysite > settings.py
      1. LANGUAGE_CODE = 'zh-hans' # default: 'en-us'
      2. TIME_ZONE = 'Asia/Shanghai' # default 'UTC'
      3. ROOT_URLCONF = 'mysite.urls'
  

# history tag

  [before use generic views](https://github.com/camnpr/django-polls/tree/38b694ad0fcb32d368c78f0f528a67b8cd12f324)
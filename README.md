# BookMe
A self bookmarking project for studying.


● You can search books, see the results.<br>
● You can bookmark books that you like.<br>
● You can list your bookmarks.<br>
● You can go into details of your bookmarks.<br>

<b>Prerequisities / Technical Details</b>

Django 2.2.3<br>
Python 3.7<br>
Mysqlclient 1.4.2 <br>
requests 2.22<br>


<b> Installing </b>
<br>
You need to install Python 3.7. 
Django 2.2 and afterwards you need to install
mysqlclient and requests.

In Ubuntu, Mint and Debian you can install Python 3 like this:

```
$ sudo apt-get install python3 python3-pip
```

For other Linux flavors, macOS and Windows, packages are available at

http://www.python.org/getit/

For Django you can use this line

```
$ pip install Django
```

You can find further information about Django

https://docs.djangoproject.com/en/2.2/topics/install/

Use the package manager pip to install mysqlclient and requests.

```
$ pip install mysqlclient
$ pip install requests
```

You'll also need internet connection for mysql server.


<br>
<b> Database Informations </b> 
<br>
```
'NAME':'lyEBWxgVhU',
'USER': 'lyEBWxgVhU',
'PASSWORD': 'TJdReyYGjs',
'HOST': '37.59.55.185',
 #'remotemysql.com'
 'PORT': '3306'
 ```
 <br>
 <b>IMPORTANT</b>

For development at mybooklist/settings.py -> DEBUG must be set to TRUE
<br>
(It left as true)

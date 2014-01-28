Healthfun
---------

A little Django-webapplication, collecting generic health data like
weight and blood pressure to have a better overview.

i18n/l10n or update of translations
===================================

Healthfun is fully enabled to be translated into different 
lanaguages. Based on user'S browsers settings the language used in 
user interface can be localized. 

To add a new translation run 

	$ django-admin.py makemessages -l xx
	
where you replace xx with your locale -- e.g. de. You can use the 
same command to update an already existing. Having this done, you 
will find updated catalog under local/xx/LC_MESSAGES/django.po, 
which you might like to open in any editor like Geany or poedit to 
update translations. j

After this has been done you should compile the messages:

	$ python manage.py compilemessages

and restart your application. 

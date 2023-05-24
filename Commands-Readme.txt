* Install ‘djangorestframework’ and ‘psycopg2-binary’ modules before running the code. For this use the following commands. 

	  pip install djangorestframework 
	  pip install psycopg2-binary

* Use the following commands for database migrations.

	 python3 manage.py makemigrations
	 python3 manage.py migrate

* Use the following command to run the server
	
	python3 manage.py runserver


* Mandatory: Before final submission run the following commands to execute testcases

   	python3 manage.py test notesapp.test.test_functional
   	python3 manage.py test notesapp.test.test_exceptional
   	python3 manage.py test notesapp.test.test_boundary


* To ensure your code is saved and available for later use, remember to use the CTRL+Shift+B command on your code IDE.
   This will push or save the updated contents in the internal git/repository.
   It is also important to use CTRL+Shift+B before the final submission to evaluate the code quality.
# Technicolor Backend Technical Test Applicant Submission: David Dilley
This is in response to the test sent in image format to dilley.david@gmail.com from Victoria.Xiong-Gnandt@technicolor.com with subject 'Backend Coding Test'.

## Clone this project repo
	> cd path/to/project/root
	> git clone --bare https://github.com/ddilley/technicolor-test.git

## Installation
	> Installation is possible with pip and easy_install and can be done in a virtual environment.
	> easy_install pip # if you don't already have pip installed

	## Install Sass
		> gem install sass

	## set up and activate virtualenv:
		> https://virtualenv.pypa.io/en/latest/installation.html

	## after installing venv:
		> cd path/to/parent/venv/dir
		> virtualenv venv
		> source ath/to/parent/venv/dir/venv/bin/activate

	## install dependencies within venv:
		> cd path/to/project/root
		> pip install -r requirements.txt

	## Install and run mongodb:
		> if you need to install mongo: http://www.mkyong.com/mongodb/how-to-install-mongodb-on-mac-os-x/
		## make sure mongo is running:
			> mongod
			> -or-
			> mongo

## run this project
	> cd path/to/project/root
	> python runsite.py
	> open your browser and navigate to 127.0.0.1:5000


## Technologies Used
	Python:
		I chose Python because it is my most seasoned language. For any given project that is not a test, compiled languages VS scripting languages would be weighed for pros and cons.
	Flask:
		I chose Flask as a framework because it is a micro framework which affords the ability to choose smaller grranu;les of imported functionality than a 'macro' framework (such as Django) and so seemed appropriate for a small app like this.
	Jinja2:
		I chose Jinja2 templating because I chose Python as the scripting language and Jinja2 has pythonic (and therefore complementing) syntax.
	JQuery:
		I chose JQuery for this project for it's ease of use and friendly syntax. IT came in handy for the ajax functionalities.
	Mongo:
		I chose MongoDB (using module PyMongo) because I recently began reading and learning about it and I wanted to see what it was like to use a not-only-SQL database.

## Endpoint versioning ("The endpoints would need to support versioning, please describe how to accomplish this"):
	We could have each version installed and running within different directories. Each could listen on a different localhost port or unix socket. The routes on versions would not need to have versions embedded. For example, both can have a /users endpoint. We could then tie everything together with a reverse proxy (like ngix) which exposes the apis with external URLs that use versioning which maps /[version]/end-point to the version's server. Example: /v1.0/account mapped to v1.0 server and /v1.1/account) mapped to the v1.1 server. Another option is to have your v1.1 server respond to both the v1.1 endpoints and the v1.0 endpoints.

## Pagination Support
	A possible pagination solution for endpoints that display result sets such as /users:
		Since MongoDB and PyMongo are being used, pagination would be pretty simple using PyMongo syntax.
		We would use .find() to get and possibly filter the initial result set. Then skip the cursor returned from that
		by (page number multiplied by number of results) and limit that by a n_per_page param.
		Below is an example of this on the user object:
			function printUsersWithPagination(page_number, n_per_page) {
			   print("Page: " + page_number);
			   ret = db.users.find().skip(
			   		(page_number-1)*n_per_page).limit(
			   			n_per_page
			   		)
			   	);
			   	for user in ret:
			   		print(user.city+': '+user.gender)
			}

	# Must consider everything related to the rebase process
	# and any extra step for this proyect.

	# Activate Virtualenv
	source ../../bin/activate

	# pull changes from git
	printf "\n > Pulling changes from git ...\n\n"
	git pull origin main

	# update pip
	printf "\n > Updating pip ...\n\n"
	pip install --upgrade pip
	# install new dependencies
	printf "\n > Updating python libraries ...\n\n"
	pip install -r requirements.txt

	printf "\n > Updating django models ...\n\n"
	python manage.py migrate
	
	# collect statics
	printf "\n > Updating static files ...\n\n"
	echo yes | python manage.py collectstatic

	# restart gunicorn
	printf "\n > Restarting djangoapp ...\n\n"
	sudo supervisorctl restart djangoapp	
	printf "\n > APP RESTARTED ...\n\n"

	# Deactivate Virtualenv
	deactivate

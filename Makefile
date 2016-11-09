shell:
	python wef/manage.py shell_plus

clean:
	find ./ -type f -name "\.*swp" -delete
	find ./ -type f -name "\.*swo" -delete
	find . -name "*.pyc" -exec rm -rf {} \;

function:
	python wef/manage.py test functional_test

unnit:
	python wef/manage.py test users

migrate:
	python wef/manage.py makemigrations users items
	python wef/manage.py migrate

collectstatic:
	python wef/manage.py collectstatic --noinput

productcollectstatic:
	python wef/manage.py collectstatic --settings=wef.settings.production

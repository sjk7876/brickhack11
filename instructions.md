You need two terminals open.

In one, run `pip install -r requirements.txt` (if you haven't done so)

Then run `py manage.py tailwind install` (if you haven't done so)

Then cd into your theme/static_src directory, and run `npm i`, to make sure you install all the npm dependencies

Then run `py manage.py tailwind start`

In two, run `py manage.py runserver` and open the URL provided
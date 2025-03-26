Descriptions:
Streamo is a Video streaming platform copy that allows users to register accounts, login, view collection of movies/shows, and add entries to favorites.

Steps to Set up Environment:

1. Open a Command terminal with anaconda and change directory to where these files are stored on your system.
2. Run 'conda create -n streamoflaskenv python=3.12' and type 'y' to proceed
3. 'activate streamoflaskenv' on windows or 'source activate streamoflaskenv' on Mac
4. pip install -r requirements.txt

Steps to Run Website: (Into the terminal type each of the following and press enter between)

1. set FLASK-APP=app.py
2. flask db init
3. flask db migrate -m "first migration"
4. flask db upgrade
5. python populate_database.py
6. python app.py

How to use Website:
You will start out on the Homepage and you can traverse to the login or register pages at the top of the page.
Once you register an account using a Username and Password, you can login using the combination of those two features.
Now as a verified user, you can see the navigation for catalog and favorites pages as well as logout. Once you login you will be directed to the catalog page where you can search and filter for movies and shows as well as click on specific title's to see that content's detail page.
On the detail page you can see the information about a title and add it to your favorites.
On the favorites page you will see a carousel of all the items you have added to your favorites. Here you can remove remove from your favorites.
Navigating to the Logout page will sign you out of the website and you will have to login again or create a new account to view the websites features again.

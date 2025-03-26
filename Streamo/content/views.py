from flask import render_template,url_for,flash,request,redirect,Blueprint
from flask_login import current_user,login_required
from Streamo import db
from Streamo.models import Movies_Show, Favorite

content = Blueprint('content',__name__)

# Content Detail
@content.route('/<title>',methods=['GET','POST'])
@login_required
def detail(title):
    film = Movies_Show.query.get_or_404(title)
    
    if request.method=='POST':
        existing_fav = Favorite.query.filter_by(user_id=current_user.id,movie_title=title).first()
        if existing_fav:
            flash('Already in Favorites')
        else:
            fav = Favorite(user_id=current_user.id,movie_title=title)
            db.session.add(fav)
            db.session.commit()
            flash('Added ' +title + ' to Favorites')
            return redirect(url_for('content.detail',title=title))

    return render_template('detail.html',title=film.title,genre=film.genre,description=film.description,release=film.release,duration=film.duration,poster=film.poster)

# Favorites
@content.route('/<int:user_id>',methods=['GET','POST'])
@login_required
def favorites(user_id):
    favorites = Favorite.query.filter_by(user_id=user_id).all()
    
    films = []
    
    for fav in favorites:
        film = Movies_Show.query.get(fav.movie_title)
        films.append(film)

    if request.method=='POST':
        
        title = request.form.get('remove_favorite')

        # Only one entry will be present with this combination of user_id and movie_title
        removing = Favorite.query.filter_by(user_id=user_id,movie_title=title).first()

        db.session.delete(removing)
        db.session.commit()
        flash('Removed '+title+' From Favorites')
        film_to_remove = Movies_Show.query.get(title)
        films.remove(film_to_remove)

        return redirect(url_for('content.favorites',user_id=current_user.id,films=films))


    return render_template('favorites.html',user_id=current_user.id,films=films)

# Catalog
@content.route('/catalog',methods=['GET','POST'])
@login_required
def catalog():
    movies_shows = Movies_Show.query.all()

    # Will not run until something is put into the search field
    if request.args.get('search') != None:
        search = request.args.get('search')

        if request.args.get('filter') != 'Filter by Genre':
            filter = Movies_Show.query.where((Movies_Show.genre == request.args.get('filter')) & (Movies_Show.title.contains(search))).all()
            return render_template('catalog.html',movies_shows=filter)

        
        searched_content = Movies_Show.query.filter(Movies_Show.title.contains(search)).all()

        return render_template('catalog.html',movies_shows=searched_content)
    
    return render_template('catalog.html', movies_shows=movies_shows)
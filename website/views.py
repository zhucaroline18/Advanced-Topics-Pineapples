from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user

from .models import Note
from . import db
import json
#separate app so don't have all views in one file but multiple files 

#now set up blueprint for flask application 
views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
@login_required #only home page if logged in 
#for homepage whenever we type in /, whatever is in home is what's going to run 
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note)<=1:
            flash('Note is too short!', category = 'error')
        else:
            new_note = Note(data = note, user_id = current_user.id) #registering the new note and adding it ot database 
            db.session.add(new_note)
            db.session.commit() #committing to the database 
            #flash('Note Added!', category = 'success')

    return render_template("home.html", user = current_user) #in our template ,can check our current user 

@views.route('/delete-note', methods = ['POST'])
def delete_note():
    #take in data from post request, load it as json object, get note id, look for note that has that id, if we own that note, delete the note
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})  
    #returning empty response 

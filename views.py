import secrets
from PIL import Image
from flask import Blueprint, render_template, request, flash, jsonify, abort
from flask.wrappers import Response
from flask_login import login_required, current_user
from sqlalchemy import asc
from sqlalchemy.sql.functions import user
from werkzeug.utils import secure_filename
from .models import Rating, User, Note, Contact, Place, Restaurant, Ho, imageplace
from . import db
import json
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Admin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from sqlite3 import Error
import numpy as np
import pandas as pd
from pandas import DataFrame as df
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity
from ast import literal_eval
from sklearn.preprocessing import LabelEncoder
import sklearn.metrics as sm
import os
from flask import Flask, request, render_template, send_from_directory
import time
import datetime

views = Blueprint('views', __name__)


def create_connection():
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    database = r"c:\Users\Public\.VS CODE\TRASIA\website\database.db"

    conn = None
    try:
        conn = sqlite3.connect(database)
        print("CONNECTED TO DATABASEEEEEEEEEEE ALHAMDULILLAH")
    except Error as e:
        print(e)

    return conn

def select_all_place(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM place ORDER BY place_name ASC")

    rows = cur.fetchall()

    return rows


#ikotkan yg ni nak fetch the details of a particular place tapi belum ada reference
def select_place_name(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM place ORDER BY place_name ASC")

    rows = cur.fetchall()

    #for row in rows:
    #    print(row)

    return rows




# fetch data of top 5 PLACES from db
def select_place_name_top5(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM place ORDER BY place_rating DESC LIMIT 5")

    

    rows = cur.fetchall()

    # print()
    # print("----------------------------------")
    # for row in rows:
    #     print(row)
    # print("----------------------------------")
    # print()

    return rows

# fetch data of top 5 RESTAURANTS from db
def select_restaurant_name_top5(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM restaurant ORDER BY rest_rating DESC LIMIT 5")

    

    rows = cur.fetchall()

    # print()
    # print("----------------------------------")
    # for row in rows:
    #     print(row)
    # print("----------------------------------")
    # print()

    return rows


def select_all_restaurant(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM restaurant ORDER BY rest_name ASC")

    rows = cur.fetchall()

    #for row in rows:
    #    print(row)

    return rows


#ikotkan yg ni nak fetch the details of a particular restaurant tapi belum ada reference
def select_restaurant_name(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM restaurant ORDER BY rest_name ASC")

    rows = cur.fetchall()

    #for row in rows:
    #    print(row)

    return rows

#ikotkan yg ni nak fetch the details of a particular restaurant tapi belum ada reference
def select_restaurant_name_shj(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT rest_name FROM restaurant ORDER BY rest_name ASC")

    rows = cur.fetchall()

    # print()
    # print("8888888888888FROM name shj 8888888888888")
    # for row in rows:
    #     print(row)

    # print()
    return rows


# fetch all place name untuk display as list that can be chosen by the user when they enter a character
def select_place_name_shj(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT place_name FROM place ORDER BY place_name ASC")

    rows = cur.fetchall()   

    return rows

def select_place_keyword_name_shj(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT place_keyword FROM place ORDER BY place_name ASC")

    rows = cur.fetchall()
    

    return rows


#fetch place's keyword untuk user search by place's keyword such as nature, wildlife etc
def select_place_keyword_shj(m_name):

    #### OKAY ####
    db = SQLAlchemy()
    DB_NAME = "database.db"
    #nak dapatkan attributes for a place
    try:
        conn = create_connection()
        print("SUCCESSFUL TO CONNECT TO DATABASE")

        select_all_place(conn)
    except Error as e:
        print("FAILEDDDDDDDDDD TO  displayyyyy")
        print(e)
    #### OKAY ####  

    cur = conn.cursor()
    cur.execute("SELECT * FROM place WHERE place_keyword = '" + m_name + "' ORDER BY place_rating ASC LIMIT 10")

    rows = cur.fetchall()   

    return rows

#fetch place's keyword untuk user search by place's keyword such as nature, wildlife etc
def select_restaurant_keyword_shj(m_name):

    #### OKAY ####
    db = SQLAlchemy()
    DB_NAME = "database.db"
    #nak dapatkan attributes for a place
    try:
        conn = create_connection()
        print("SUCCESSFUL TO CONNECT TO DATABASE")

        select_all_place(conn)
    except Error as e:
        print("FAILEDDDDDDDDDD TO  displayyyyy")
        print(e)
    #### OKAY ####  

    cur = conn.cursor()
    cur.execute("SELECT * FROM restaurant WHERE rest_keyword = '" + m_name + "' ORDER BY rest_rating ASC LIMIT 10")

    rows = cur.fetchall()   

    return rows


def select_place_attraction_shj(m_name):

    #### OKAY ####
    db = SQLAlchemy()
    DB_NAME = "database.db"
    #nak dapatkan attributes for a place
    try:
        conn = create_connection()
        print("SUCCESSFUL TO CONNECT TO DATABASE")

        select_all_place(conn)
    except Error as e:
        print("FAILEDDDDDDDDDD TO  displayyyyy")
        print(e)
    #### OKAY ####  

    cur = conn.cursor()
    cur.execute("SELECT * FROM place WHERE place_attractions = '" + m_name + "' ORDER BY place_rating ASC LIMIT 10")

    rows = cur.fetchall()   

    return rows

def select_restaurant_attraction_shj(m_name):

    #### OKAY ####
    db = SQLAlchemy()
    DB_NAME = "database.db"
    #nak dapatkan attributes for a place
    try:
        conn = create_connection()
        print("SUCCESSFUL TO CONNECT TO DATABASE")

        select_all_place(conn)
    except Error as e:
        print("FAILEDDDDDDDDDD TO  displayyyyy")
        print(e)
    #### OKAY ####  

    cur = conn.cursor()
    cur.execute("SELECT * FROM restaurant WHERE rest_attractions = '" + m_name + "' ORDER BY rest_rating ASC LIMIT 10")

    rows = cur.fetchall()   

    return rows


#untuk page search all places
def select_place_name_keyword_attractions_shj(conn):
    rows = []
    rows2 = []
    rows3 = []

    cur = conn.cursor()

    cur.execute("SELECT place_name FROM place ORDER BY place_name ASC")
    rows = cur.fetchall()

    cur.execute("SELECT DISTINCT place_keyword FROM place ORDER BY place_keyword ASC")
    rows2 = cur.fetchall()

    rows += rows2

    cur.execute("SELECT DISTINCT place_attractions FROM place ORDER BY place_attractions ASC")
    rows3 = cur.fetchall()
    
    rows += rows3
    rows = list(dict.fromkeys(rows))

    return rows

#untuk page search all places
def select_restaurant_name_keyword_attractions_shj(conn):
    rows = []
    rows2 = []
    rows3 = []

    cur = conn.cursor()

    cur.execute("SELECT rest_name FROM restaurant ORDER BY rest_name ASC")
    rows = cur.fetchall()

    cur.execute("SELECT DISTINCT rest_keyword FROM restaurant ORDER BY rest_keyword ASC")
    rows2 = cur.fetchall()

    rows += rows2

    cur.execute("SELECT DISTINCT rest_attractions FROM restaurant ORDER BY rest_attractions ASC")
    rows3 = cur.fetchall()
    
    rows += rows3
    rows = list(dict.fromkeys(rows))

    return rows



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity
from ast import literal_eval
from sklearn.preprocessing import LabelEncoder
import sklearn.metrics as sm

place_df = pd.read_csv("website/dataset_place.csv",encoding='latin1')


#    THE similarity are counted / calculated from the number of similarity of
#    EACH WORDS in place_desc !!!!!!!!!!!!!!!!!!!!!!

tfidf = TfidfVectorizer(stop_words="english")
place_df["place_desc"] = place_df["place_desc"].fillna("")

tfidf_matrix = tfidf.fit_transform(place_df["place_desc"])

# Compute similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(place_df.index, index=place_df["place_name"]).drop_duplicates()
all_names = [place_df['place_name'][i] for i in range(len(place_df['place_name']))]


# function get name
def get_recommendations(name):
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    idx = indices[name]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]

    tit = place_df['place_name'].iloc[movie_indices]
    dat = place_df['place_keyword'].iloc[movie_indices]
    image = place_df['image1_img'].iloc[movie_indices]

    place_from_csv_name = place_df["place_name"].values.tolist()

    place_from_csv2 = place_df[0:].values.tolist()
    
    place_from_db = Place.query.all()                   # Output : [<Place 1>, <Place 2>, <Place 3>, <Place 4>]
    place_from_dbName = place_from_db[1]                # Output : <Place 1>
    

    #### OKAY ####
    db = SQLAlchemy()
    DB_NAME = "database.db"
    #nak dapatkan attributes for a place
    try:
        conn = create_connection()
        print("SUCCESSFUL TO CONNECT TO DATABASE           SUCCESSFUL")

        select_all_place(conn)
    except Error as e:
        print("FAILEDDDDDDDDDD TO  displayyyyy         FAILEDDDDDDDDDD")
        print(e)

    #print("................PLACE IN name:: ")
    #print(place_from_csv_name)                #place_from_csv2 =  ALL attributes in csv displayed.
    

    return_df = pd.DataFrame(columns=['place_name','place_keyword','image1_img'])

    return_df['place_name'] = tit               #!! recommendation :: place name - ada 10
    return_df['place_keyword'] = dat            #!! recommendation :: place keyword - ada 10
    return_df['image1_img'] = image

    return return_df




def get_admission(x):
    for i in x:
        if i["place_admission"] == "free":
            return (i["place_name"])
    return np.nan

def get_list(x):
    if isinstance(x, list):
        names = [i["place_name"] for i in x]

        if len(names) > 3:
            names = names[:3]

        return names

    return []


#DATA CLEANING
def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ""
    
### Count similarity from these attributes
features = ['place_keyword', 'place_attractions', 'place_desc', 'place_rating']

for feature in features:
    place_df[feature] = place_df[feature].apply(clean_data)
    

def create_soup(x):
    return ' '.join(x['place_keyword']) + ' ' + ' '.join(x['place_attractions']) + ' ' + ' '.join(x['place_desc']) + ' ' + ' '.join(x['place_rating'])


place_df["soup"] = place_df.apply(create_soup, axis=1)

count_vectorizer = CountVectorizer(token_pattern=r"(?u)\b\w+\b", stop_words=None, ngram_range=(2,2), analyzer='word')

count_matrix = count_vectorizer.fit_transform(place_df["soup"])

cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

place_df = place_df.reset_index()
indices = pd.Series(place_df.index, index=place_df['place_name'])
all_places = [place_df['place_name'][i] for i in range(len(place_df['place_name']))]
all_keyword = [place_df['place_keyword'][i] for i in range(len(place_df['place_keyword']))]












































rest_df = pd.read_csv("website/dataset_restaurant.csv",encoding='latin1')


#    THE similarity are counted / calculated from the number of similarity of
#    EACH WORDS in rest_desc !!!!!!!!!!!!!!!!!!!!!!

tfidf2 = TfidfVectorizer(stop_words="english")
rest_df["rest_desc"] = rest_df["rest_desc"].fillna("")

tfidf_matrix2 = tfidf2.fit_transform(rest_df["rest_desc"])

# Compute similarity
cosine_sim2 = linear_kernel(tfidf_matrix2, tfidf_matrix2)

indices2 = pd.Series(rest_df.index, index=rest_df["rest_name"]).drop_duplicates()
all_names2 = [rest_df['rest_name'][i] for i in range(len(rest_df['rest_name']))]


# function get name
def get_recommendations_restaurant(name):
    cosine_sim2 = cosine_similarity(count_matrix2, count_matrix2)
    idx2 = indices2[name]
    sim_scores = list(enumerate(cosine_sim2[idx2]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices2 = [i[0] for i in sim_scores]

    tit = rest_df['rest_name'].iloc[movie_indices2]
    dat = rest_df['rest_keyword'].iloc[movie_indices2]
    image = rest_df['image1_img'].iloc[movie_indices2]
    
    place_from_csv_name = rest_df["rest_name"].values.tolist()

    place_from_csv2 = rest_df[0:].values.tolist()
    
    rest_from_db = Restaurant.query.all()                   # Output : [<Place 1>, <Place 2>, <Place 3>, <Place 4>]
    place_from_dbName = rest_from_db[1]                # Output : <Place 1>
    

#### OKAY ####
    db = SQLAlchemy()
    DB_NAME = "database.db"
    #nak dapatkan attributes for a place
    try:
        conn = create_connection()
        print("SUCCESSFUL TO CONNECT TO DATABASE           SUCCESSFUL")

        select_all_place(conn)
    except Error as e:
        print("FAILEDDDDDDDDDD TO  displayyyyy         FAILEDDDDDDDDDD")
        print(e)
#### OKAY ####    


    # print("................PLACE IN name:: ")
    # print(place_from_csv_name)                #place_from_csv2 =  ALL attributes in csv displayed.
    
    return_df = pd.DataFrame(columns=['rest_name','rest_keyword','image1_img'])

    return_df['rest_name'] = tit               #!! recommendation :: place name - ada 10
    return_df['rest_keyword'] = dat            #!! recommendation :: place keyword - ada 10
    return_df['image1_img'] = image

    return return_df


def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ""


### BHGN NI YG PENTINGGGGGGG !!!!!! Dia kira similarity from these attributes  
features = ['rest_keyword', 'rest_attractions', 'rest_desc']

for feature in features:
    rest_df[feature] = rest_df[feature].apply(clean_data)
    
def create_soup(x):
    return ' '.join(x['rest_keyword']) + ' ' + ' '.join(x['rest_attractions']) + ' ' + ' '.join(x['rest_desc'])


rest_df["soup"] = rest_df.apply(create_soup, axis=1)

#count_vectorizer = CountVectorizer(stop_words="english")

count_vectorizer2 = CountVectorizer(token_pattern=r"(?u)\b\w+\b", stop_words=None, ngram_range=(2,2), analyzer='word')

count_matrix2 = count_vectorizer2.fit_transform(rest_df["soup"])

cosine_sim4 = cosine_similarity(count_matrix2, count_matrix2)

rest_df = rest_df.reset_index()
indices2 = pd.Series(rest_df.index, index=rest_df['rest_name'])
all_restaurant_rest = [rest_df['rest_name'][i] for i in range(len(rest_df['rest_name']))]

















@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    user=current_user

    if user.type == 'user':
        #return redirect(url_for('views.home'))
        image_file = url_for('static', filename='profile_pics/' + user.image_file)

        return render_template("User/1home.html", user=current_user, image=image_file)
    else:
        #return redirect(url_for('views.Ahome'))
        
        # Fetch all customer records
        #records = db.query.all(User)

        # Loop over records
        #for record in records:
        #    print(record)

        # file_user = user.image_file
        # file_name = 'profile_pics/' + file_user

        # image_file = "default.png"

        image_file = url_for('static', filename='profile_pics/' + user.image_file)
            
        return render_template("Admin/1.0.home.html", user=current_user, image=image_file)
    


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})





@views.route('/contact', methods=['GET', 'POST'])
@login_required
def contact():
    #user=current_user

    print('masuk contact @ views.py')
    posts = Contact.query.all()

    print(posts)

    return render_template("Admin/7.0contactview.html", user=current_user, posts=posts)
    

@views.route('/all_place', methods=['GET', 'POST'])
@login_required
def all_place():

    if request.method == 'POST':
        print("@@@MASUKKKKKKKKKKKKKKKKKKKK all_place from ALL PLACES.html")
        

        #KITA X PASS PLACE ID DARI PAGE ALL PLACES !!!
        id = request.form.get('place_name')
        user_id = current_user.id

        #panggil data from database
        posts = Place.query.filter_by(place_name=id).first()
        #posto = Restaurant.query.get(id)   #same as above



        try:
            rate_status = Rating.query.filter_by(id_attraction=id, user_id=user_id).first()

            review = Rating.query.filter_by(id_attraction=posts.place_name).all()

            users = User.query.all()

            print("ADA KE ?")
            print(rate_status)
        except:
            rate_status = "NONE"
            
            print("TAK MASUK rate_status")


        #return redirect(url_for('views.rec_detail'))
        return render_template("User/2.1.2.place_details.html", user=current_user, posts=posts, rate_status=rate_status, review=review, users=users)

    else:
        print("----------all_place----------")
        #panggil data from database
        posts = Place.query.order_by(asc("place_name")).all()

        # print(posts)

        db = SQLAlchemy()
        DB_NAME = "database.db"
                #nak dapatkan attributes for a place
        try:
            conn = create_connection()
            print("SUCCESSFUL TO CONNECT TO DATABASE           SUCCESSFUL")

            select_place_name_shj(conn)

        except Error as e:
            print("FAILEDDDDDDDDDD TO  displayyyyy         FAILEDDDDDDDDDD")
            print(e)
            #### OKAY ####   

        result = select_place_name_shj(conn)         #!! fetch all places
        

        return render_template("User/2.1..view_all_place.html", user=current_user, posts=posts, languages=result)

@views.route('/all_restaurant', methods=['GET', 'POST'])
@login_required
def all_restaurant():

    if request.method == 'POST':
        print("@@@MASUKKKKKKKKKKKKKKKKKKKK all_restaurant from ALL RESTAURANT.html")
        

        #KITA X PASS PLACE ID DARI PAGE ALL PLACES !!!
        id = request.form.get('place_name')
        user_id = current_user.id

        # print()
        # print()
        # print()
        # print("@@@@@@@@@@@@@@@@")
        # print()
        # print("Name: ")
        # print(id)
        

        #panggil data from database
        posts = Restaurant.query.filter_by(rest_name=id).first()
        #posto = Restaurant.query.get(id)   #same as above



        try:
            rate_status = Rating.query.filter_by(id_attraction=id, user_id=user_id).first()

            review = Rating.query.filter_by(id_attraction=posts.rest_name).all()

            users = User.query.all()

            print("ADA KE ?")
            print(rate_status)
        except:
            print("TAK MASUK rate_status")

        # print(posts)
        print()
        print("@@@@@@@@@@@@@@@@")
        print()
        print()
        print()

        #return redirect(url_for('views.rec_detail'))
        return render_template("User/2.2.2.rest_details.html", user=current_user, posts=posts, rate_status=rate_status, review=review, users=users)

    else:
        print("----------all_place----------")
        #panggil data from database
        posts = Restaurant.query.order_by(asc("rest_name")).all()

        # print(posts)

        db = SQLAlchemy()
        DB_NAME = "database.db"
                #nak dapatkan attributes for a place
        try:
            conn = create_connection()
            print("SUCCESSFUL TO CONNECT TO DATABASE           SUCCESSFUL")

            select_restaurant_name_shj(conn)

        except Error as e:
            print("FAILEDDDDDDDDDD TO  displayyyyy         FAILEDDDDDDDDDD")
            print(e)
            #### OKAY ####   

        result = select_restaurant_name_shj(conn)         #!! fetch all places

        # print(result)
        print()

        return render_template("User/2.2..view_all_restaurant.html", user=current_user, posts=posts, languages=result)

@views.route('/rec_place', methods=['GET', 'POST'])
@login_required
def rec_place():

    if request.method == 'POST':
        m_name = request.form['place_name'] #get title
        m_name = str(m_name) #change datatype to string

        m_name2 = m_name
        m_name = m_name.upper()
        
        attractions = ["ARCHITECTURAL BUILDING", "NATIONAL HERITAGE", "AQUARIUM", "WILDLIFE", "TOWERS", "SHOPPING MALLS", "NEIGHBOURHOODS", "GARDEN", "RELIGIOUS SITES", "SCIENCE", "LEISURE", "FOUNTAIN", "NATURE", "PARKS", "MOUNTAINS", "WATERFALLS", "FOREST", "THEME PARKS", "RIVER", "PUBLIC TRANSPORT", "BUILDING", "WATER ATTRACTION"]
        keywords = ["MUSEUM", "NATURE", "NEIGHBOURHOODS", "PUBLIC TRANSPORT", "RELIGIOUS SITES", "SCULPTURE", "SHOPPING CENTRE", "WATER ATTRACTION", "WILDLIFE"]

    #call and display recommendation
        #check = difflib.get_close_matches(m_name,all_titles,cutout=0.50,n=1)
        if m_name2 in all_places:
            result_final = get_recommendations(m_name2) #call function

            print()
            print()
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            print(" if m_name in all_places: ")
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            print()
            print()

            names = []
            keyword = []
            result = []
            image = []

            for i in range(len(result_final)):
                names.append(result_final.iloc[i][0])
                keyword.append(result_final.iloc[i][1])
                image.append(result_final.iloc[i][2])
                
                     

            #### OKAY ####
            db = SQLAlchemy()
            DB_NAME = "database.db"
            #nak dapatkan attributes for a place
            try:
                conn = create_connection()
                print("SUCCESSFUL TO CONNECT TO DATABASE")

                select_all_place(conn)
            except Error as e:
                print("FAILEDDDDDDDDDD TO  displayyyyy")
                print(e)
            #### OKAY ####   


            print("__________________________")
            

            result = select_place_name(conn)         #!! fetch all places
            #result_name = result[1]                 #name of places in DB
            #print()
            #print()
            #print("yg ini+++")
            #print(result[0][1])
            #print(result[1][1])
            #print(result[2][1])
            #print(result[3][1])
            #print(result[4][1])    #Taman Rimba Bukit Kerinchi


            count = Place.query.count()
            # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            # print("COUNT NUMBER OF PLACE")
            # print(count)
            # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            my_array = []
            my_array_name = []
            my_array_id = []
            #cari and compare each recommendation from csv with database
            #for fruit in result:       # fruit supposedly nama from database
            for x in names:                 #x ni nama place from recommendation
                i=0
                while i<count:         
                    #nanti kena tukar sbb once tambah new place, nanti kiraan dia out of bound
                    if x == result[i][1]:     # if x from recommendation == y from db
                        #print()
                        print("~~~~~~~~~~~~~~~~~~~~~~PLACE exists")
                        
                        # print(result[i])
                        #my_array = my_list.append(result[i])
                    
                        #my_list = np.append(my_list, result[i])
                        my_array.append([result[i]])            # APPEND SEMUA DETAILS UNTUK 10 RECOMMENDATIONS
                        my_array_name.append(result[i][1])      # APPEND NAMES SAHAJA UNTUK 10 REC TU.
                        my_array_id.append(result[i][0])        # APPEND ID SAHAJA UNTUK 10 REC TU.
                        print("@@@@@@@@@@@@@@ MY_ARRAY")
                        print(my_array_name)
                        print(my_array_id)
                        print("@@@@@@@@@@@@@@@@@@@@@@")

                        
                    #else:
                        #print("No")
                        #print(x)     #names ni kedudukan dari recommendation

                    i=i+1
                    
                
            # print("+++++++++++++++++++++++++++++++++++++")
            print (my_array_name)
            # print()
            # print (my_array)

            my_array_name = my_array_name
            

            print("__________________________")

            
            return render_template('User/2.1.1.rec_place.html', my_array_id=my_array_id, my_array_name=my_array_name, my_list=my_array, posts=result, place_name=names, place_keyword=keyword,search_name=m_name, user=current_user, image=image)
        
        elif m_name in keywords:

            result_final = select_place_keyword_shj(m_name)  #call function

            id = []
            names = []
            keyword = []
            result = []
            image = []

            for i in range(len(result_final)):
                id.append(result_final[i][0])
                names.append(result_final[i][1])
                keyword.append(result_final[i][2])
                image.append(result_final[i][13])
                                 
            
            return render_template('User/2.1.1.rec_place.html', my_array_id=id, my_array_name=names, posts=result, place_name=names, place_keyword=keyword,search_name=m_name, user=current_user, image=image)
        
        elif m_name in attractions:
            
            result_final = select_place_attraction_shj(m_name)  #call function

            id = []
            names = []
            keyword = []
            result = []
            image = []

            for i in range(len(result_final)):
                id.append(result_final[i][0])
                names.append(result_final[i][1])
                keyword.append(result_final[i][2])
                image.append(result_final[i][13])
                                 
            
            return render_template('User/2.1.1.rec_place.html', my_array_id=id, my_array_name=names, posts=result, place_name=names, place_keyword=keyword,search_name=m_name, user=current_user, image=image)
        else: 
            return render_template("User/2.1.0.rec_place.html", user=current_user)
    else:

        db = SQLAlchemy()
        DB_NAME = "database.db"
            #nak dapatkan attributes for a place
        try:
            conn = create_connection()
            print("SUCCESSFUL TO CONNECT TO DATABASE           SUCCESSFUL")

            select_all_place(conn)

        except Error as e:
            print("FAILEDDDDDDDDDD TO  displayyyyy         FAILEDDDDDDDDDD")
            print(e)
            #### OKAY ####   


        print("_____________rec_place_____________")
            
        result = select_place_name_keyword_attractions_shj(conn)
        #result = select_place_name_shj(conn)         #!! fetch all places

        #top5 = db.session.query(Place).order_by(Place.place_rating.asc()).limit(5).all()

        top5 = select_place_name_top5(conn)


        return render_template("User/2.1.0.rec_place.html", user=current_user, languages=result, posts=top5) 










@views.route('/rec_restaurant', methods=['GET', 'POST'])
@login_required
def rec_restaurant():

    if request.method == 'POST':
        m_name = request.form['place_name'] #get title
        m_name = str(m_name) #change datatype to string

        m_name2 = m_name
        m_name = m_name.upper()

        print("NAMA YG DISEARCH : "+m_name)

        attractions = ["DESSERT", "HEAVY MEALS", "COFFEE N TEA", "FAST FOOD", "QUICK BITES"]
        keywords = ["CAFE", "RESTAURANT"]

        #call and display recommendation
        #check = difflib.get_close_matches(m_name,all_titles,cutout=0.50,n=1)
        if m_name2 in all_restaurant_rest:
            result_final = get_recommendations_restaurant(m_name2) #call function

            names = []
            keyword = []
            result = []
            image = []

            for i in range(len(result_final)):
                names.append(result_final.iloc[i][0])
                keyword.append(result_final.iloc[i][1].upper())
                image.append(result_final.iloc[i][2])
                
            
            

            #### OKAY ####
            db = SQLAlchemy()
            DB_NAME = "database.db"
            #nak dapatkan attributes for a place
            try:
                conn = create_connection()
                print("SUCCESSFUL TO CONNECT TO DATABASE           SUCCESSFUL")

                select_all_place(conn)
            except Error as e:
                print("FAILEDDDDDDDDDD TO  displayyyyy         FAILEDDDDDDDDDD")
                print(e)
            #### OKAY ####   


            print("__________________________")
            

            result = select_restaurant_name(conn)         #!! fetch all places
           
            count = Restaurant.query.count()
            
            my_array = []
            my_array_name = []
            my_array_id = []
            #cari and compare each recommendation from csv with database
            #for fruit in result:       # fruit supposedly nama from database
            for x in names:                 #x ni nama place from recommendation
                i=0
                while i<count:    # YANG INI PENTING SEBAB DIA FETCH THE DATA FROM DATABASE, SO IF U TAMBAH DATA, PLEASEEEEE CHANGE ITERATION.
                    #nanti kena tukar sbb once tambah new place, nanti kiraan dia out of bound
                    if x == result[i][1]:     # if x from recommendation == y from db
                        #print()
                        print("~~~~~~~~~~~~~~~~~PLACE exists")
                        
                        #print(result[i])
                        #my_array = my_list.append(result[i])
                    
                        #my_list = np.append(my_list, result[i])
                        my_array.append([result[i]])            # APPEND SEMUA DETAILS UNTUK 10 RECOMMENDATIONS
                        my_array_name.append(result[i][1])      # APPEND NAMES SAHAJA UNTUK 10 REC TU.
                        my_array_id.append(result[i][0])        # APPEND ID SAHAJA UNTUK 10 REC TU.
                        # print("@@@@@@@@@@@@@@ MY_ARRAY")
                        # print(my_array_name)
                        # print(my_array_id)
                        # print("@@@@@@@@@@@@@@@@@@@@@@")
                    #else:
                        #print("No")
                        #print(x)     #names ni kedudukan dari recommendation

                    i=i+1
                    
                
            # print("+++++++++++++++++++++++++++++++++++++")
            # print (my_array_name)
            # print()
            # print (my_array)

            my_array_name = my_array_name

            print("__________________________")

            
            return render_template('User/2.2.1.rec_restaurant.html', image=image, my_array_id=my_array_id, my_array_name=my_array_name, my_list=my_array, posts=result, place_name=names, place_keyword=keyword,search_name=m_name, user=current_user)
        
        elif m_name in keywords:

            result_final = select_restaurant_keyword_shj(m_name)  #call function

            id = []
            names = []
            keyword = []
            result = []
            image = []

            for i in range(len(result_final)):
                id.append(result_final[i][0])
                names.append(result_final[i][1])
                keyword.append(result_final[i][2])
                image.append(result_final[i][13])
                                 
            
            return render_template('User/2.2.1.rec_restaurant.html', my_array_id=id, my_array_name=names, posts=result, place_name=names, place_keyword=keyword,search_name=m_name, user=current_user, image=image)
        
        elif m_name in attractions:
            
            result_final = select_restaurant_attraction_shj(m_name)  #call function

            id = []
            names = []
            keyword = []
            result = []
            image = []

            for i in range(len(result_final)):
                id.append(result_final[i][0])
                names.append(result_final[i][1])
                keyword.append(result_final[i][2])
                image.append(result_final[i][13])
                                 
            return render_template('User/2.2.1.rec_restaurant.html', my_array_id=id, my_array_name=names, posts=result, place_name=names, place_keyword=keyword,search_name=m_name, user=current_user, image=image)
        else: 
            return render_template("User/2.2.0.rec_restaurant.html", user=current_user)
    else:
        db = SQLAlchemy()
        DB_NAME = "database.db"
            #nak dapatkan attributes for a place
        try:
            conn = create_connection()
            print("SUCCESSFUL TO CONNECT TO DATABASE           SUCCESSFUL")

            select_all_place(conn)

        except Error as e:
            print("FAILEDDDDDDDDDD TO  displayyyyy         FAILEDDDDDDDDDD")
            print(e)
            #### OKAY ####   


        print("_____________rec_restaurant_____________")
            

        #result = select_restaurant_name_shj(conn)         #!! fetch all places
        result = select_restaurant_name_keyword_attractions_shj(conn)

        top5 = select_restaurant_name_top5(conn)


        return render_template("User/2.2.0.rec_restaurant.html", user=current_user, languages=result, posts=top5)   



@views.route("/rate_place", methods=["POST", "GET"])
def rate_place():
    if request.method == "POST":

        user_id = current_user.id
        rating = request.form.get('rating')
        rate_type = request.form.get('rate_type')
        id_attraction = request.form.get('id_attraction')
        place_name = request.form.get('place_name')
        review = request.form.get('review')

        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%Y %I:%M %p')

        db = SQLAlchemy()
        DB_NAME = "database.db"
            #nak dapatkan attributes for a place
        try:
            conn = create_connection()
            print("SUCCESSFUL TO CONNECT TO DATABASE           SUCCESSFUL")

            new_rate = Rating(rating=rating, user_id=user_id, rate_date=timestamp, rate_type=rate_type, id_attraction=place_name, review=review)
            db.session.add(new_rate)
            db.session.commit()

        except Error as e:
            print("FAILEDDDDDDDDDD TO  displayyyyy         FAILEDDDDDDDDDD")
            print(e)
            #### OKAY ####   

                 
        return redirect(url_for('views.rate_place'))
        # return render_template("User/2.1..view_all_place.html", user=current_user, posts=posts, languages=result)
    
    else:
        return redirect(url_for('views.all_place'))
        # return render_template("User/2.1..view_all_place.html", user=current_user, posts=posts, languages=result)



@views.route("/rate_restaurant", methods=["POST", "GET"])
def rate_restaurant():
    if request.method == "POST":

        user_id = current_user.id
        rating = request.form.get('rating')
        rate_type = request.form.get('rate_type')
        id_attraction = request.form.get('id_attraction')
        place_name = request.form.get('place_name')

        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%Y %I:%M %p')

        db = SQLAlchemy()
        DB_NAME = "database.db"
            #nak dapatkan attributes for a place
        try:
            conn = create_connection()
            print("SUCCESSFUL TO CONNECT TO DATABASE           SUCCESSFUL")

            new_rate = Rating(rating=rating, user_id=user_id, rate_date=timestamp, rate_type=rate_type, id_attraction=place_name)
            db.session.add(new_rate)
            db.session.commit()

        except Error as e:
            print("FAILEDDDDDDDDDD TO  displayyyyy         FAILEDDDDDDDDDD")
            print(e)
            #### OKAY ####   
          
        return redirect(url_for('views.rate_restaurant'))
        # return render_template("User/2.1..view_all_place.html", user=current_user, posts=posts, languages=result)
    
    else:
        return redirect(url_for('views.all_restaurant'))
        # return render_template("User/2.1..view_all_place.html", user=current_user, posts=posts, languages=result)




############################ ############## ##############        ADMIN    ################################################################################ 

@views.route('/Ahome', methods=['GET', 'POST'])
@login_required
def Ahome():
    #return redirect(url_for('views.Ahome'))
    return render_template("Admin/1.0.home.html", user=current_user)


from base64 import b64encode

@views.route('/view_place', methods=['GET', 'POST'])
@login_required
def view_place():

        print("------------------------view_place-----------------")
        #panggil data from database
        posts = Place.query.all()    

        return render_template("Admin/2.0.viewPlace.html", user=current_user, posts=posts)



@views.route('/update_place', methods=['POST'])
@login_required
def update_place():
    
    if request.method == 'POST':
        print("~~~~~~~~~~~~~~~MASUKKKKKKKKKKKKKKKKKKKK updatePlace")
        
        id = request.form.get('id')
        address = request.form.get('address')
        email = request.form.get('email')
        name = request.form.get('name')
        phonenumber = request.form.get('phonenumber')
        description = request.form.get('description')
        website = request.form.get('website')
        hour = request.form.get('hour')
        keyword = request.form.get('keyword')
        attraction= request.form.get('attraction')
        fee = request.form.get('place_fee')
        update_image = request.form.get('update_image')

        #email = current_user.email
       
        image = request.files['image1']
        imageLama = request.form.get('imageLama')
        


        if(update_image == 'NO'):
            picture_fn2 = imageLama
            print("@@@@@@@@@@@@@@@@@@@@@@@NNNNNNNNNNNNNOOOOOOOOOOOOOOO")
        else:
            print("@@@@@@@@@@@@@@@@@@@@@@@YYYYYYYYYYYYEEEEEEEEESSSSSSS")
            random_hex = secrets.token_hex(8)
            _, f_ext = os.path.splitext(image.filename)
            picture_fn = random_hex + f_ext
            picture_path = os.path.join(views.root_path, 'static/place_pics', picture_fn)

            output_size = (125, 125)
            i = Image.open(image)
            i.thumbnail(output_size)
            i.save(picture_path)

            prev_picture = os.path.join(views.root_path, imageLama)
            if os.path.exists(prev_picture):
                os.remove(prev_picture)

            picture_fn2 = "static/place_pics/" + picture_fn


        # print("@@@@@@@@@@@@@@@@@@@@@")
        # print(id)
        # print("IMAGE LAMA:")
        # print(imageLama)
        # print()
        # print("PATH PIC LAMA")
        # print(prev_picture)
        # print()
        # print("IMAGE BARU")
        # print(picture_fn2)
        # print("@@@@@@@@@@@@@@@@@@@@@")

        try:
            db.session.query(Place).filter(Place.place_id == id).update({'place_address': address, 'place_email': email, 'place_name' : name, 'place_phoneNum': phonenumber, 'place_description': description, 'place_website' : website, 'place_operatingHour': hour, 'place_keyword': keyword, 'place_attractions' : attraction, 'place_fee' : fee, 'image1_img' : picture_fn2})
            db.session.commit()
            print("@@@@@@@@@@@@@@@@BERJAYA UPDATEEEEEEEEEEE")

            #image_file = url_for('static', filename='profile_pics/' + current_user.image1_img)
            return redirect(url_for('views.view_place'))
            
        except:
            print("@@@@@@@@@@@@@@@@TAKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK BERJAYA UPDATEEEEEEEEEEE")
            #return render_template("Admin/1.0.home.html", user=current_user)
            return redirect(url_for('views.view_place'))

    

@views.route('/delete_place', methods=['POST'])
def delete_place():
    
    if request.method == 'POST':
        print("~~~~~~~~~~~~~~~MASUKKKKKKKKKKKKKKKKKKKK delete_place")
        
        id = request.form.get('id')
        print()
        print(id)

        imageLama = request.form.get('imageLama')

        prev_picture = os.path.join(views.root_path, imageLama)
        if os.path.exists(prev_picture):
            os.remove(prev_picture)


        try:
            my_data = Place.query.get(id)

            db.session.delete(my_data)
            db.session.commit()
            print("@@@@@@@@@@@@@@@@BERJAYA DELETE")

            return redirect(url_for('views.view_place'))
            
        except:
            print("@@@@@@@@@@@@@@@@TAKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK BERJAYA DELETEEEEEEEEE")
            return render_template("Admin/1.0.home.html", user=current_user)







@views.route('/view_restaurant', methods=['GET', 'POST'])
@login_required
def view_restaurant():

    #panggil data from database
    posts = Restaurant.query.all()

    #print(posts)

    return render_template("Admin/2.0.viewRestaurant.html", user=current_user, posts=posts)

@views.route('/update_restaurant', methods=['POST'])
@login_required
def update_restaurant():
    
    if request.method == 'POST':
        print("~~~~~~~~~~~~~~~MASUKKKKKKKKKKKKKKKKKKKK update_restaurant")
        
        id = request.form.get('id')
        address = request.form.get('address')
        email = request.form.get('email')
        name = request.form.get('name')
        phonenumber = request.form.get('phonenumber')
        description = request.form.get('description')
        website = request.form.get('website')
        hour = request.form.get('hour')
        keyword = request.form.get('keyword')
        attraction= request.form.get('attraction')       
        update_image = request.form.get('update_image')

        #email = current_user.email
       
        image = request.files['image1']
        imageLama = request.form.get('imageLama')
        
        if(update_image == 'NO'):
            picture_fn2 = imageLama
            print("@@@@@@@@@@@@@@@@@@@@@@@NNNNNNNNNNNNNOOOOOOOOOOOOOOO")
        else:
            print("@@@@@@@@@@@@@@@@@@@@@@@YYYYYYYYYYYYEEEEEEEEESSSSSSS")
            random_hex = secrets.token_hex(8)
            _, f_ext = os.path.splitext(image.filename)
            picture_fn = random_hex + f_ext
            picture_path = os.path.join(views.root_path, 'static/restaurant_pics', picture_fn)

            output_size = (125, 125)
            i = Image.open(image)
            i.thumbnail(output_size)
            i.save(picture_path)

            prev_picture = os.path.join(views.root_path, imageLama)
            if os.path.exists(prev_picture):
                os.remove(prev_picture)

            picture_fn2 = "static/restaurant_pics/" + picture_fn

        try:
            db.session.query(Restaurant).filter(Restaurant.rest_id == id).update({'rest_address': address, 'rest_email': email, 'rest_name' : name, 'rest_phonenum': phonenumber, 'rest_desc': description, 'rest_website' : website, 'rest_operatingHour': hour, 'rest_keyword': keyword, 'rest_attractions' : attraction, 'image1_img' : picture_fn2})
            db.session.commit()
            print("@@@@@@@@@@@@@@@@BERJAYA UPDATEEEEEEEEEEE")

            return redirect(url_for('views.view_restaurant'))
            
        except:
            print("@@@@@@@@@@@@@@@@TAKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK BERJAYA UPDATEEEEEEEEEEE")
            return render_template("Admin/1.0.home.html", user=current_user)

    

@views.route('/delete_restaurant', methods=['POST'])
def delete_restaurant():
    
    if request.method == 'POST':
        print("~~~~~~~~~~~~~~~MASUKKKKKKKKKKKKKKKKKKKK delete_restaurant")
        
        id = request.form.get('id')

        imageLama = request.form.get('imageLama')

        prev_picture = os.path.join(views.root_path, imageLama)

        if os.path.exists(prev_picture):
            os.remove(prev_picture)

        try:
            my_data = Restaurant.query.get(id)

            db.session.delete(my_data)
            db.session.commit()
            print("@@@@@@@@@@@@@@@@BERJAYA DELETE")

            return redirect(url_for('views.view_restaurant'))
            
        except:
            print("@@@@@@@@@@@@@@@@TAKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK BERJAYA DELETEEEEEEEEE")
            return render_template("Admin/1.0.home.html", user=current_user)


@views.route('/view_ho', methods=['GET', 'POST'])
@login_required
def view_ho():

    #panggil data from database
    posts = Ho.query.all()

    #print(posts)

    return render_template("Admin/3.0.viewHO.html", user=current_user, posts=posts)

@views.route('/view_ho_user', methods=['GET', 'POST'])
@login_required
def view_ho_user():

    #panggil data from database
    posts = Ho.query.all()

    #print(posts)

    return render_template("User/3.0.viewHO.html", user=current_user, posts=posts)


@views.route('/view_contact', methods=['GET', 'POST'])
@login_required
def view_contact():

    #panggil data from database
    posts = Contact.query.all()

    #print(posts)

    return render_template("User/4.0.viewContact.html", user=current_user, posts=posts)

@views.route('/update_ho', methods=['POST'])
@login_required
def update_ho():
    
    if request.method == 'POST':
        print("~~~~~~~~~~~~~~~MASUKKKKKKKKKKKKKKKKKKKK updatePlace")
        
        id = request.form.get('id')
        address = request.form.get('address')
        email = request.form.get('email')
        name = request.form.get('name')
        phonenumber = request.form.get('phonenumber')
        website = request.form.get('website')
        hour = request.form.get('hour')

        update_image = request.form.get('update_image')
       
        image = request.files['image1']
        imageLama = request.form.get('imageLama')
        
        if(update_image == 'NO'):
            picture_fn2 = imageLama
            print("@@@@@@@@@@@@@@@@@@@@@@@NNNNNNNNNNNNNOOOOOOOOOOOOOOO")
        else:
            print("@@@@@@@@@@@@@@@@@@@@@@@YYYYYYYYYYYYEEEEEEEEESSSSSSS")
            random_hex = secrets.token_hex(8)
            _, f_ext = os.path.splitext(image.filename)
            picture_fn = random_hex + f_ext
            picture_path = os.path.join(views.root_path, 'static/ho_pics', picture_fn)

            output_size = (125, 125)
            i = Image.open(image)
            i.thumbnail(output_size)
            i.save(picture_path)

            prev_picture = os.path.join(views.root_path, imageLama)
            if os.path.exists(prev_picture):
                os.remove(prev_picture)

            picture_fn2 = "static/ho_pics/" + picture_fn

       
        print(id)
        print(address)
        print(email)
        print(name)
        print(phonenumber)
        print(website)
        print(picture_fn2)

        try:
            db.session.query(Ho).filter(Ho.ho_id == id).update({'ho_address': address, 'ho_email': email, 'ho_name' : name, 'ho_phoneNum': phonenumber, 'ho_website' : website, 'ho_operatingHour' : hour, 'image1_img' : picture_fn2})
            db.session.commit()
            print("@@@@@@@@@@@@@@@@BERJAYA UPDATEEEEEEEEEEE")

            return redirect(url_for('views.view_ho'))
            
        except:
            print("@@@@@@@@@@@@@@@@TAKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK BERJAYA UPDATEEEEEEEEEEE")
            return render_template("Admin/1.0.home.html", user=current_user)

    

@views.route('/delete_ho', methods=['POST'])
def delete_ho():
    
    if request.method == 'POST':
        print("~~~~~~~~~~~~~~~MASUKKKKKKKKKKKKKKKKKKKK delete_ho")
        
        id = request.form.get('id')
        print(id)
        try:
            my_data = Ho.query.get(id)

            imageLama = request.form.get('imageLama')

            prev_picture = os.path.join(views.root_path, imageLama)
            if os.path.exists(prev_picture):
                os.remove(prev_picture)

            db.session.delete(my_data)
            db.session.commit()
            print("@@@@@@@@@@@@@@@@BERJAYA DELETE")

            return redirect(url_for('views.view_ho'))
            
        except:
            print("@@@@@@@@@@@@@@@@TAKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK BERJAYA DELETEEEEEEEEE")
            return render_template("Admin/1.0.home.html", user=current_user)





@views.route('/view_user', methods=['GET', 'POST'])
@login_required
def view_user():

    #panggil data from database
    #posts = User.query.all()
    posts = User.query.filter((User.type == "user"))

    #print(posts)
    # posts = User.query.filter(User.type = "user")

    return render_template("Admin/4.0.viewUser.html", user=current_user, posts=posts)


# -----------------------------------------------------------------ADMIN PART------------------------------------------------------------------
@views.route('/view_admin', methods=['GET', 'POST'])
@login_required
def view_admin():

    #panggil data from database
    #posts = User.query.all()
    posts = User.query.filter((User.type == "admin"))

    #print(posts)
    # posts = User.query.filter(User.type = "user")

    return render_template("Admin/5.0.viewAdmin.html", user=current_user, posts=posts)




@views.route('/update_contact', methods=['POST'])
@login_required
def update_contact():
    
    if request.method == 'POST':
        print("~~~~~~~~~~~~~~~MASUKKKKKKKKKKKKKKKKKKKK update_contact")
        
        id = request.form.get('id')
        address = request.form.get('address')
        email = request.form.get('email')
        phonenumber = request.form.get('phone')

       
        print(id)
        print(address)
        print(email)
        print(phonenumber)

        try:
            db.session.query(Contact).filter(Contact.contact_id == id).update({'contact_HQaddress': address, 'contact_email': email, 'contact_phoneNumber': phonenumber})
            db.session.commit()
            print("@@@@@@@@@@@@@@@@BERJAYA UPDATEEEEEEEEEEE")

            return redirect(url_for('views.contact'))
            
        except:
            print("@@@@@@@@@@@@@@@@TAKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK BERJAYA UPDATEEEEEEEEEEE")
            return render_template("Admin/1.0.home.html", user=current_user)




@views.route('/rec_details', methods=['GET', 'POST'])
@login_required
def rec_details():

    
        print("@@@MASUKKKKKKKKKKKKKKKKKKKK rec_details from rec_restaurant.html")
        
        id = request.form.get('rec_id')
        user_id = current_user.id

        print("@@@@@@@@@@@@@@@@")
        print("ID: ")
        print(id)
        

        #panggil data from database
        posts = Restaurant.query.filter_by(rest_id=id).first()
        #posto = Restaurant.query.get(id)   #same as above

        try:
            rate_status = Rating.query.filter_by(id_attraction=id, user_id=user_id).first()

            print("ADA KE ?")
            print(rate_status)
        except:
            print("TAK MASUK rate_status")

        # print(posts)
        print()
        print("@@@@@@@@@@@@@@@@")
        print()
        print()
        print()
        
        #return redirect(url_for('views.rec_detail'))
        return render_template("User/2.2.2.rest_details.html", user=current_user, posts=posts, rate_status=rate_status)

@views.route('/rec_place_details', methods=['GET', 'POST'])
@login_required
def rec_place_details():

    
        print("@@@MASUKKKKKKKKKKKKKKKKKKKK rec_place_details from rec_place.html")
        
        id = request.form.get('rec_id')
        user_id = current_user.id

        print("@@@@@@@@@@@@@@@@")
        print("ID: ")
        print(id)
        

        #panggil data from database
        posts = Place.query.filter_by(place_id=id).first()
        #posto = Restaurant.query.get(id)   #same as above


        try:
            rate_status = Rating.query.filter_by(id_attraction=id, user_id=user_id).first()

            print("ADA KE ?")
            print(rate_status)
        except:
            rate_status = "NONE"
            
            print("TAK MASUK rate_status")

        # print(posts)
        print()
        print("@@@@@@@@@@@@@@@@")
        print()
        print()
        print()


        #return redirect(url_for('views.rec_detail'))
        return render_template("User/2.1.2.place_details.html", user=current_user, posts=posts, rate_status=rate_status)





@views.route('/view_place_details', methods=['GET', 'POST'])
@login_required
def view_place_details():

    
        print("@@@MASUKKKKKKKKKKKKKKKKKKKK view_place_details from view_place.html")
        
        id = request.form.get('place_name')

        print("@@@@@@@@@@@@@@@@")
        print("ID: ")
        print(id)
        

        #panggil data from database
        posts = Place.query.filter_by(place_name=id).first()
        #posto = Restaurant.query.get(id)   #same as above

        print(posts)
        print("@@@@@@@@@@@@@@@@")

        #return redirect(url_for('views.rec_detail'))
        return render_template("User/2.1.2.place_details.html", user=current_user, posts=posts)




####################RATE HISTORY - LIST UNTUK PLACE & RESTAURANT###############################
@views.route('/rate_history_place', methods=['GET', 'POST'])
@login_required
def rate_history_place():

        print("------------------------rate_history_place-----------------")
        
        user_id = current_user.id

        #panggil data from database
        posts = Rating.query.filter_by(rate_type="PLACE").all()

        users = User.query.filter_by(id=Rating.user_id).all()

        img = Place.query.all()

        #posts2 = Place.query.filter_by(place_name=Rating.id_attraction).all()

        #print(posts2)

        return render_template("User/5.1.rate_history_place.html", user=current_user, posts=posts, users=users, img=img)

@views.route('/rate_history_restaurant', methods=['GET', 'POST'])
@login_required
def rate_history_restaurant():

        print("------------------------rate_history_restaurant-----------------")
        
        user_id = current_user.id

        #panggil data from database
        posts = Rating.query.filter_by(rate_type="RESTAURANT").all()

        users = User.query.filter_by(id=Rating.user_id).all()

        img = Restaurant.query.all()

        #posts2 = Place.query.filter_by(place_name=Rating.id_attraction).all()

        #print(posts2)

        return render_template("User/5.2.rate_history_restaurant.html", user=current_user, posts=posts, users=users, img=img)

@views.route('/rate_history_placeA', methods=['GET', 'POST'])
@login_required
def rate_history_placeA():

        print("------------------------rate_history_place-----------------")
        
        user_id = current_user.id

        #panggil data from database
        posts = Rating.query.filter_by(rate_type="PLACE").all()

        users = User.query.filter_by(id=Rating.user_id).all()

        img = Place.query.all()

        #posts2 = Place.query.filter_by(place_name=Rating.id_attraction).all()

        #print(posts2)

        return render_template("Admin/4.1.rate_history_place.html", user=current_user, posts=posts, users=users, img=img)

@views.route('/rate_history_restaurantA', methods=['GET', 'POST'])
@login_required
def rate_history_restaurantA():

        print("------------------------rate_history_restaurant-----------------")
        
        user_id = current_user.id

        #panggil data from database
        posts = Rating.query.filter_by(rate_type="RESTAURANT").all()

        users = User.query.filter_by(id=Rating.user_id).all()

        img = Restaurant.query.all()

        #posts2 = Place.query.filter_by(place_name=Rating.id_attraction).all()

        #print(posts2)

        return render_template("Admin/4.2.rate_history_restaurant.html", user=current_user, posts=posts, users=users, img=img)









def get_recommendations_by_keyword(name):
    place_df = pd.read_csv("website/dataset_place.csv",encoding='latin1')
    
    tfidf = TfidfVectorizer(stop_words="english")
    place_df["place_keyword"] = place_df["place_keyword"].fillna("")

    tfidf_matrix = tfidf.fit_transform(place_df["place_keyword"])

    # Compute similarity
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    indices = pd.Series(place_df.index, index=place_df["place_keyword"]).drop_duplicates()
    all_names = [place_df['place_name'][i] for i in range(len(place_df['place_name']))]

    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    idx = indices[name]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]

    tit = place_df['place_name'].iloc[movie_indices]
    dat = place_df['place_keyword'].iloc[movie_indices]
    image = place_df['image1_img'].iloc[movie_indices]
    
    place_from_db = Place.query.all()                   # Output : [<Place 1>, <Place 2>, <Place 3>, <Place 4>]
    place_from_dbName1 = place_from_db[1]                # Output : <Place 1>
    place_from_dbName2 = place_from_db[2] 
    place_from_dbName3 = place_from_db[3] 
    place_from_dbName4 = place_from_db[4] 
    place_from_dbName5 = place_from_db[5] 

    #### OKAY ####
    db = SQLAlchemy()
    DB_NAME = "database.db"
    #nak dapatkan attributes for a place
    try:
        conn = create_connection()
        print("SUCCESSFUL TO CONNECT TO DATABASE           SUCCESSFUL")

        select_all_place(conn)
    except Error as e:
        print("FAILEDDDDDDDDDD TO  displayyyyy         FAILEDDDDDDDDDD")
        print(e)

    print()
    print()
    print(".....get_recommendations_by_keyword.......")
    #print(place_from_csv_name)                #place_from_csv2 =  ALL attributes in csv displayed.
    print(place_from_dbName1)
    print(place_from_dbName2)
    print(place_from_dbName3)
    print(place_from_dbName4)
    print(place_from_dbName5)
    print()
    print()

    return_df = pd.DataFrame(columns=['place_name','place_keyword','image1_img'])

    return_df['place_name'] = tit               #!! recommendation :: place name - ada 10
    return_df['place_keyword'] = dat            #!! recommendation :: place keyword - ada 10
    return_df['image1_img'] = image

    return return_df
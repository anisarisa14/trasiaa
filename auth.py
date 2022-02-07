# dari sini dia navigate pegi views.py using    return redirect(url_for('views.Ahome'))
 
from tkinter import messagebox
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from .models import User, Admin, Place, Restaurant, Ho, imageplace
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from PIL import Image
import os
import secrets
from flask_wtf.file import FileField, FileAllowed, FileRequired

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if user.passwordOri == password:
                print('Logged in successfully!')
                login_user(user, remember=True)

                if user.type == 'user':    
                    return redirect(url_for('views.home'))
                else:
                    return redirect(url_for('views.home'))
            else:
                flash("Incorrect password! Please re-enter your e-mail and password again.")
                
                print("INCORRECT PASSWORD ! PLEASE RE-ENTER YOUR PASSWORD !!")
                return render_template("login.html", user=current_user)
        else:
            flash("E-mail does not exist! Please ensure that you are registered, if not, please sign up for a new account.")
            return render_template("login.html", user=current_user)

    return render_template("login.html", user=current_user)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        ic = request.form.get('ic')
        gender = request.form.get('gender')
        address = request.form.get('address')
        phone_number = request.form.get('phone_number')
        status = 'active'
        type = 'user'

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 3:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, name=name, address=address, ic=ic, status=status, type=type, gender=gender, phone_number=phone_number, passwordOri = password1, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)


@auth.route('/add_admin', methods=['GET', 'POST'])
def add_admin():

    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('firstName')
        password1 = request.form.get('password1')
        ic = request.form.get('ic')
        gender = request.form.get('gender')
        address = request.form.get('address')
        phone_number = request.form.get('phone_number')
        status = 'active'
        type = 'admin'

        image = "static\profile_pics\DEFAULT.jpg"

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(password1) < 3:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, name=name, address=address, ic=ic, status=status, type=type, gender=gender, phone_number=phone_number, passwordOri = password1, password=generate_password_hash(
                password1, method='sha256'), image_file=image)
            db.session.add(new_user)
            db.session.commit()
            #login_user(new_user, remember=True)
            flash('Admin successfully registered!', category='success')
            
            print("#############################BERJAYA ADD ADMIN")
            return redirect(url_for('views.view_admin'))

        
        return redirect(url_for('views.view_admin'))

    else:
        return render_template("Admin/5.1.addAdmin.html", user=current_user)


@auth.route('/update', methods=['GET', 'POST'])
def update():

    if request.method == 'POST':
        print("~~~~~~~~~~~~~~~MASUKKKKKKKKKKKKKKKKKKKK")
        
        email = current_user.email
        address = request.form.get('address')
        phone_number = request.form.get('phone_number')
        password = request.form.get('password')
        update_image = request.form.get('update_image')
        imageLama = request.form.get('imageLama')
        image = request.files['image1']
        
        print("!!!!!!!!!!!!PIC LAMA!!!!!!!!!!!!")
        print(imageLama)

        prev_picture = os.path.join(auth.root_path, imageLama)
        substring = "DEFAULT.jpg"


        if substring in prev_picture or update_image == 'NO':
            picture_fn2 = imageLama
            print("AAAAAADDDDDDDDDDDAAAAAAAAAAAAAAA")
        #if os.path.exists(prev_picture):
        else:
            print("~~~~~~DELETE OLD PICTURE~~~~~")
            random_hex = secrets.token_hex(8)
            _, f_ext = os.path.splitext(image.filename)
            picture_fn = random_hex + f_ext
            picture_path = os.path.join(auth.root_path, 'static', 'profile_pics', picture_fn)

            picture_fn2 = os.path.join('static','profile_pics', picture_fn)

            output_size = (125, 125)
            i = Image.open(image)
            i.thumbnail(output_size)
            i.save(picture_path)
            
            os.remove(prev_picture)
        
        print("~~~~~~~~~~~~~~~")
        print(prev_picture)
        print(image)
        print()
        print(picture_fn2)
        print("~~~~~~~~~~~~~~")

        #picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png','jpeg'])])

        #image_file = url_for('static', filename='profile_pics/' + current_user.image_file)

        try:
            db.session.query(User).filter(User.email == email).update({'address': address, 'phone_number': phone_number, 'passwordOri' : password, 'image_file' : picture_fn2})
            db.session.commit()
            print("@@@@@@@@@@@@@@@@BERJAYA UPDATEEEEEEEEEEE")

            image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
            return redirect(url_for('views.home'))
            
        except:
            print("@@@@@@@@@@@@@@@@TAKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK BERJAYA UPDATEEEEEEEEEEE")
            image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
            return render_template("User/1home.html", user=current_user, image=image_file)

    else:
        print('~~~~~~~~~~~~~~~TAK MASUKKKKKKKKKKKKKKK')

        image_file = url_for('static', filename='profile_pics/' + current_user.image_file)

        return render_template("User/1.2.updateDetails.html", user=current_user, image=image_file)


@auth.route('/delete_acc', methods=['GET', 'POST'])
def delete_acc():
    user=current_user

    if request.method == 'POST':
        print("~~~~~~~~~~~~~~~MASUKKKKKKKKKKKKKKKKKKKK delete_acc")
        
        id = request.form.get('id')
        print(id)

        imageLama = request.form.get('imageLama')

        prev_picture = os.path.join(auth.root_path, imageLama)
        if os.path.exists(prev_picture):
            os.remove(prev_picture)


        try:
            my_data = User.query.get(id)

            db.session.delete(my_data)
            db.session.commit()
            print("@@@@@@@@@@@@@@@@BERJAYA DELETE")

            return redirect(url_for('index'))
            
        except:
            print("@@@@@@@@@@@@@@@@TAKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK BERJAYA DELETEEEEEEEEE")
            return redirect(url_for('index'))

    else:

        return render_template("User/1.3.deleteAcc.html", user=current_user)


#inactivate admin
@auth.route('/delete_admin', methods=['GET', 'POST'])
def delete_admin():
    
    if request.method == 'POST':
        print("~~~~~~~~~~~~~~~MASUKKKKKKKKKKKKKKKKKKKK")
        
        
        email = request.form.get('email')
        status = request.form.get('status')

        print(email)
        print(status)
        
        try:
            if(status == "ACTIVE"):
                db.session.query(User).filter(User.email == email).update({'status' : "INACTIVE"})
                db.session.commit()
            else:
                db.session.query(User).filter(User.email == email).update({'status' : "ACTIVE"})
                db.session.commit()
                
            print("@@@@@@@@@@@@@@@@BERJAYA UPDATEEEEEEEEEEE")
            print(email)
            return redirect(url_for('views.view_admin'))
            
        except:
            print("@@@@@@@@@@@@@@@@TAKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK BERJAYA UPDATEEEEEEEEEEE")
            return redirect(url_for('views.view_user'))





@auth.route('/add_place', methods=['GET', 'POST'])
def add_place():
    if request.method == 'POST':
        place_name = request.form.get('place_name')
        place_address = request.form.get('place_address')
        place_phoneNumber = request.form.get('place_phoneNumber')
        place_email = request.form.get('place_email')
        place_description = request.form.get('place_description')
        place_fee = request.form.get('place_fee')
        place_type = request.form.get('place_type')
        #place_rating = request.form.get('place_rating')
        #place_numrater = request.form.get('place_numrater')
        place_website = request.form.get('place_website')
        place_keyword = request.form.get('place_keyword')
        place_attractions = request.form.get('place_attractions')
        hour = request.form.get('place_hour')

        image = request.files['image1']
        
        random_hex = secrets.token_hex(8)
        _, f_ext = os.path.splitext(image.filename)
        picture_fn = random_hex + f_ext
        
        if(place_type == "PLACE"):
            picture_path = os.path.join(auth.root_path, 'static/place_pics', picture_fn)
            picture_fn2 = "static/place_pics/" + picture_fn
        else:
            picture_path = os.path.join(auth.root_path, 'static/restaurant_pics', picture_fn)
            picture_fn2 = "static/restaurant_pics/" + picture_fn

        output_size = (125, 125)
        i = Image.open(image)
        i.thumbnail(output_size)
        i.save(picture_path)

        

        
        # print("@@@@@@@@@@@@@@@@@@@@@")
        # print(picture_fn2)
        # print("@@@@@@@@@@@@@@@@@@@@@")

        if(place_type == 'PLACE'):
            new_place = Place(place_name=place_name, place_address=place_address, place_phoneNum=place_phoneNumber, place_email=place_email, place_description=place_description,
                place_fee=place_fee, place_rating=0, place_numrater=0, place_website=place_website, place_keyword=place_keyword, place_attractions=place_attractions, place_operatingHour = hour,
                image1_img=picture_fn2)

            db.session.add(new_place)
            db.session.commit()

            print("88888888 IS SUCCESSFULLY SAVED INTO DB   88888888888")

            return redirect(url_for('views.view_place'))
        else:
            new_restaurant = Restaurant(rest_name=place_name, rest_address=place_address, rest_phonenum=place_phoneNumber, rest_email=place_email, rest_desc=place_description,
                 rest_rating=0, rest_num_rater=0, rest_website=place_website, rest_keyword=place_keyword, rest_attractions=place_attractions, rest_operatingHour = hour,
                 image1_img=picture_fn2, image2_img=None, image3_img=None)

            db.session.add(new_restaurant)
            db.session.commit()

            print("~~~~~~RESTAURANT IS SUCCESSFULLY SAVED INTO DB")

            return redirect(url_for('views.view_restaurant'))

        

    else:
        print('TAK JADI')

    return render_template("Admin/2.1.addPlace.html", user=current_user)

    
    
@auth.route('/add_ho', methods=['GET', 'POST'])
def add_ho():

    if request.method == 'POST':
        ho_id = request.form.get('ho_id')
        ho_name = request.form.get('ho_name')
        ho_address = request.form.get('ho_address')
        ho_email = request.form.get('ho_email')
        ho_phoneNum = request.form.get('ho_phoneNumber')
        ho_website = request.form.get('ho_website')
        
        image = request.files['image1']

        random_hex = secrets.token_hex(8)
        _, f_ext = os.path.splitext(image.filename)
        picture_fn = random_hex + f_ext
        
        picture_path = os.path.join(auth.root_path, 'static/ho_pics', picture_fn)
        picture_fn2 = "static/ho_pics/" + picture_fn
        
        output_size = (125, 125)
        i = Image.open(image)
        i.thumbnail(output_size)
        i.save(picture_path)

        try:
            new_place = Ho(ho_id=ho_id, image1_img=picture_fn2, ho_name=ho_name, ho_address=ho_address, ho_email=ho_email, ho_phoneNum=ho_phoneNum, ho_website=ho_website)

            db.session.add(new_place)
            db.session.commit()

            print("~~~~~~HO IS SUCCESSFULLY SAVED INTO DB")

            return redirect(url_for('views.view_ho'))
        except:
            print("@@@@@@@@@@@@@@@@TAKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK BERJAYA ADDDDDDDDDDD")
            return render_template("Admin/3.1.addHo.html", user=current_user)

    else:
        print('~~~~~~~~~~~~~~~TAK MASUKKKKKKKKKKKKKKK')
        return render_template("Admin/3.1.addHo.html", user=current_user)







############### ADMIN #################################

@auth.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        admin = Admin.query.filter_by(admin_email=email).first()
        
        if admin:
            if admin.admin_password == password:
                print('Logged in successfully!')
                return render_template("Admin/1home.html", user=current_user)
            else:
                print('Incorrect password, try again.')
        else:
            print('Email does not exist.')

    return render_template("loginA.html", user=current_user)









@auth.route('/updateAdmin', methods=['GET', 'POST'])
def updateAdmin():


    if request.method == 'POST':
        print("~~~~~~~~~~~~~~~MASUKKKKKKKKKKKKKKKKKKKK")
        
        email = current_user.email
        address = request.form.get('address')
        phone_number = request.form.get('phone_number')
        password = request.form.get('password')
        update_image = request.form.get('update_image')
        imageLama = request.form.get('imageLama')
        image = request.files['image1']
        
        print("!!!!!!!!!!!!PIC LAMA!!!!!!!!!!!!")
        print(imageLama)

        prev_picture = os.path.join(auth.root_path, imageLama)
        substring = "DEFAULT.jpg"


        if substring in prev_picture or update_image == 'NO':
            picture_fn2 = imageLama
            print("AAAAAADDDDDDDDDDDAAAAAAAAAAAAAAA")
        #if os.path.exists(prev_picture):
        else:
            print("~~~~~~DELETE OLD PICTURE~~~~~")
            random_hex = secrets.token_hex(8)
            _, f_ext = os.path.splitext(image.filename)
            picture_fn = random_hex + f_ext
            picture_path = os.path.join(auth.root_path, 'static', 'profile_pics', picture_fn)

            picture_fn2 = os.path.join('static','profile_pics', picture_fn)

            output_size = (125, 125)
            i = Image.open(image)
            i.thumbnail(output_size)
            i.save(picture_path)
            
            os.remove(prev_picture)
        
        print("~~~~~~~~~~~~~~~")
        print(prev_picture)
        print(image)
        print()
        print(picture_fn2)
        print("~~~~~~~~~~~~~~")

        #picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png','jpeg'])])

        #image_file = url_for('static', filename='profile_pics/' + current_user.image_file)

        try:
            db.session.query(User).filter(User.email == email).update({'address': address,'phone_number': phone_number, 'passwordOri' : password, 'image_file' : picture_fn2})
            db.session.commit()
            
            print("@@@@@@@@@@@@@@@@BERJAYA UPDATEEEEEEEEEEE")
            print("image updated in database, folder & successfully displayed in page")

            image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
            return redirect(url_for('views.home'))
            
        except:
            print("@@@@@@@@@@@@@@@@TAKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK BERJAYA UPDATEEEEEEEEEEE")
            return render_template("Admin/1.0.home.html", user=current_user, image=image_file)

    else:
        print('~~~~~~~~~~~~~~~TAK MASUKKKKKKKKKKKKKKK')

        image_file = url_for('static', filename='profile_pics/' + current_user.image_file)

        return render_template("Admin/1.1.updateDetails.html", user=current_user, image=image_file)
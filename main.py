from website import create_app
from flask import render_template

#Database engine & session creation.
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#engine = create_engine('sqlite:///TRASIA/database.db', convert_unicode=True)
#db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

app = create_app()

# Set up the main route
@app.route('/')
def index(): 
    return render_template("indexHome.html")



if __name__ == '__main__':
    
    app.run(debug=True)
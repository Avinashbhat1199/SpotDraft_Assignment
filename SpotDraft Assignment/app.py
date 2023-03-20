from flask import Flask , render_template,request,jsonify
from urllib.request import urlopen
import os 
import requests
from flask_sqlalchemy import SQLAlchemy

import json

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from flask_migrate import Migrate

db = SQLAlchemy(app)
Migrate(app,db)


class movies(db.Model):
           __tablename__ = 'movie'

           name = db.Column(db.String(80),primary_key=True)
    
           created = db.Column(db.String)
           updated=db.Column(db.String)
           url=db.Column(db.String)
           is_fav=db.Column(db.Boolean)


    # This sets what an instance in this table will have
    # Note the id will be auto-created for us later, so we don't add it here!
           def __init__(self,name,created,updated,url,is_fav):
                        self.name = name
                        self.created=created
                        self.updated = updated
                        self.url=url
                        self.is_fav=is_fav

class planet(db.Model):
           __tablename__ = 'planet'

           name = db.Column(db.Text,primary_key=True)
    
           created = db.Column(db.Text)
           updated=db.Column(db.Text)
           url=db.Column(db.Text)
           is_fav=db.Column(db.Boolean)


    # This sets what an instance in this table will have
    # Note the id will be auto-created for us later, so we don't add it here!
           def __init__(self,name,created,updated,url,is_fav):
                        self.name = name
                        self.created=created
                        self.updated = updated
                        self.url=url
                        self.is_fav=is_fav


class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    type = db.Column(db.String(10))
    item_id = db.Column(db.Integer)
    custom_title = db.Column(db.String(100))


@app.route('/', methods = ['GET'])
def index():
    
        return render_template('index.html')
    
@app.route('/planet', methods = ['GET'])

def planets():
    pla=[]
    
    if(request.method == 'GET'):
        url = "https://swapi.dev/api/planets/"
        data=requests.get(url,verify=False)
        jsondata=data.json()
        for child in jsondata['results']:
                      name=child['name']
                      created=child['created']
                      updated=child['edited']
                      url=child['url']
                      is_fav=False
                      pla.append({'name':name,'created':created,'edited':updated,'url':url,'is_fav':is_fav})
                      new=planet(name,created,updated,url,is_fav)
                      j=json.dumps(pla)
                     
                      #db.session.add(new)
                     
                      #db.session.commit()
                      all_movies=planet.query.all()
        #return render_template('movie.html',data=all_movies)
        return jsonify(j)
    
   
movie_list=[]   
@app.route('/movie', methods = ['GET'])
def movie():   
        mov=[]
        if(request.method == 'GET'):
              url = "https://swapi.dev/api/films/"
              data=requests.get(url,verify=False)
              jsondata=data.json()
              for child in jsondata['results']:
                      name=child['title']
                      created=child['created']
                      updated=child['edited']
                      url=child['url']                          
                      is_fav=False
                      mov.append({'name':name,'created':created,'edited':updated,'url':url,'is_fav':is_fav})
                      #new=movies(name,created,updated,url,is_fav)
                      json_movie_Data=json.dumps(mov)
                     
                      #db.session.add(new)
                     
                      
                      #all_movies=movies.query.all()
        #return render_template('movie.html',data=all_movies)
        return jsonify(json_movie_Data)
@app.route('/favorites/movie/', methods = ['POST'])   
def favmovie():
        if request.is_json:
                 query=request.get_json()
                 if query['id']==None:
                         return "405"
                 
                 planetname=query['moviename']
                 #customname=query['customname']
                 url = "https://swapi.dev/api/planets/"
                 data=requests.get(url,verify=False)
                 jsondata=data.json()
                 if planetname in jsondata['result']:
                               for child in jsondata['results']:
                                    
                                            
                                       name=child['title']
                                       created=child['created']
                                       updated=child['edited']
                                       url=child['url']                          
                                       is_fav=True
                                       movie_list.append({'id':query['id'],'customname':query['customname'],'name':name,'created':created,'edited':updated,'url':url,'is_fav':is_fav})
                                       return json.dumps(movie_list)
planetlist=[]
@app.route('/favorites/planet/', methods = ['POST'])   
def favmovie():
        if request.is_json:
                 query=request.get_json()
                 if query['id']==None:
                         return "405"
                 
                 moviename=query['moviename']
                 #customname=query['customname']
                 url = "https://swapi.dev/api/films/"
                 data=requests.get(url,verify=False)
                 jsondata=data.json()
                 if moviename in jsondata['result']:
                               for child in jsondata['results']:
                                    
                                            
                                       name=child['name']
                                       created=child['created']
                                       updated=child['edited']
                                       url=child['url']                          
                                       is_fav=True
                                       planetlist.append({'id':query['id'],'customname':query['customname'],'name':name,'created':created,'edited':updated,'url':url,'is_fav':is_fav})
                                       return json.dumps(planetlist)
@app.route('/favorites/search/movie', methods = ['POST'])       
def search():
        query=request.get_json()
        if query['titile']==None:
                         return "405"
                 
        moviename=query['title']

        
        search=movies.query.filter_by(title=moviename)
        return json.dumps(search)
        
@app.route('search/planet', methods = ['POST'])       
def search():
        query=request.get_json()
        if query['titile']==None:
                         return "405"
                 
        planetname=query['name']

        
        search=planet.query.filter_by(name=planetname)
        return json.dumps(search)
if __name__ =="__main__":
    app.run(debug=True)
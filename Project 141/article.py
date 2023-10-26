from flask import Flask, jsonify, request
import csv

articles = []

likedArticles = []
notLikedArticles = []

with open('articles.csv', 'r', encoding= 'utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]



app = Flask(__name__)

@app.route("/articles")
def article12():
    return jsonify({
        "data": articles[0],
        "status": "success"
    })
@app.route("/notLiked")
def anotliked():
    return jsonify({
        
        "status": "success"
    })
@app.route("/Liked")
def aliked():
    return jsonify({
        
        "status": "success"
    })

if __name__ == "__main__":
  app.run()
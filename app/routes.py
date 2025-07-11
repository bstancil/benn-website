from app import app
from app import opengraph

from flask import Flask, render_template

import requests

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/twitter-interstitial')
def twitter_interstitial():
    return render_template('twitter-interstitial.html')

@app.route('/p/<dynamic_page>')
def dynamic_page(dynamic_page):
    
    substack_url = f'https://benn.substack.com/p/{dynamic_page}'
    related_url = f'https://benn.substack.com/api/v1/archive?sort=new&search=&offset=0&limit=11'
    
    ogs = opengraph.OpenGraph(url=substack_url)
    
    if ogs.is_valid() and 'benn.substack' not in ogs.title:

        try:
            js = requests.get(related_url).json()
            related = [{"title":r['title'], "slug":r['slug']} for r in js if r['slug'] != dynamic_page]
        except:
            related = []

        return render_template('post.html', 
            title=ogs.title, 
            image=ogs.image, 
            description=ogs.description, 
            substack_url=substack_url,
            related=related
        )
        
    else:
        return render_template('404.html'), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, port=8000)

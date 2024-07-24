from app import app
from app import opengraph

from flask import Flask, render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/twitter-interstitial')
def twitter_interstitial():
    return render_template('twitter-interstitial.html')

@app.route('/p/<dynamic_page>')
def dynamic_page(dynamic_page):
    
    substack_url = f'https://benn.substack.com/p/{dynamic_page}'
    
    ogs = opengraph.OpenGraph(url=substack_url) 
    
    if ogs.is_valid() and 'benn.substack' not in ogs.title:
        return render_template('post.html', 
            title=ogs.title, 
            image=ogs.image, 
            description=ogs.description, 
            substack_url=substack_url
        )
        
    else:
        return render_template('404.html'), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, port=8000)

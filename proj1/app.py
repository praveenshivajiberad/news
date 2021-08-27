from flask import Flask,redirect,request,render_template,url_for
import data as df


app=Flask(__name__,template_folder='template')

@app.route('/')
def home():
    articles=df.gettopheadlines()
    return render_template('h.html',articles=articles,title='Top headlines')
@app.route('/top-headlines')
def gettopheadlines():
    articles=df.gettopheadlines()
    return render_template('articles.html',articles=articles,title='Top headlines')

@app.route('/search',methods=['POST'])
def search_news():
    search_keyword=request.form['search']
    art=df.getevery(search_keyword)
    return render_template('articles.html',articles=art,title='Search Page')

@app.route('/category/<cate>')
def category_news(cate):
    articles=df.getevery(cate)
    return render_template('articles.html',articles=articles,title=cate.capitalize)


if (__name__) == '__main__':
    port=int(os.environ.get('PORT',5000))
    app.run(debug=True)
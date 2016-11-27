from flask import Flask, render_template, redirect, request, url_for,flash
import bs4 as bs
import urllib

app = Flask(__name__)
app.secret_key = "super secret key"


@app.route('/', methods=["GET", "POST"])
def index():

    ticker = {'APPLE':'AAPL', 'YAHOO':'YHOO', 'ALPHABET':'GOOGL'}
    company = ""
    value = ""

    try:
        if request.method == "POST":
            company = str(request.form['ticker'])
            comp = ticker[company.upper()]
            yahoo = urllib.urlopen('https://in.finance.yahoo.com/q?s=' + comp).read()
            soup = bs.BeautifulSoup(yahoo,'html.parser')
            identifier = "yfs_l84_"+comp.lower()
            span = soup.find('span', id=identifier)
            value = span.text

    except Exception as e:
        print e

    return render_template("index.html",company=company.upper(),value=value)

app.run()
app.debug()
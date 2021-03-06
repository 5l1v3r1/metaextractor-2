import json
import os
from settings import METAEXTRACTOR_CONFIG
from metaextractor import extract, ContentHolder
from flask_cors import cross_origin
from flask import Flask,abort, request, redirect, Response
app = Flask(__name__, static_url_path='/static')

@app.route("/metaextract", methods=['GET'])
@cross_origin()
def mo():
    if len(request.args)==0 or request.args.get("url")=="": #if you have no parameters then redirect to the static page
        return redirect("/extracturl")
    else: 
        url = request.args.get("url")
        config = dict(METAEXTRACTOR_CONFIG.items())
        if request.args.get("config"):
             config.update(json.loads(request.args.get("config")))
        ret = extract(config = config, url=url)
        return Response(json.dumps(ret ,encoding='utf-8', ensure_ascii=True), mimetype="text/json")


@app.route('/extracturl', methods=['GET'])
@app.route('/extracturl.html', methods=['GET'])
def static_extracturl():  
    return  app.send_static_file('extracturl.html')

if __name__ == "__main__":
    app.run(debug=True)
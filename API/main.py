from flask import Flask,jsonify
from flask_pymongo import PyMongo
from bson import json_util
from dotenv import load_dotenv
import json
import os
load_dotenv()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO")
mongo = PyMongo(app)
print('Db connected')

@app.route("/")
def index():
    return "API is Up"

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/en/<int:count>', methods=['GET'])
def getEnglish(count):
    if count > 25:
        return jsonify({'error': 'max 25'})
    array = []
    cursor = mongo.db.English.aggregate([{"$sample": {"size": count}}])
    for document in cursor:
        del document['_id']
        array.append(document)
    page_sanitized = json.loads(json_util.dumps(array))
    return jsonify(page_sanitized)


@app.route('/hi/<int:count>', methods=['GET'])
def getHindi(count):
    if count > 25:
        return jsonify({'error': 'max 25'})
    array = []
    cursor = mongo.db.Hindi.aggregate([{"$sample": {"size": count}}])
    for document in cursor:
        del document['_id']
        array.append(document)
    page_sanitized = json.loads(json_util.dumps(array))
    return jsonify(page_sanitized)


#if __name__ == "__main__":
#    app.run()


# [ { $sample: { size: 10 } } ]

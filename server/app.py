import config
import os

from datetime import date
from flask import Flask, jsonify, send_from_directory
from flask.json import JSONEncoder
from flask_cors import CORS
#TODO: Check if CORS is properly set in vue


class CustomJSONEncoder(JSONEncoder):
    """Use ISO 8601 for dates"""

    def default(self, obj):  # noqa: E0202
        try:
            if isinstance(obj, date):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
app.config["SECRET_KEY"] = config.flask_secret_key
CORS(app)


@app.route("/api/file/<string:filename>")
def images_get(filename):
    return send_from_directory(config.image_upload_folder, filename)


from views.authentication import *  # noqa
from views.posts import *  # noqa
from views.subvues import *  # noqa
from views.users import *  # noqa

import errors  # noqa


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        "error": "API endpoint not found"
    }), 404


@app.errorhandler(500)
@app.errorhandler(405)
def internal_server_error(e):
    return jsonify({
        "error": "Internal server error"
    }), 500


@app.errorhandler(413)
def request_entity_too_large(e):
    return jsonify({
        "error": "To large (max. 1 MB)"
    }), 413


if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    app.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
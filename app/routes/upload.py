from flask import Blueprint, request, jsonify

upload_bp = Blueprint('upload', __name__)

# Test route (important for debugging)
@upload_bp.route("/test", methods=["GET"])
def test():
    return "Upload route is working"

# Upload route
@upload_bp.route("/upload", methods=["POST"])
def upload_resume():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    # Temporary logic (you will replace later)
    return jsonify({
        "message": "File received successfully",
        "filename": file.filename
    })
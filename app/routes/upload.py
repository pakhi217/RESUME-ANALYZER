import fitz  # PyMuPDF
from flask import Blueprint, request, jsonify

upload_bp = Blueprint('upload', __name__)

@upload_bp.route("/upload", methods=["POST"])
def upload_resume():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    try:
        # Read PDF
        pdf = fitz.open(stream=file.read(), filetype="pdf")
        text = ""

        for page in pdf:
            text += page.get_text()

        return jsonify({
            "message": "Resume processed",
            "extracted_text": text[:1000]  # limit output
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
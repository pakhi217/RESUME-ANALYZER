from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to connect

@app.route("/")
def home():
    return "Backend is running!"

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        file = request.files.get("resume")

        if not file:
            return jsonify({"error": "No file uploaded"}), 400

        # For now, just return file info and fake analysis
        return jsonify({
            "message": "File received successfully",
            "filename": file.filename,
            "score": 75,
            "skills_found": ["Python", "Communication"],
            "missing_skills": ["Machine Learning", "SQL"]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, jsonify, request
from week_1.flask_crud_project.students_data import students

app = Flask(__name__)

@app.route("/students")
def get_students():
    """Index route with pagination"""
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))
    start = (page - 1) * limit
    end = start + limit
    data = students[start:end]
    return jsonify({"students": data, "page": page, "limit": limit})

@app.route("/students/<int:student_id>")
def get_student(student_id):
    """Get a student by id"""
    student = next((s for s in students if s["id"] == student_id), None)
    return jsonify(student) if student else (jsonify({"error": "Not found"}), 404)

@app.route("/students", methods=["POST"])
def create_student():
    """Create a student"""
    data = request.json
    new_id = max(s["id"] for s in students) + 1 if students else 1
    data["id"] = new_id
    students.append(data)
    return jsonify(data), 201

@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    """Update a student"""
    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        return jsonify({"error": "Not found"}), 404
    student.update(request.json)
    return jsonify(student)

@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    """Delete a student"""
    global students
    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        return jsonify({"error": "Not found"}), 404
    students = [s for s in students if s["id"] != student_id]
    return jsonify({"deleted": student})

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": "An error occurred", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)

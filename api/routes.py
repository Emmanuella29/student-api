from flask import Blueprint, request, jsonify
from api import db
from api.models import Student

student_bp = Blueprint("students", __name__, url_prefix="/students")

@student_bp.route("/", methods=["GET"])
def get_students():
    students = Student.query.all()
    return jsonify([{"id": s.id, "name": s.name, "age": s.age, "email": s.email} for s in students])

@student_bp.route("/", methods=["POST"])
def add_student():
    data = request.get_json()
    new_student = Student(name=data["name"], age=data["age"], email=data["email"])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Student added successfully!"}), 201


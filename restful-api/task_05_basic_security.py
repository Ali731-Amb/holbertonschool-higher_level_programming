#!/usr/bin/python3
"""
Main module for the Flask API Security project.
Implements Basic Authentication, JWT Authentication, and
Role-Based Access Control (RBAC).
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
    JWTManager
)

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "scrt_JWT"
jwt = JWTManager(app)
auth = HTTPBasicAuth()


"""
In-memory user database with hashed passwords and roles.
"""
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


"""JWT gestion d'erreurs"""


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handles missing or invalid token errors."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handles invalid token errors."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handles expired token errors."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handles revoked token errors."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handles fresh token required errors."""
    return jsonify({"error": "Fresh token required"}), 401


"""Basic Auth"""


@auth.verify_password
def verify_password(username, password):
    """
    Verifies the username and password for Basic Authentication.
    Returns the username if valid, None otherwise.
    """
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """
    Returns a success message if Basic Authentication is valid.
    """
    return ("Basic Auth: Access Granted")


"""JWT"""


@app.route("/login", methods=["POST"])
def login():
    """
    Authenticates a user and returns a JWT access token.
    Expects a JSON payload with 'username' and 'password'.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON in request"}), 400
    username = data.get("username")
    password = data.get("password")
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        access_token = create_access_token(
            identity={"username": username, "role": user["role"]}
                                        )
        return jsonify({"access_token": access_token}), 200
    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """
    Returns a success message if a valid JWT token is provided.
    """
    token = get_jwt_identity()
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """
    Returns a success message only if the user has an 'admin' role.
    Returns 403 Forbidden if the user is authenticated but not an admin.
    """
    identity = get_jwt_identity()
    if identity.get("role") == "admin":
        return "Admin Access: Granted"
    return jsonify({"error": "Admin access required"}), 403


if __name__ == "__main__":
    """Starts the Flask development server."""
    app.run(debug=True)

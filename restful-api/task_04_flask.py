#!/usr/bin/python3
from flask import Flask, jsonify, request


app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """Return a simple welcome message"""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Return a JSON list of all stored usernames."""
    return jsonify(list(users.keys()))


@app.status("/status")
def status():
    """Confirm the API is running."""
    return "OK"


@app.route("/users/<username>")
def get_username(username):
    """Retrieve detailed information for a specific user."""
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user to the memory-stored dictionary."""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()

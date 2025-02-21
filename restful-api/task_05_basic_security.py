#!/usr/bin/python3
'''this modul is for basic security in flask'''
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required
from flask_jwt_extended import create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

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


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Route protégée par JWT."""
    return "JWT Auth: Access Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Gère les erreurs d'absence de token."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Gère les erreurs de token invalide."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Gère les erreurs de token expiré."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Gère les erreurs de token révoqué."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Gère les erreurs nécessitant un token frais."""
    return jsonify({"error": "Fresh token required"}), 401


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Route réservée aux administrateurs."""
    current_user = get_jwt_identity()
    if users[current_user]['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted", 200


@app.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    """Rafraîchit le token JWT."""
    pass


@auth.verify_password
def verify_password(username, password):
    if username in users:
        if check_password_hash(users[username]['password'], password):
            return username


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Route protégée par l'authentification de base."""
    return "Basic Auth: Access Granted", 200


@app.route("/login", methods=["POST"])
def login():
    """Gère la connexion et génère un token JWT."""
    username = request.json.get("username")
    password = request.json.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 401

    if (username in users
            and check_password_hash(users[username]['password'], password)):
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401


if __name__ == "__main__":
    app.run()

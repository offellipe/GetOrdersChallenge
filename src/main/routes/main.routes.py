from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest

from src.main.composer.user_register_composer import user_register_composer
from src.main.composer.login_creator_composer import login_creator_composer

from src.main.middlewares.auth_jwt import auth_jwt_verify

from src.errors.error_handler import handle_errors

main_route = Blueprint("main_route", __name__)

@main_route.route("/orders/registry", methods=["POST"])
def registry_user():
    try:
        http_request = HttpRequest(body=request.json)
        http_response = user_register_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@main_route.route("/user/login", methods=["POST"])
def create_login():
    try:
        http_request = HttpRequest(body=request.json)
        http_response = login_creator_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@main_route.route("/user/order/<user_id>", methods=["PATCH"])
def edit_balance(user_id):
    try:
        token_information = auth_jwt_verify()
        http_request = HttpRequest(
            body=request.json,
            params={ "user_id": user_id },
            token_infos=token_information,
            headers=request.headers
            )
        http_response = user_register_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    Response,
    redirect,
    url_for,
    Blueprint,
    session,
)
import os
import requests
import src.service.example_service as example_service

example_controller = Blueprint("example_controller", __name__)


@example_controller.route("/health/", methods=["GET"])
def health():
    return jsonify({"Health": "Ok"})


@example_controller.route("/os_info/", methods=["GET"])
def test_endpoint():

    # Using a service from another folder
    os_info = example_service.get_os_info()

    return jsonify(os_info)

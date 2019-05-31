"""Initialize pulling Jira issues."""
from flask import Flask, make_response, request, jsonify
from flask_cors import CORS
from db import Database


def main(request):
    """Entry point."""
    db = Database()
    projectName = request.args.get('project')
    records = db.create_json_response(projectName)
    response = jsonify(records)
    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.set('Access-Control-Allow-Methods', 'GET, POST')
    return response

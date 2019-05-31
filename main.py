"""Initialize pulling Jira issues."""
from flask import Flask, make_response, request
from flask_cors import CORS
from db import Database


def main(request):
    """Entry point."""
    db = Database()
    projectName = request.args.get('project')
    records = db.create_json_response(projectName)
    return records

import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json

yml_configs = {}
with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)


def handle_request():
    message = g.sms_client.messages.create(
                     body="Welcome new traveller!",
                     from_=yml_configs['twillio']['phone_number'],
                     to='+18583303617'
                 )
    return json_response( sid = message.sid )

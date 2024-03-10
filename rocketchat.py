#encoding:utf8
import requests
import config

headers = {
    'X-Auth-Token': config.auth_token,
    'X-User-Id': config.user_id,
    'Content-type': 'application/json',
}

def send_msg(channel, text, emoji, alias):
    json_data = {
        'channel': channel,
        'text': text,
        'emoji': emoji,
        'alias': alias,
    }
    resp = requests.post(config.url, headers=headers, json=json_data)
    return resp

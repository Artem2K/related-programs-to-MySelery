from typing import Dict

import MySentrySettings
import requests
import traceback


class ErrorLogSender:

    def __init__(self, app_id: int, app_token: str):
        assert isinstance(app_id, int), f'id not int'
        assert isinstance(app_token, str) and len(app_token) != 0, f'token is empty or not string'
        self.id = app_id
        self.token = app_token

    def sender(self, error_log: Dict) -> None:
        assert len(error_log) == 3 and ['error_type', 'error_message', 'error_stack_trace'] == list(error_log.keys()), \
            f'error_log is invalid'
        url = f'http://127.0.0.1:8000/apps/{self.id}/error_log/'
        requests.post(url, data=error_log, headers={'token': self.token})


def error_searcher(fun):
    def wrapper():
        app = ErrorLogSender(MySentrySettings.settings['id'], MySentrySettings.settings['token'])
        try:
            return fun()
        except Exception as error:
            error_dict_for_sender = {
                'error_type': error.__class__.__name__,
                'error_message': error.__str__(),
                'error_stack_trace': ''.join(traceback.format_stack())
            }
            app.sender(error_dict_for_sender)

    return wrapper


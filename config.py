"""
Config file
"""

import os

config = {
    'application_id': os.getenv('APPLICATION_ID'), #An API key can be obtained from https://developers.wargaming.net/applications/
    'api_accounts_template': 'https://api.wotblitz.ru/wotb/account/list'
                                '/?application_id={application_id}&search={username}',
    'api_user_template': 'https://api.wotblitz.ru/wotb/account/info'
                                '/?application_id={application_id}&account_id={user_id}'
}

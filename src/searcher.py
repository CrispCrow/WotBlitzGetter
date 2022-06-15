"""
File for search user's data
"""

import requests

from config import config
from .exceptions import UserNotFoundError


def get_user_info(nickname: str) -> dict:
    """
    Get user's game statistics

    :param nickname: User's name
    :return: JSON object with data
    """

    user_id = get_user_id(nickname)
    formatted = config['api_user_template'].format(
        application_id=config['application_id'],
        user_id=user_id)

    response = requests.get(formatted)

    return response.json()['data'][str(user_id)]['statistics']['all']


def get_user_id(username: str) -> int:
    """
    Find user id by user
    name
    
    :param username: User's name
    :return: User id
    """

    formatted = config['api_accounts_template'].format(
        application_id=config['application_id'], username=username)

    response = requests.get(formatted)

    try:
        return response.json()['data'][0]['account_id']
    except (KeyError, IndexError):
        raise UserNotFoundError(f'User with nickname "{username}" does not exists.')
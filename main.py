"""
The main file
"""

from dotenv import load_dotenv
load_dotenv()

from src.searcher import get_user_id, get_user_info
from src.utils import calculate_percent, separate


def main() -> None:
    """
    Main function.
    App works only with RU-region
    """

    username = input('Enter username: ')

    data = get_user_info(username)
    user_id = get_user_id(username)
    percent = calculate_percent(data['wins'], data['battles'])

    print(
        f'Username: {username}\n',
        f'User ID: {user_id}\n',
        f'Total Battles: {data["battles"]}\n',
        f'Win Percent: {percent}%\n',
        f'Wins: {data["wins"]}\n',
        f'Losses: {data["losses"]}\n',
        f'Max Frags: {data["max_frags"]}\n',
        f'Damage Dealt: {separate(data["damage_dealt"])}\n',
        f'Damage Received: {separate(data["damage_received"])}'
        )

if __name__ == '__main__':
    main()
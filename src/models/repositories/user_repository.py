from typing import Tuple
from sqlite3 import Connection
from src.models.interface.user_repository import UserRepositoryInterface

class UserRepository(UserRepositoryInterface):
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_user(self, username: str, password: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO users
                (username, password)
            VALUES
                (?, ?, ?);
            ''', (username, password)
        )
        self.__conn.commit()

    def get_order_by_user(self, user_id: int) -> Tuple[int, str, str, str]:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            SELECT id, user_id, date_order, description
            FROM orders
            WHERE user_id = ?;
            """, (user_id,)
        )

        order_data = cursor.fetchone()

        return order_data


    def get_user_by_username(self, username: str) -> Tuple[int, str, str]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            SELECT id, username, password
            FROM users
            WHERE username = ?
            ''', (username,)
        )
        user = cursor.fetchone()
        return user

from database.database import Database
from models.room import Room
from models.user import User
from models.meeting import Meeting


class Service:
    def __init__(self, database: Database):
        self.database = database

    def get_all_rooms(self) -> list[Room]:
        pass

    def get_all_users(self) -> list[User]:
        pass

    def get_room_meetings(self, room_id) -> list[Meeting]:
        pass

    def get_user_meetings(self, user_id) -> list[User]:
        pass

    def reserve_room(self, room_id, user_id, participants, date, start_time, end_time):
        pass

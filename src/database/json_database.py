from database.database import Database
from models.room import Room
from models.meeting import Meeting
from models.user import User


class JsonDatabase(Database):
    def __init__(self, data_path: str):
        self.data_path = data_path

    def get_all_rooms(self) -> list[Room]:
        pass

    def get_all_users(self) -> list[User]:
        pass

    def get_all_meetings(self) -> list[Meeting]:
        pass

    def insert_room(self, room: Room):
        pass

    def insert_user(self, user: User):
        pass

    def insert_meeting(self, meeting: Meeting):
        pass


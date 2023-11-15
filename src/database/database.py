from models.room import Room
from models.meeting import Meeting
from models.user import User
from abc import ABC, abstractmethod


class Database(ABC):

    @abstractmethod
    def get_all_rooms(self) -> list[Room]:
        pass

    @abstractmethod
    def get_all_users(self) -> list[User]:
        pass

    @abstractmethod
    def get_all_meetings(self) -> list[Meeting]:
        pass

    @abstractmethod
    def insert_room(self, room: Room):
        pass

    @abstractmethod
    def insert_user(self, user: User):
        pass

    @abstractmethod
    def insert_meeting(self, meeting: Meeting):
        pass

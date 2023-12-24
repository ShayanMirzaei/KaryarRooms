from database.database import Database
from models.room import Room
from models.meeting import Meeting
from models.user import User
from json import dump, load


class JsonDatabase(Database):
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.data = dict()
        self.exc_data()

    def exc_data(self):
        try:
            with open(self.data_path) as json_data:
                self.data: dict = load(json_data)
        except :
            self.data = dict()

    def get_all_rooms(self) -> list[Room]:
        lst_room = list()
        rooms_list: list[dict] = self.data['rooms']

        for room_dict in rooms_list:  
            room = Room(room_id=room_dict['room_id'],#or(**room_dict)
                        name=room_dict['name'],
                        floor=room_dict['floor'],
                        capacity=room_dict['capacity'])
            lst_room.append(room)

        return lst_room
             
    def get_all_users(self) -> list[User]:
        lst_user = list()
        users_list: list[dict] = self.data['users']

        for user_dict in users_list:
            user = User(**user_dict)
            lst_user.append(user)

        return lst_user
        
    def get_all_meetings(self) -> list[Meeting]:
        lst_meet = list()
        meets_list: list[dict] = self.data['meetings']

        for meet_dict in meets_list:
            meet = Meeting(**meet_dict)
            lst_meet.append(meet)

        return lst_meet
    
    def insert_room(self, room: Room):
        rooms: list = self.data.setdefault("rooms", [])
        rooms.append(vars(room))

        with open(self.data_path, "w") as json_data:
            dump(self.data, json_data, indent=2)

    def insert_user(self, user: User):
        users: list = self.data.setdefault("users", [])
        users.append(vars(user))

        with open(self.data_path, "w") as json_data:
            dump(self.data, json_data, indent=2)

    def insert_meeting(self, meeting: Meeting):
        meets: list = self.data.setdefault("meetings", [])
        meets.append(vars(meeting))

        with open(self.data_path, "w") as json_data:
            dump(self.data, json_data, indent=2)
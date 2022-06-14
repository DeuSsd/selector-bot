from abc import ABC, abstractmethod
import random
from tkinter.tix import Tree
from models.models import *
from datetime import datetime
from peewee import ModelSelect

from typing import List, Optional, TypeVar

id = TypeVar('id')


class BasicGame(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def _add_new_event(self):
        pass

    @abstractmethod
    def check_available_game(self):
        pass

    @abstractmethod
    def get_user_id(self):
        pass

    @abstractmethod
    def _available_game(self) -> bool:
        pass

    @abstractmethod
    def drop_data(self) -> bool:
        pass


class GameHandsomeOFTheDay(BasicGame):
    # type_game = 'handsome_of_day'

    def __init__(self) -> None:
        super().__init__()

    # was run method
    def check_available_game(self, chat_id: id) -> bool:
        query = Game.select().where(
            (Game.chat_id == chat_id)
        )

        if not len(query):
            return True
        else:
            assert len(query) == 1, "В таблице найдены дубликаты"
            event: Game = query[0]
            return self._available_game(event)

    def _add_new_event(self, chat_id: id, user_id: id) -> id:
        new_record = Game(
            chat_id=chat_id,
            user_id=user_id,
            date_handsome_of_day=datetime.date(datetime.now()),
            handsome_of_day=True,
        )
        new_record.save()

        return new_record.id

    def _available_game(self, record_game: Game) -> bool:
        return not record_game.date_handsome_of_day == datetime.date(datetime.now())
    
    # def _update_event(self, record_event: Game) -> bool:
        # if self._available_game(record_event):
        #     # record_event.date_handsome_of_day = datetime.now()
        #     # record_event.save()
        #     return True
        # else:
        #     return False

    # TODO вызывать данный метод в run
    def update_event(self, chat_id: id, new_user_id: id) -> None:
        query = Game.select().where(
            (Game.chat_id == chat_id)
        )

        if not len(query):
            self._add_new_event(
                chat_id=chat_id,
                user_id=new_user_id
            )
        else:
            assert len(query) == 1, "В таблице найдены дубликаты"
            record_game: Game = query[0]
            record_game.date_handsome_of_day = datetime.now()
            record_game.user_id = new_user_id
            record_game.save()

    # TODO вызывать данный метод в run
    def get_user_id(self, chat_id: id) -> Optional[id]:
        query = Game.select(Game.user_id).where(
            (Game.chat_id == chat_id)
        )
        if not len(query):
            return None
        else:
            assert len(query) == 1, "В таблице найдены дубликаты"
            event: Game = query[0]
            return event.user_id

    def drop_data(self, chat_id: id) -> bool:
        query = Game.select().where(
            (Game.chat_id == chat_id)
        )
        flag = False
        for id in query:
            flag = Game.delete_by_id(id)
            print(f"Game was removed {id} chat_id = {chat_id};")

        return flag


HandsomeOFTheDay = GameHandsomeOFTheDay()


if __name__ == "__main__":
    chat_id = -553294046
    user_id = 390239427
    # remove_dublicate_user(chat_id, user_id)
    # print(add_user_if_not_exist(chat_id, user_id))
    # remove_user(chat_id, user_id)
    # select_users_in_chat(chat_id)
    print(HandsomeOFTheDay.run(chat_id, user_id))
    print(HandsomeOFTheDay.update_event(chat_id, user_id))
    # print(get_statistics(chat_id))
    # for i in range(1000000):
    # randomly_choose_one_user(chat_id)
    # print(get_statistics(chat_id))
    # print(randomly_choose_one_user(chat_id).split("\n"))

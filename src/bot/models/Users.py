import ABC, ABCMeta

class Model(ABC):
    def __init__(self) -> None:
        super().__init__()

    

class User(Model):
    def __init__(self, 
                 id: int,
                 first_name: str,
                 last_name: str,
                #  username: str,
                 ) -> None:
        super().__init__()
        __id: int = id
        __first_name: str = first_name
        __last_name: str = last_name 
        # __username: str = username 
        
        
        
    def get_fullname(self):
        

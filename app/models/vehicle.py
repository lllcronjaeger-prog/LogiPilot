from dataclasses import dataclass
@dataclass
class Vehicle:
 vehicle_id:int|None; kennzeichen:str; alias:str|None=None; aktiv:bool=True

from dataclasses import dataclass
from datetime import date
@dataclass
class Shipment:
 shipment_id:int|None; sendungsnummer:str; kennzeichen:str; unternehmer:str; entladedatum:date; kalenderwoche:int; standort:str='Leipzig'; erloes:float|None=None; kosten:float|None=None

import re
def normalize_plate(p:str)->str:
 p=(p or '').upper().replace('-','').replace(' ','')
 m=re.match(r'([A-Z]{1,3})([A-Z]{1,3})(\d+)',p)
 return f"{m.group(1)}-{m.group(2)} {m.group(3)}" if m else p

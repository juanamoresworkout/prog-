from dataclasses import dataclass, asdict
from datetime import datetime
import json


@dataclass
class Message :
    id: int 
    send_date: datetime 
    sender_id: int
    receiver_id: int 
    room_id: int
    content: str 
    content_type: str



message = Message (1,datetime.now(),10, 20,45,"Hola gente", "text/plain") 
text = json.dumps(asdict(message), default=str)
print(message )

# ✅ Deserializar (convertir de JSON a objeto Message)
data = json.loads(text)
# Convertir la fecha desde string a datetime otra vez
data["send_date"] = datetime.fromisoformat(data["send_date"])

message_obj = Message(**data)

print("\nObjeto deserializado:")
print(message_obj)
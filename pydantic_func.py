import hashlib

from pydantic import BaseModel, validator


class DataModel(BaseModel):
    name: str

    @validator("name")
    def check_name(cls, v):
        v = "".join(v.split())
        if len(v) > 0 and len(v) < 64:
            v = hashlib.md5(v.encode()).hexdigest()
            return v
        elif len(v) > 64:
            return "Строка слшком длинная"
        elif len(v) == 0:
            return "Строка не должа быть пустой"
        else:
            return "Что-то сломалось"

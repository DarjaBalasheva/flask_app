from marshmallow import Schema, ValidationError, fields


def validate_name(name):
    name = "".join(name.split())
    if len(name) > 64:
        raise ValidationError("Строка слшком длинная")
    elif len(name) == 0:
        raise ValidationError("Строка не должа быть пустой")
    else:
        ValidationError("Что-то сломалось")


def type_message(type):
    if type != "md5":
        if type != "sha256":
            raise ValidationError('Тип строки должен быть "md5" или "sha256"')


class MarshModel(Schema):
    name = fields.String(validate=validate_name)
    type = fields.String(validate=type_message)

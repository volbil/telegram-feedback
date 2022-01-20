from datetime import datetime
from pony import orm

db = orm.Database()

class Message(db.Entity):
    _table_ = "codepillow_messages"

    created = orm.Optional(datetime, default=datetime.utcnow)
    offers = orm.Required(bool)
    message = orm.Required(str)
    email = orm.Required(str)

from datetime import datetime
from pony import orm

db = orm.Database()

class Message(db.Entity):
    _table_ = "codepillow_messages"

    created = orm.Optional(datetime, default=datetime.utcnow)
    offers = orm.Required(bool)
    budget = orm.Required(str)
    message = orm.Required(str)
    email = orm.Required(str)
    name = orm.Required(str)

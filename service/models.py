from datetime import datetime
from pony import orm

db = orm.Database()

class Message(db.Entity):
    _table_ = "codepillow_messages"

    created = orm.Optional(datetime, default=datetime.utcnow)
    budget = orm.Optional(str, nullable=True)
    name = orm.Optional(str, nullable=True)
    message = orm.Required(str)
    offers = orm.Required(bool)
    email = orm.Required(str)

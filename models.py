from app import db,ma

class Actor(db.Model):
    __tablename__ = 'actor'

    actor_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    last_update = db.Column(db.DateTime)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '<actor id {}>'.format(self.actor_id)

class ActorSchema(ma.Schema):
    class Meta:
        fields = ("actor_id", "first_name", "last_name", "last_update")
        model = Actor
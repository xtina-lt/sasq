from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User

class Skeptic:
    db='sasquach_schema'
    def __init__(self, data):
        self.id=data["id"]
        self.creator_id=data["creator_id"]
        self.sighting_id=data["sighting_id"]

    '''CREATE'''
    @classmethod
    def insert(cls, data):
        query="INSERT INTO skeptics(user_id, sighting_id) VALUES(%(user_id)s, %(sighting_id)s)"
        return connectToMySQL(cls.db).query_db(query, data)
        # returns id number
    
    '''DELETE'''
    @classmethod
    def delete(cls,data):
        query="DELETE FROM skeptics WHERE user_id=%(user_id)s"
        return connectToMySQL(cls.db).query_db(query, data)
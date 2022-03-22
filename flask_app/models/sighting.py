from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from datetime import datetime

class Sighting:
    db='sasquach_schema'
    def __init__(self, data):
        self.id=data["id"]
        self.location=data["location"]
        self.detail=data["detail"]
        self.seen=data["seen"].strftime('%m-%d-%Y')
        self.sas_num = data["sas_num"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.creator_id=User.select_one({"id":data["creator_id"]})
        self.holds = self.get_holds({"id":data["id"]})
    
    '''HOLDS / SKEPTICS'''
    @classmethod
    def get_holds(cls, data):
        query="SELECT * FROM skeptics WHERE sighting_id=%(id)s"
        result=connectToMySQL(cls.db).query_db(query, data)
        cls.holds = [User.select_one({"id" : i["user_id"]}) for i in result]
        return cls.holds
        
    '''READ ALL'''
    @classmethod
    def select_all(cls):
        query="SELECT * FROM sightings"
        results=connectToMySQL(cls.db).query_db(query)
        if results:
            return [cls(i) for i in results]
        else:
            return False

    '''READ ONE'''
    @classmethod
    def select_one(cls, data):
        query="SELECT * FROM sightings WHERE id=%(id)s"
        result=connectToMySQL(cls.db).query_db(query, data)
        if result:
            x = cls(result[0])
            return x
        else:
            return False

    '''CREATE'''
    @classmethod
    def insert(cls, data):
        query="INSERT INTO sightings(location, detail, seen, sas_num, creator_id) VALUES(%(location)s, %(detail)s, %(seen)s, %(sas_num)s, %(creator_id)s)"
        return connectToMySQL(cls.db).query_db(query, data)
        # returns id number

    '''UPDATE'''
    @classmethod
    def update(cls,data):
        query="UPDATE sightings SET location=%(location)s, detail=%(detail)s, seen=%(seen)s, sas_num=%(sas_num)s WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, data)


    '''DELETE'''
    @classmethod
    def delete(cls,data):
        query="DELETE FROM sightings WHERE id=%(id)s"
        return connectToMySQL(cls.db).query_db(query, data)
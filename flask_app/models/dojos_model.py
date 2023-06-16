from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import ninjas_model


class Dojo:
    DB = 'dojos_and_ninjas_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.all_ninjas = [] #this will add the ninjas in the dojo

    @classmethod
    def get_all(cls):
        query = """
        SELECT *
        FROM dojos;
        """

        results = connectToMySQL(cls.DB).query_db(query)
        all_dojos = []
        if results:
            for dojo in results:
                all_dojos.append(cls(dojo))
        return all_dojos

    @classmethod
    def get_one(cls, data):
        query = """
        SELECT *
        FROM dojos
        LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
        WHERE dojos.id = %(id)s;
        """

        results = connectToMySQL(cls.DB).query_db(query, data)

        # This would make an instance of a collection
        one_dojo = cls(results[0])

        print(results)

        for row_from_db in results:

            ninja_data = {
                "id": row_from_db['ninjas.id'],
                "first_name": row_from_db['first_name'],
                "last_name": row_from_db['last_name'],
                "age" : row_from_db['age'],
                "created_at" : row_from_db['created_at'],
                "updated_at" : row_from_db['updated_at'],
                "dojo_id" : row_from_db['dojo_id']
            }

            one_dojo.all_ninjas.append( ninjas_model.Ninja(ninja_data) )

        return one_dojo


    @classmethod
    def add_dojo(cls, data):
        query = """
        INSERT
        INTO dojos (name)
        VALUES (%(name)s);
        """

        return connectToMySQL(cls.DB).query_db(query, data)

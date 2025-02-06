import psycopg2

from configuration import config

pg_config = config.postgres

class DB:
    def __get_result_from_query(self, sql):
        conn = psycopg2.connect(
            dbname=pg_config.database,
            user=pg_config.username,
            password=pg_config.userpassword,
            host=pg_config.host,
            port=pg_config.port
        )

        cursor = conn.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        cursor.close()
        conn.close()

        return records

    def __insert_query(self, sql):
            conn = psycopg2.connect(
                dbname=pg_config.database,
                user=pg_config.username,
                password=pg_config.userpassword,
                host=pg_config.host,
                port=pg_config.port
            )

            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()

            cursor.close()
            conn.close()

    def create_collaborators_table(self):
        query = """
            CREATE TABLE users (
                id SERIAL PRIMARY KEY,
                username TEXT NOT NULL
            );
        """

        self.__insert_query(query)

    def add_user(self, username):
        query = f"""
            INSERT INTO "users" ("username")
            VALUES ('{username}')
        """

        self.__insert_query(query)

    def get_user_from_username(self, username):
        query = f"""
            SELECT
                *
            FROM
                "users" AS "us"
            WHERE "us"."username" = '{username}'
        """

        return self.__get_result_from_query(query)
    
    def get_users(self):
        result = list()
        query = "SELECT * FROM \"users\""

        users = self.__get_result_from_query(query)

        for id, username in users:
             result.append({
                  "id": id,
                  "username": username
             })
        
        return result
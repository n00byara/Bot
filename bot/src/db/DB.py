import psycopg2
from configuration.Config import Config

pg_config = Config().postgres

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
                username TEXT NOT NULL,
            );
        """

        self.__insert_query(query)

    def get_user_from_username(self, username):
        query = f"""
            SELECT
                *
            FROM
                "users" AS "us"
            WHERE "us"."username" = {username}
        """

        return self.__get_result_from_query(query)

db = DB()
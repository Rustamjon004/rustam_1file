import psycopg2 
from typing import Optional

conn = psycopg2.connect(database  = 'n44r',
                        user = 'postgres',
                        password = '123',
                        port = '5432')
cursor = conn.cursor()

#create_users_table_ = '''create table users (
#        id serial primary key,
#        first_name varchar(100) not null,
#        last_name varchar(100) not null,
#        email varchar (100) not null,
#        age float check(age > 15),
#        is_active BOOLEAN DEFAULT TRUE


#);'''
#cursor.execute(create_users_table_)
#conn.commit()

class person:
    def __init__(self,
                 first_name:str,
                 last_name:str,
                 email:Optional[str]=None,
                 age: Optional[int]=None,
                 is_activite:Optional[bool]=None
                 ):
        self.first_name =first_name
        self.last_name = last_name
        self.email = email
        self.age = age 
        self.is_active = is_activite

    def save(self):
        insert_into_query = '''
        insert into person (first_name,last_name,email,age,is_active)
        values(%s,%s,%s,%s,%s);

        '''
        data = (self.first_name,self.last_name,self.email,self.age,self.is_active)
        cursor.execute(insert_into_query,data)
        conn.commit()

user = person('rustam','odilov','odilovv.com','19',True)
user.save()

@staticmethod
conn = psycopg2.connect("database = n44r,user = postgres, password = 123, port = 5432")
cursor = conn.cursor()
cursor.execute('selecr * from user ')
rows = cursor.fetchall()
conn.close()


@staticmethod
def get_user(user_id):
        conn = psycopg2.connect("dbname=test user=postgres password=pass")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        row = cursor.fetchone()
        conn.close()          

@staticmethod
def delete_user(user_id):
        conn = psycopg2.connect("dbname=test user=postgres password=pass")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        conn.close()

        
def update_user(self):
        conn = psycopg2.connect("dbname=test user=postgres password=pass")
        cursor = conn.cursor()
        update_query = "UPDATE users SET first_name = %s, last_name = %s, email = %s, age = %s WHERE id = %s"
        cursor.execute(update_query, (self.first_name, self.last_name, self.email, self.age, self.id))
        conn.commit()
        conn.close()

import psycopg2
db_params = {
    'database' : 'n44r',
    'user' : 'postgres',
    'password' : '123',
    'host' : 'localhost',
    'port' : 5432
}

class DBCconnect :
    def __init__(self,db_params):
        self.db_params =db_params

    def __enter__(self):
        self.conn = psycopg2.connect(**self.db_params)
        self.cur = self.conn.cursor()
        return self.conn, self.cur
        
        self.cur =self.conn.cursor()
        return self.conn,self.cur
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        if self.conn:
            self.conn.close()

        if self.cur:
            self.cur.close()
            
with DBCconnect(db_params) as (conn,cur):
    #select_query = ''' select * from car ;'''
    #cur.execute(select_query)
    #rows = cur.fetchall()
    #for row in rows:
     #   print(row)


    create_car = ''' INSERT INTO car (id,name,color,price ) 
                 VALUES (3,'malibu','blue',24000)'''
    #cur.execute(create_car)
    #conn.commit()

    read_cars_lists = ''' SELECT * FROM car; '''
    #cur.execute(read_cars_lists)
    #conn.commit()

    update_car = ''' update car set name = ' Malibu premier turbo ' where id = 3; '''
    cur.execute(update_car)
     conn.commit()

    delete_car = ''' DELETE FROM car WHERE id = 1;'''
    #cur.execute(delete_car)
    #conn.commit()
    

     
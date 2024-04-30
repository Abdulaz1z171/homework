import psycopg2

conn = None
cur = None
try:
    conn =  psycopg2.connect(
        dbname='n42',
        user='postgres',
        password='temur_1336',
        host='localhost',
        port=5432
    ) 
    cur =   conn.cursor()
#  Table create qiladigan funksiya
    def create_table_product():
        create_table_products = """CREATE TABLE IF NOT EXISTS products
                (
                    id SERIAL PRIMARY KEY,
                    product_name VARCHAR(50) NOT NULL,
                    price FLOAT NOT NULL,
                    color VARCHAR(50) NOT NULL,
                    image VARCHAR(300) NOT NULL






                );
                """
                
        cur.execute(create_table_products)
        conn.commit()
            
# Tablega malumot qushadigan funksiya                     
    def insert_information_to_query():
        insert_to_product = """INSERT INTO products(product_name,price,color,image)
            VALUES (%s,%s,%s,%s)
                
                """
        insert_data_list = [('Samsung S 21',758.65,'black','https://www.olx.uz/d/obyavlenie/telefon-v-kredit-iphone-14-pro-max-256gb-ll-a-novyy-ID2XAWz.html'),
                ('Iphone',1255,'white','https://www.olx.uz/d/obyavlenie/telefon-v-kredit-iphone-14-pro-max-256gb-ll-a-novyy-ID2XAWz.html'),
                ('LG frdige','1211','white','https://www.olx.uz/d/obyavlenie/lgelectronics-expresscool-fridge-lg-muzlatgich-lg-holodilnik-ID3Celt.html')]
        
        cur.executemany(insert_to_product,insert_data_list)
        conn.commit()
                
            

#  Table dan malumotni id orqali uchiradigan funksiya
    def delete_query_products(product_id):
        delete_into_query = """DELETE FROM products WHERE id = %s;"""

        cur.execute(delete_into_query, (product_id,))
        conn.commit()
                
# Tabledagi ma'lumot nomini  id orqali uzgartirish
    def update_query_products(product_id, product_name):
        update_query = """UPDATE products SET product_name = %s WHERE id = %s;"""
        data = (product_name,product_id )
        cur.execute(update_query, data)
        conn.commit()
                
# Table dagi ma'lumotlarni hammasini consolga chiqaradigan funksiya
    def select_all_information_from_products():
        select_product_query = '''SELECT * FROM products ;'''
        cur.execute(select_product_query)
        for product in cur.fetchall():
            print(product)

# Table dagi bitta ma'lumotni id orqali chiqarish 
    def select_one_iformation_from_products(product_id):
        get_product_by_id = """SELECT * FROM products WHERE id = %s"""
        cur.execute(get_product_by_id,(product_id,))
        print(cur.fetchone())


except psycopg2.OperationalError as e:
    print(e)


else:
    print('The operation was successful')


finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

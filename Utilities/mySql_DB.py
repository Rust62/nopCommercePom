import mysql.connector

try:
    con = mysql.connector.connect (
        host="localhost" ,
        port=3306 , user="root" ,
        passwd="1999" ,
        database="admin_credentials"
    )
    curs = con.cursor ()
    curs.execute ( "CREATE DATABASE IF NOT EXISTS admin_credentials" )
    curs.execute ( "USE admin_credentials" )
    curs.execute ( "SHOW DATABASES" )
    for database in curs:
        print ( database )

    curs.execute ( """CREATE TABLE  IF NOT EXISTS admin (
                        admin_id int not null,
                        user_name varchar(50) not null,
                        password varchar(50) not null,
                        primary key(admin_id));
                     """ )
    curs.execute ( """CREATE TABLE IF NOT EXISTS admin1 (
                        admin_id int not null,
                        user_name varchar(50) not null,
                        password varchar(50) not null,
                        primary key(admin_id));
                     """ )
    curs.execute ( """CREATE TABLE IF NOT EXISTS admin2 (
                        admin_id int not null,
                        user_name varchar(50) not null,
                        password varchar(50) not null,
                        primary key(admin_id));
                     """ )

    curs.execute ( "SHOW TABLES" )
    for table in curs:
        print ( table )

    curs.execute ( """insert into admin_credentials.admin(admin_id, user_name, password)
                                values(1, 'test1@gmail.com', 'admin1')""")
    curs.execute ( """insert into admin_credentials.admin(admin_id, user_name, password)
                                values(2, 'test2@gmail.com', 'admin2')""" )
    curs.execute ( """insert into admin_credentials.admin(admin_id, user_name, password)
                                values(3, 'test3@gmail.com', 'admin')3""" )
    con.commit()
    curs.execute("select * from admin")
    for row in curs:
        print(row[0], row[1], row[2])
    con.close()
    print("finished....")
except:
    print ( "The connection unsuccessful" )

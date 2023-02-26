import mysql.connector

try:
    con = mysql.connector.connect (
        host="localhost" ,
        port=3306 , user="root" ,
        passwd="1999" ,
        database="`admin_credentials`"
    )
    curs = con.cursor()
    curs.execute("use database `admin_credentials`")
    curs.execute("CREATE TABLE admin('username' varchar(50) not null, 'password' varchar(50) not null )")
    curs.execute("insert into `admin` values ('email', 'password')")
    con.commit()

    con.close()
except:
    print("Unsuccessful connection")
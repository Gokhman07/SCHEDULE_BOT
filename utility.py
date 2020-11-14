import mysql.connector



from telegram import ReplyKeyboardMarkup
from telegram import KeyboardButton

SMILE = ['😊', '😀', '😇', '🤠', '😎', '🤓', '👶', '🧑‍🚀', '👮', '🦸', '🧟']

mydb = mysql.connector.connect(
  host="us-cdbr-east-02.cleardb.com",
  user="b243ca206d55ea",
  password="6f215509",
  database='heroku_47b87531408c5a5'

)
cursor = mydb.cursor()


# функция создает клавиатуру и ее разметку
def get_keyboard():
    cursor = mydb.cursor()
    cursor.execute("SELECT Name FROM  TEACHERS")
    data= (cursor.fetchall())
    cursor.close()
    print(data)
    ls=[]
    for teacher in data:
      ls.append(list(teacher))


    
  

    my_keyboard = ReplyKeyboardMarkup(ls,resize_keyboard=True)  # добавляем кнопки
    return my_keyboard

def get_url(name):
    mydb = mysql.connector.connect(
    host="us-cdbr-east-02.cleardb.com",
    user="b243ca206d55ea",
    password="6f215509",
    database='heroku_47b87531408c5a5'

    )
    cursor = mydb.cursor()
    cursor.execute(f"SELECT URL, conf_id, password  FROM  TEACHERS WHERE Name ='{name}'")
    data= list(cursor.fetchall())
    cursor.close()
    mydb.close()
   
    
    conf=[]
    for col in data[0]:
      if col != None:
        conf.append(col)

    print(conf)
    return conf


    

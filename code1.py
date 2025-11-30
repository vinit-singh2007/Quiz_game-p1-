import mysql.connector
import random 
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="quiz_game"
    )

def save_score_mysql(name,score):
   conn=connect_db()
   cursor=conn.cursor()
   query="insert into scores(name,score)values(%s,%s)"
   values=(name,score)
   cursor.execute(query,values)
   conn.commit()
   conn.close()



while(1):
   score=0
   question=[{
      "question":"what is the capital of israel",
      "options":["1.tel aviv,2.jerusalem,3.palestine,4.none of the above"],
      "answers":"3"
   },
   {
      "question":"what is the capital of india",
      "options":["1.mumbai,2.delhi,3.punjab,4.up"],
      "answers":"2"
   },
    {
      "question":"what is the capital of usa",
      "options":["1.mumbai,2.delhi,3.washington,4.up"],
      "answers":"3"
   },
   {
   "question":"what is the capital of russia",
      "options":["1.mumbai,2.delhi,3.washington,4.moscow"],
      "answers":"4"
   },
   {
     "question":"what is the capital of uk",
      "options":["1.mumbai,2.delhi,3.london,4.up"],
      "answers":"3"
   }
   ]
   ask=(input("Do you want to start with quiz yes/no:"))
   random.shuffle(question)
   if ask=="yes":
    name=input("enter your name:")
    print("welcome to quiz game!!")
    for q in question:
       print(q["question"])
       for opt in q["options"]:
           print(opt)
     
       ans=(input("enter the ans:"))
       if(ans==q["answers"]):
           print()
           print("great!!,you have given right answer")
           score+=1
           print()
       else:
          print("wrong")
    print()
    print("your score is:",score,"/",len(question))

    save_score_mysql(name,score)
   else:
    print("Thank you!!")  
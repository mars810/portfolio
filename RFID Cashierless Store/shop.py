import pymysql
import twilio
from twilio.rest import Client
import time
def rfidLoop(detectedName):
    localtime = time.asctime(time.localtime(time.time()))
    #twilio
    account_sid = '00000000000000000000000'
    auth_token = '00000000000000000000000'
    client = Client(account_sid, auth_token)

    #db connection
    db = pymysql.connect(host='localhost', user ='raspberry', passwd='000000000', db='groceryStore')
    cr=db.cursor()

    #customer ID
    #print ("Please scan your ID")  #facial recognition here
    itemRFID=0
    #
    cr.execute("select ID from customers where name = " + "'" +  detectedName+"'")
    person=cr.fetchone()
    customerID = person[0]

    cr.execute("select transactions from customers where ID = " + str(customerID))
    s=cr.fetchone()
    transactionNum = s[0] + 1
    tableName = str(customerID) +"_"+ str(transactionNum)

    #create table for this transaction
    cr.execute("""create table `%s` (RFID int, name varchar(30), price double)""",[tableName])
    db.commit()
    print ("Welcome " + detectedName +"!")
    print ("This is your " + str(transactionNum) + "th transaction.")

    #shopping loop - executes repeatedly until the customer ID is read which signifies the end of the purchase
    cr.execute("select * from customers where ID = " + str(customerID))
    t=cr.fetchone()
    name = t[1]
    textMessage= "\nThank you for shopping with us " + str(name) +"! \nBelow is the receipt of your purchase on " + str(localtime) + "\n\n"
    purchaseTotal = 0.00
    while True:
        print ("Waiting on item to be scanned...")
        itemRFID =input()
        if itemRFID == str(customerID):
            print ("thank you for shopping!")
            break
        else:
            cr.execute("select RFID, name, price  from groceryItems where RFID= " + str(itemRFID))
            r=cr.fetchone()
            print (str(r[1]) +" " + str(r[2]))
            curRFID = r[0]
            curName = r[1]
            curPrice = r[2]
            textMessage = textMessage + str(curName)  + " $" + str(curPrice) + "\n"
            purchaseTotal += r[2]
            cr.execute("insert into `%s` values (%s, %s, %s) ",(tableName, curRFID, curName, curPrice))

    textMessage = textMessage + "\nTotal cost: $" + str(purchaseTotal)
    #send message to phone
    message = client.messages \
            .create(
                    body=textMessage,
                    from_='+0000000000',
                    to='00000000000'
             )
    #update transaction number in database
    cr.execute("update customers set transactions = %s  where ID = %s",(transactionNum, customerID))
    db.commit()

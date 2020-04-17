import sqlite3
import datetime
import sys





nameOfDatabase = "../Database/search.sqlite"
db = sqlite3.connect(nameOfDatabase)
def create_connection(db_name):
    try:
        con = sqlite3.connect(db_name)
        return con

    except Error as e:
        print(e)

    return None

def create_table():
    db=create_connection(nameOfDatabase).cursor()
    db = sqlite3.connect(nameOfDatabase)
    db.execute("CREATE TABLE IF NOT EXISTS searchResult(id INTEGER PRIMARY KEY AUTOINCREMENT,searchNumber INTEGER , numPlayer INTEGER , searchName TEXT ,mouseStep INTEGER PRIMARYKEY,exploredNodeCount INTEGER, numOfMoves INTEGER,inserted_date TEXT )")
    db.execute("CREATE TABLE IF NOT EXISTS WinScore(id INTEGER PRIMARY KEY AUTOINCREMENT, numPlayer INTEGER , searchName TEXT, inserted_date TEXT )")

    db.commit()
    db.close()



def insertSearchResult(searchNum ,numPlayer , searchName,mouseStep,exploredCount,numMoves):
    db=create_connection(nameOfDatabase).cursor()
    con = sqlite3.connect(nameOfDatabase)
    date = datetime.datetime.today()
    values=(searchNum ,numPlayer , searchName,mouseStep,exploredCount,numMoves, date)
    con.execute('INSERT INTO searchResult(searchNumber,numPlayer, searchName,mouseStep, exploredNodeCount, numOfMoves, inserted_date)VALUES(?,?,?,?,?,?,?)', values)
    con.commit()
    con.close()




def displayTable():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM searchResult")
    for id,searchNum ,numPlayer , searchName,mouseStep,exploredCount,numMoves, date in cursor:
        print(id,searchNum ,numPlayer , searchName,mouseStep,exploredCount,numMoves, date)
    print("-"*20)
    cursor.close()
    cursor.connection.commit()

    db.close()


def averageExploredNode():
    cursor = db.cursor()
    cursor.execute("SELECT searchName , numPlayer, mouseStep,  AVG(exploredNodeCount), COUNT(id) FROM searchResult GROUP BY searchName , numPlayer, mouseStep")
    for searchNum ,numPlayer , mouseStep, avg, numTrails in cursor:
        print("Name: %s  numPlayer:%s mouseStep%s avg%1.2f Trails%s"  % (searchNum ,numPlayer , mouseStep, avg, numTrails))


    cursor.close()
    cursor.connection.commit()

    db.close()


def averageExploredNodeIntoText(numPlayer):
    cursor = db.cursor()
    cursor.execute("SELECT searchName , numPlayer, mouseStep,  AVG(exploredNodeCount), COUNT(id) FROM searchResult GROUP BY searchName , numPlayer, mouseStep")
    orig_stdout = sys.stdout
    f = open('GridSize'+ str(numPlayer)+'ExploredNodes.txt', 'w')
    sys.stdout = f
    for searchNum ,numPlayer , mouseStep, avg, numTrails in cursor:
        print("Name: %s  numPlayer:%s mouseStep%s avg%1.2f Trails%s"  % (searchNum ,numPlayer , mouseStep, avg, numTrails))

    sys.stdout = orig_stdout
    f.close()
    cursor.close()
    cursor.connection.commit()

    db.close()


def averageNumOfMoves():
    cursor = db.cursor()
    cursor.execute("SELECT searchName , numPlayer, mouseStep,  AVG(numOfMoves), COUNT(id) FROM searchResult GROUP BY searchName , numPlayer, mouseStep")
    for searchNum ,numPlayer , mouseStep, avg, numTrails in cursor:
        print("Name: %s  numPlayer:%s mouseStep%s avg%1.2f Trails%s"  % (searchNum ,numPlayer , mouseStep, avg, numTrails))

    cursor.close()
    cursor.connection.commit()

    db.close()
def averageNumOfMovesIntoText(numPlayer):
    cursor = db.cursor()
    cursor.execute("SELECT searchName , numPlayer, mouseStep,  AVG(numOfMoves), COUNT(id) FROM searchResult GROUP BY searchName , numPlayer, mouseStep")
    orig_stdout = sys.stdout
    f = open('GridSize'+ str(numPlayer)+'AverageMoves.txt', 'w')
    sys.stdout = f
    for searchNum ,numPlayer , mouseStep, avg, numTrails in cursor:
        print("Name: %s  numPlayer:%s mouseStep%s avg%1.2f Trails%s"  % (searchNum ,numPlayer , mouseStep, avg, numTrails))


    sys.stdout = orig_stdout
    f.close()
    cursor.close()
    cursor.connection.commit()
    db.close()


def deleteData():
    db=create_connection(nameOfDatabase).cursor()
    con = sqlite3.connect(nameOfDatabase)
    date = datetime.datetime.today()
    con.execute('delete from searchResult')
    con.commit()
    con.close()

create_table()

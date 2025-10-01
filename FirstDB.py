import psycopg2
conn = psycopg2.connect(
    hostaddr="127.0.0.1",  # hard override
    host="localhost",
    port=5432,
    user="accounting",
    password="Frostpin!2",
    dbname="fall2025csci260",
)
with conn, conn.cursor() as cur:
    cur.execute("select 1;")
    print(cur.fetchone())


def showLocations():
    
    print( "     x|      y|      id")
    print("---------------------")
    for row in data:
        for value in row:
            print(value,"|",end="")
            print("|", end = "")
            print("")

def getLocation():
    cursor.execute("Select * from location")
    data = cursor.fecthall()
    print(data)
    return data

def putLocation(values):
    first ="update location set "
    last =f"where id = {d ["id"] }"
    value1 ="" 
    if "x" in d:
        value =f"x={3}"
        value2=""
    if "y" in d:
        value2=f"y={y}"
        if"x" in d and "y" in d:
            value1 = value1+","
        cursor.execute(first+value1+value2+last)

def addLocation():
    x = input("Please enter X")
    y = input("Please enter y")
    cursor.execute(f"insert into location (x,y) values ({x}, {y} )")

def putChange(values):

    def updateLocation():
        # id = input("Enter id you want to update:")
        # x = input('Enter new X:")' \
        # 'y=input("Enter new Y:") ')
        choice =0
        print("0) Cancel")
        print("1) Change X")
        print("2) Change Y")
        print("3) Change Both")
        choice = input("Enter your choice to change a parameter")
        if choice !=0:
            id = input("Enter id you want to update:")
            if choice==1:
                    x=input("Enter new X:")
                    cursor.execute(f"update location set x = (x) where id = (id)")
            if choice==2:
                y=input("Enter new Y:")
                cursor.execute(f"update location set y = (y) where id =(id)")
                if choice ==3:
                    x=input("Enter new X:")
                    y = input("Enter new Y:)")
                if choice ==1: 
                    putchange((id,x))
                if choice ==2:
                    putchange((id,y))
                if choice == 3:
                    putchange((id,x,y))
            

        choice = 1
        while choice!=0:
            print("0) Quit")
            print("1) Show Location")
            print("2 ) Add locstion")
            print("3) Update Locatino U")
            print("4) Delete (to be completed by student)")
            print("5) commit current changes")
            choice = int(input("Enter your choice"))
            if choice == 1:
                showLocations(getLocation())
            if choice==2:
                putLocation(getLocation())
            if choice==3:
                updateLocation()
            if choice ==5:
                connection.commit()
        


            cursor.execute("Select * from common")

    data=cursor.fetchall()

    print(data)


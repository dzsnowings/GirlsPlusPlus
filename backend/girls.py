import sys, csv, pymysql
from pprint import pprint

def connect(args):
    global connection, cursor
    try:
        connection = pymysql.connect(host = 'localhost', user = args[1], password =args[2], db = 'girls', charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        return connection, cursor
    except Exception as e:
        return print(f'The following Exception occured, {e}\n\n{args[1]} could not log into MySQL database')

def csvExtractor(csvFile):
    with open(csvFile) as fin:
        dictreader = csv.DictReader(fin)
        dictList = [dict(row) for row in dictreader]

    members = [(int(i['ID']), i['name'], i['email'], i['major'], i['gender'], i['class'], i['why']) for i in dictList]
    return members

def insert(members):
    query = "insert into members (ID, name, email, major, gender, class, why) values (%s, %s, %s, %s, %s, %s, %s);"
    cursor.executemany(query, members)

    connection.commit()
    connection.close()

def main(args):
    connection, cursor = connect(args)
    members = csvExtractor(args[0])
    insert(members)

if __name__ == "__main__":
    main(sys.argv[1:])
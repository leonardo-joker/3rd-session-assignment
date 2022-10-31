import psycopg2, re


def fibonacci_generator(x):
    sequence = []
    for i in range(x):
        if i == 0:
            sequence.append(0)
        if i == 1:
            sequence.append(1)
        if i > 1:
            a = sequence[i - 2] + sequence[i - 1]
            sequence.append(a)
    return sequence


print(fibonacci_generator(50))

#2
the_names = []
with open("baby2008.html", "r") as h:
    data = h.read()
    x = re.sub(r'<.*?>', ' ', data)
    names = re.compile(r'\s*[1-9]+\s*([A-Z][a-z]+)\s*([A-Z][a-z]+)')
    the_names = names.findall(x)
    baby_names = []
    male_names = []
    female_names = []
    for x in range(len(the_names)):
        if x == 0:
            continue
        else:
            male = the_names[x][0]
            female = the_names[x][1]
            baby_names.append(male)
            baby_names.append(female)
            male_names.append(male)
            female_names.append(female)
    print("")
    print(baby_names)
    print(male_names)
    print(female_names)
print(the_names)
hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'leonardo'
port_id = 5432
try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
    )
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS baby_names')
    create_script = '''CREATE TABLE IF NOT EXISTS baby_names(
                            
                            male    varchar(100) NOT NULL,
                            female  varchar(100) NOT NULL)
    '''
    cur.execute(create_script)

    insert_script = 'INSERT INTO baby_names ( male, female) VALUES ( %s, %s) '
    insert_values = []
    for i in range(len(the_names)):
        if i == 0:
            continue
        else:
            value = (f"{the_names[i][0]}", f"{the_names[i][1]}" )
            insert_values.append(value)
    for data in insert_values:
        cur.execute(insert_script, data)

    conn.commit()

except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()



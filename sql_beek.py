import sqlite3

date_base = 'user_bases.db'

base = sqlite3.connect(date_base,check_same_thread=False)
cursor = base.cursor()

sqlite_create_table = '''CREATE TABLE Users (
                             id INTEGER PRIMARY KEY AUTOINCREMENT,
                             id_telegram int UNIQUE,
                             first_name TEXT,
                             username TEXT,
                             apikey JSONB,
                             last_msg_user int,
                             last_msg_bot int,
                             flag TEXT,
                             apikey_vib TEXT,
                             main_otsh JSONB,
                             today_otsh JSONB,
                             yester_otsh JSONB,
                             today_week_otsh JSONB, 
                             yester_week_otsh JSONB,
                             nev_order INTEGER DEFAULT 1, 
                             nev_order_otk INTEGER DEFAULT 1, 
                             nev_sale INTEGER DEFAULT 1, 
                             nev_sale_otk INTEGER DEFAULT 1,
                             base_nev_messeg_ord TEXT,
                             base_nev_messeg_sale TEXT,
                             base_canal TEXT ,
                             base_ostatki TEXT
                             );
                            '''
try:
    cursor.execute(sqlite_create_table)
    base.commit()
    print("Таблица SQLite создана")
except:
    None

def selekt(id_tg = None):

    arg = dict()

    zapros = f"""SELECT * from Users where id_telegram like {id_tg}"""
    cursor.execute(zapros)

    try:

        records = cursor.fetchall()[0]
        arg['id_telegram'] = records[1]
        arg['first_name'] = records[2]
        arg['username'] = records[3]
        arg['apikey'] = eval(f'{records[4]}')
        arg['last_msg_user'] = records[5]
        arg['last_msg_bot'] = records[6]
        arg['flag'] = records[7]
        arg['apikey_vib'] = eval(f'{records[8]}')
        arg['main_otsh'] = eval(f'{records[9]}')
        arg['today_otsh'] = eval(f'{records[10]}')
        arg['yester_otsh'] = eval(f'{records[11]}')
        arg['today_week_otsh'] = eval(f'{records[12]}')
        arg['yester_week_otsh'] = eval(f'{records[13]}')
        arg['nev_order'] = records[14]
        arg['nev_order_otk'] = records[15]
        arg['nev_sale'] = records[16]
        arg['nev_sale_otk'] = records[17]
        arg['base_nev_messeg_ord'] = eval(records[18])
        arg['base_nev_messeg_sale'] = eval(records[19])
        arg['base_canal'] = eval(records[20])
        arg['base_ostatki'] = eval(records[21])
        arg['status'] = True


    except:
        arg['status'] = False

    return arg

def selekt_all():

    zapros = f"""SELECT * from Users"""
    return cursor.execute(zapros).fetchall()

def add(arg):

    pol = ''
    zash = ''

    for i in arg:
        pol += f',{i}'
        zash += f',"{arg[i]}"'

    pol = pol[1:]
    zash = zash[1:]

    zapros = f"INSERT INTO users ({pol}) VALUES ({zash});"

    cursor.execute(zapros)
    base.commit()


def update(id_tg,arg):

    pol = ''

    for i in arg:

        pol += f',{i} = "{arg[i]}"'

    pol = pol[1:]

    zapros = f"""UPDATE Users SET {pol} WHERE id_telegram = {id_tg};"""

    cursor.execute(zapros)
    base.commit()


if __name__ == '__main__':

    arg = {'id_telegram':2,'first_name':'qweasdzxc','apikey': {"test":"qwe"}}
    #print(selekt(2))
    #update('5294119975',arg)
    print(selekt('5294119975')['main_otsh'])
    base = selekt('5294119975')['base_ostatki']['2023-01-19']['ost']
    for i in base:
        print(i)
    #{'2023-01-19': {


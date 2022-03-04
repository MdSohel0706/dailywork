


from _22_2_DB_String._2_CREATE_mulitple_strs.utils import conn

def save_to_db(i_str, le):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO STRING_DATA VALUES(%s,%s)"
        cursor.execute(query, (i_str, le))
        conn.commit()
    except Exception as e:
        print("Exception details : ", e)
    finally:
        cursor.close()
        conn.close()

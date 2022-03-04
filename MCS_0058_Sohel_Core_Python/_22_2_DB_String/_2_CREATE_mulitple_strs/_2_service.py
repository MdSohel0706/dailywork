
from _22_2_DB_String._2_CREATE_mulitple_strs._3_dao import save_to_db

# Business logic
def get_len(str_val):
    le = 0
    for each in str_val:
        le += 1
    save_to_db(str_val, le)
    return le
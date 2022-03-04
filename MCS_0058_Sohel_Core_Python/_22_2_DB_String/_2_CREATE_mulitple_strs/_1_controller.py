from _22_2_DB_String._2_CREATE_mulitple_strs._2_service import get_len

# Controller
def get_str_len(in_str):
    if in_str == '':
        return "Enter valid string"
    else:
        st_len = get_len(in_str)
        return st_len



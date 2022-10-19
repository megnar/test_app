from .__init__ import file_db
import os

def correctCard(str):
    if len(str) > 20 or len(str) < 16:
        return False
    return str.isdigit()


def getInformation(str):
    newstr = str[:6]
    s = file_db.execute(f"""SELECT * FROM bankInfo
                        WHERE  bin = {newstr}""").fetchall()
    if len(s) != 0:
        return True, s
    else:
        return False, s




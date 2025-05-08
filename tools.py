from database import UserFetchFormat,connect_to_localDB
from typing import Union, Dict
from langchain.agents import tool
@tool
def check_user(phone:str) -> Union[Dict[str, any], str]:
    """ Fetch User info (name,phone,email,address,city,state,zipcode),
     if the phone number given by user exists in the users table in db with the given query.
     Args: phone:str-> Phone number of the user
     """
    cursor, conn = connect_to_localDB('user.db')
    query = """
            SELECT
                name,
                phone,
                email,
                address_line_1,
                address_line_2,
                city,
                state,
                zipcode
            FROM users
            WHERE phone = ?
        """
    cursor.execute(query, (phone,))
    row = cursor.fetchone()
    conn.close()
    if row:
        result=UserFetchFormat(
            name=row[0],
            phone_number = row[1],
            email_id= row[2],
            address= f"{row[3]} {row[4] if row[4] else ''}",
            city= row[5],
            state= row[6],
            pincode= row[7]
        )
        return result.model_dump()
    else:
        return "No User"
    
from database.crud import Session
from database.models_sql import Users
from sqlalchemy.dialects.postgresql import insert


def create_new_user(user_id: int):
    s = Session()
    insert_stmt = insert(Users).values(id=user_id)

    do_nothing_stmt = insert_stmt.on_conflict_do_nothing(index_elements=["id"])
    s.execute(do_nothing_stmt)
    s.commit()
    s.close()

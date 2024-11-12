from app.DAL.base import BaseDAL
from app.users.models import Users

class UsersDAL(BaseDAL):
    model = Users
    
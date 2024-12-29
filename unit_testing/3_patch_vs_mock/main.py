def external_service(user_id):
    USERS_BY_ID = {
        1: {'name': 'Filip', 'age': 35},
        2: {'name': 'John', 'age': 30}
    }
    return USERS_BY_ID.get(user_id, f'User with id {user_id} not found')

def get_user_info(user_id):
    return external_service(user_id)

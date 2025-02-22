from core.domain.entities import UserEntity

# Mock database for storing user registrations
user_storage: set[UserEntity] = set()

class UserRepository:
    """Repository handling user storage"""

    @staticmethod
    def save(user: UserEntity) -> None:
        """Save user in mock storage"""
        if user in user_storage:
            raise ValueError("User already exists.")
        user_storage.add(user)

    @staticmethod
    def get_all_users() -> list[UserEntity]:
        """Retrieve all registered users"""
        return user_storage
    
    @staticmethod
    def get_user(user: UserEntity) -> UserEntity:
        """Returns the user if found, otherwise None"""
        return next((x for x in user_storage if x == user), None)

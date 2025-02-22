from core.domain.entities import UserEntity
from core.infrastructure.repositories import UserRepository

class RegisterUserUseCase:
    """Handles the logic of user registration"""

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, data: UserEntity) -> UserEntity:
        """Validates and registers a user"""
        if not data.accepted_terms:
            raise ValueError("User must accept the terms and conditions to register.")
        self.repository.save(data)
        return data
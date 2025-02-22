import pytest
from core.infrastructure.repositories import UserRepository
from core.domain.entities import UserEntity


@pytest.fixture
def sample_user():
    """Creates a user entity"""
    return UserEntity(
        first_name="Jane",
        last_name="Doe",
        country="UK",
        phone="+449876543210",
        email="jane.doe@example.com",
        experience="Intermediate",
        accepted_terms=True
    )

def test_repository_save_and_get(sample_user):
    """Test if user is saved and retrievable"""
    UserRepository.save(sample_user)
    user = UserRepository.get_user(sample_user)
    assert sample_user == user


def test_repository_get_user_not_found(sample_user):
    sample_user.email = "nonexistent@example.com"
    """Ensure repository returns None when user is not found"""
    user = UserRepository.get_user(sample_user)
    assert user == None

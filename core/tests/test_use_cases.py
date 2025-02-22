import pytest
from core.application.register_user import RegisterUserUseCase
from core.infrastructure.repositories import UserRepository, user_storage
from core.domain.entities import UserEntity


@pytest.fixture(autouse=True)
def reset_repository():
    """Clear user storage before each test"""
    global user_storage
    user_storage.clear()

@pytest.fixture
def test_user_data():
    return UserEntity.from_dict({
        "first_name": "John",
        "last_name": "Doe",
        "country": "USA",
        "phone": "+1234567890",
        "email": "john.doe@example.com",
        "experience": "Beginner",
        "accepted_terms": True
    })

@pytest.fixture
def use_case():
    return RegisterUserUseCase(UserRepository())

def test_register_user_success(use_case, test_user_data):
    user = use_case.execute(test_user_data)
    assert user.first_name == test_user_data.first_name
    assert user.email == test_user_data.email

def test_register_user_repository(use_case, test_user_data):
    user = use_case.execute(test_user_data)
    user = UserRepository.get_user(user=test_user_data)
    assert user == test_user_data
    print(test_user_data, user)


def test_register_user_duplicate(use_case, test_user_data):
    user = use_case.execute(test_user_data)
    """Ensure that duplicate registration is prevented"""
    with pytest.raises(ValueError, match="User already exists."):
        use_case.execute(test_user_data)  # Registering the same user again should fail

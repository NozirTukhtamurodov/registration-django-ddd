from dataclasses import dataclass

@dataclass
class UserEntity:
    first_name: str
    last_name: str
    country: str
    phone: str
    email: str
    experience: str
    accepted_terms: bool

    @classmethod
    def from_dict(cls, data: dict) -> "UserEntity":
        """Creates a UserEntity instance from a dictionary."""
        return cls(**data)


    def __hash__(self):
        return hash(self.phone)

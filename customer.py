from pydantic import BaseModel

class Customer(BaseModel):
    CustomerId: str
    Name: str

    
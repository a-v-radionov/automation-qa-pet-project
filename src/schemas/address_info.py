from pydantic import BaseModel


class Address(BaseModel):
    address: str
    received: int
    sent: int
    balance: int
    tx_count: int
    unconfirmed_tx_count: int
    unconfirmed_received: int
    unconfirmed_sent: int
    unspent_tx_count: int
    first_tx: str = ''
    last_tx: str = ''

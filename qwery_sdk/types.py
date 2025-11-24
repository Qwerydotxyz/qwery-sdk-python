"""Type definitions for Qwery SDK."""
from enum import Enum
from typing import Optional, Dict
from pydantic import BaseModel

class Network(str, Enum):
    MAINNET = "solana"
    DEVNET = "solana-devnet"

class PaymentRequest(BaseModel):
    amount: float
    token: str
    recipient: str
    metadata: Optional[Dict[str, str]] = None

class PaymentResponse(BaseModel):
    payment_id: str
    transaction: str
    amount: float
    token: str
    recipient: str
    network: str
    status: str
    expires_at: Optional[str] = None

class SettleResponse(BaseModel):
    success: bool
    signature: Optional[str] = None
    status: str
    error: Optional[str] = None

class VerifyResponse(BaseModel):
    verified: bool
    status: str
    confirmations: Optional[int] = None

class HealthResponse(BaseModel):
    status: str
    version: str
    networks: Dict[str, str]

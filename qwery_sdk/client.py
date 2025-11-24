"""Qwery API client."""
from typing import Optional, Dict
import httpx
from .types import Network, PaymentResponse, SettleResponse, VerifyResponse, HealthResponse
from .errors import QweryAPIError

class QweryClient:
    """Client for Qwery x402 Payment Facilitator API."""
    
    DEFAULT_URL = "https://facilitator.qwery.xyz"
    
    def __init__(self, network: Network = Network.MAINNET, facilitator_url: Optional[str] = None, api_key: Optional[str] = None, timeout: float = 30.0):
        self.network = network
        self.facilitator_url = facilitator_url or self.DEFAULT_URL
        self.api_key = api_key
        self.timeout = timeout
        self._client = httpx.AsyncClient(timeout=timeout)
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
    
    async def close(self):
        await self._client.aclose()
    
    def _headers(self) -> Dict[str, str]:
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers
    
    async def create_payment(self, amount: float, token: str, recipient: str, metadata: Optional[Dict[str, str]] = None) -> PaymentResponse:
        """Create a new payment request."""
        payload = {"amount": amount, "token": token, "recipient": recipient, "network": self.network.value}
        if metadata:
            payload["metadata"] = metadata
        
        response = await self._client.post(f"{self.facilitator_url}/payments/create", json=payload, headers=self._headers())
        if response.status_code != 200:
            raise QweryAPIError(f"Failed to create payment: {response.text}", response.status_code)
        return PaymentResponse(**response.json())
    
    async def settle_payment(self, payment_id: str, signed_transaction: str) -> SettleResponse:
        """Settle a payment with signed transaction."""
        response = await self._client.post(f"{self.facilitator_url}/payments/settle", json={"payment_id": payment_id, "signed_transaction": signed_transaction}, headers=self._headers())
        if response.status_code != 200:
            raise QweryAPIError(f"Failed to settle: {response.text}", response.status_code)
        return SettleResponse(**response.json())
    
    async def verify_payment(self, signature: str) -> VerifyResponse:
        """Verify a payment by signature."""
        response = await self._client.post(f"{self.facilitator_url}/payments/verify", json={"signature": signature, "network": self.network.value}, headers=self._headers())
        if response.status_code != 200:
            raise QweryAPIError(f"Failed to verify: {response.text}", response.status_code)
        return VerifyResponse(**response.json())
    
    async def health(self) -> HealthResponse:
        """Check facilitator health."""
        response = await self._client.get(f"{self.facilitator_url}/health")
        if response.status_code != 200:
            raise QweryAPIError(f"Health check failed: {response.text}", response.status_code)
        return HealthResponse(**response.json())

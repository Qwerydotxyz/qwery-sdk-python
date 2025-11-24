# Qwery SDK for Python

Python SDK for integrating Qwery x402 Payment Facilitator into your applications.

[![PyPI version](https://badge.fury.io/py/qwery-sdk.svg)](https://pypi.org/project/qwery-sdk/)
[![Python](https://img.shields.io/pypi/pyversions/qwery-sdk.svg)](https://pypi.org/project/qwery-sdk/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Installation
```bash
pip install qwery-sdk
```

## Quick Start
```python
import asyncio
from qwery_sdk import QweryClient, Network

async def main():
    async with QweryClient(network=Network.MAINNET) as client:
        payment = await client.create_payment(
            amount=0.01,
            token="SOL",
            recipient="merchant_wallet_address"
        )
        print(f"Payment ID: {payment.payment_id}")

asyncio.run(main())
```

## Features

- **Zero User Fees** - Facilitator pays network costs
- **Instant Settlement** - Sub-2 second finality
- **Multi-Token Support** - SOL, USDC, USDT
- **Async/Await** - Built for asyncio
- **Type Hints** - Full type annotations

## Documentation

- **API Docs**: https://docs.qwery.xyz
- **Website**: https://qwery.xyz

## License

MIT © Qwery

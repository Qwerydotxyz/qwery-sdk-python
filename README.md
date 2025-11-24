<div align="center">
  <img src="https://res.cloudinary.com/dkfwg4ta8/image/upload/v1763973825/pysdk402_f5exsu.png" alt="Qwery Python SDK" width="100%" />
</div>

# Qwery SDK for Python

Python SDK for integrating Qwery x402 Payment Facilitator into your applications.

[![PyPI version](https://img.shields.io/pypi/v/qwery-sdk)](https://pypi.org/project/qwery-sdk/)
[![Python](https://img.shields.io/pypi/pyversions/qwery-sdk)](https://pypi.org/project/qwery-sdk/)
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
- **Facilitator API**: https://facilitator.qwery.xyz/docs
- **Website**: https://qwery.xyz

## License

MIT © Qwery

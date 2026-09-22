# py_logger

Project used in my personal projects to personalise debugging messages.

## Installation

```bash
pip install git+https://github.com/Kaua-Matheus/py_logger.git
```

## Use

```python
from logger.logger import Logger

logger = Logger()

logger.log("Server initialized successfully", level="ok")
logger.log("Config not found, using default", level="warn")
logger.log("Fail trying to connect to database", level="err")
logger.log("Requisition received", level="info", detail=True)
```
# lynette-utils

A modular Python toolkit for reusable, audit-ready scripting across ETL workflows, configuration management, and process automation. Designed for clarity, traceability, and consistent logging practices.

## 📦 Modules

### 'logger'
Provides a configurable logger with rotating file handler and optional console output.

- Supports structured logging for ETL pipelines and automation scripts
- Enables audit trails with timestamped entries and log level control
- Easily integrated across projects with minimal setup

### 'log_decorator'
Function-level logging decorator for execution tracing and exception handling.

- Logs function entry, exit, and optional runtime duration
- Captures exceptions with full traceback for debugging
- Produces readable, structured error messages for maintainability

### 'config' *(planned)*
Future module for loading and validating configuration files with schema support.

## 🧪 Example Usage

```python
from logger.logger import setup_logger
from logger.log_decorator import log_function

logger = setup_logger(name="etl_step", log_file="etl_pipeline.log", to_console=True)

@log_function(logger, include_runtime=True)
def extract_data():
    time.sleep(2)
    return "Data extracted"

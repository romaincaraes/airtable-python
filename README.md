# Airtable API with Python

A Python library for the Airtable API.

## Getting Started

### Installation

Install with pip directly from the GitHub repository :

    pip install git+https://github.com/romaincaraes/airtable-python.git

## Usage

### Authentication

Visit the [Standard API Documentation website](https://airtable.com/api) to get your API credentials (API key, base code and table name).

```python
import airtable

parameters = {
    "api_key" : "API_KEY",
    "base" : "BASE_CODE"
}

table = airtable.API(parameters, "TABLE_NAME")
```

### Get data

```python
# Get a list of fields in a table
fields = table.get_fields()
print(fields)

# Get a list of all records in a table
records = table.get_records()
print(records)

# Get an existing record in a table
record = table.get_record("RECORD_ID")
print(record)
```

### Create records

```python
# Create new records in table
status = table.create_records(records)
print(status)
```

### Update records

```python
# Update records in table
status = table.update_records(records)
print(status)
```

### Delete records

```python
# Delete records in table
status = table.delete_records(records)
print(status)
```

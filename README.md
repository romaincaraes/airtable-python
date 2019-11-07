# Airtable API with Python

A Python library for accessing the Airtable API.

## Getting Started

### Authentication

Visit the [Standard API Documentation website](https://airtable.com/api) to get your API credentials (API key, base code and table name).

    import airtable

    parameters = {
        "api_key" : "API_KEY",
        "base" : "BASE_CODE",
        "table" : "TABLE_NAME"
    }

    table = airtable.API(parameters)

### Get a list of fields in a table

    fields = table.get_fields()
    print(fields)

### Get a list of all records in a table

    records = table.get_records()
    print(records)

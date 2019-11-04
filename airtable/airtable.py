#!/usr/bin/env python
#coding: utf-8

import requests

class Airtable() :
    def __init__(self, parameters) :
        self.parameters = parameters

def main() :
    parameters = {
        "api_key" : "API_KEY",
        "base" : "BASE_CODE",
        "table" : "TABLE_NAME"
    }
    table = Airtable(parameters)
    records = table.get_records()
    print(records)


if __name__ == "__main__":
    main()

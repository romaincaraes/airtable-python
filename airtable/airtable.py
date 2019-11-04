#!/usr/bin/env python
#coding: utf-8

import requests

class Airtable() :
    def __init__(self, parameters) :
        self.parameters = parameters

    def auth(self) :
        url = [
            "https://api.airtable.com/v0",
            self.parameters["base"],
            self.parameters["table"].replace(" ", "%20")
            ]
        api_key = self.parameters["api_key"]
        url = "/".join(url) + "?api_key=" + api_key
        return url

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

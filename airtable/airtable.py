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

    def get_fields(self) :
        # Get a list of fields labels in table
        fields = []
        try :
            r = requests.get(self.auth()).json()
            for field in r["records"][0]["fields"] :
                fields.append(field.encode('utf-8'))
        except KeyError as e :
            print(e)
        return fields

    def get_records(self) :
        # Get table records
        records = []
        r = requests.get(self.auth()).json()
        for record in r["records"] :
            records.append(record)
        while ("offset" in r) :
            params = {
                "offset" : r["offset"]
            }
            r = requests.get(self.auth(), params=params).json()
            for record in r["records"] :
                records.append(record)
        return records

    def get_record(self, id) :
        # Get a specific record in table
        record = []
        id = "/" + id
        self.parameters["table"] += id
        try :
            record = requests.get(self.auth()).json()
        except KeyError as e :
            print(e)
        self.parameters["table"] = self.parameters["table"].replace(id, "")
        return record

    def create_records(self, records) :
        # Create new records in table
        data = {"records" : []}
        try :
            rng = [0,10]
            for i in range(0, len(records)/10 + 1) :
                data["records"] = records[rng[0]:rng[1]]
                rng = [x + 10 for x in rng]
                r = requests.post(self.auth(), json=data)
        except KeyError as e :
            print(e)
        return r

    def update_records(self) :
        # Update records in table
        return

    def delete_records(self) :
        # Delete records in table
        return

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

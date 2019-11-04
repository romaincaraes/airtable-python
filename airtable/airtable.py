#!/usr/bin/env python
#coding: utf-8

import requests

def auth(parameters) :
    # Authenticate to a table in a base
    url = [
        "https://api.airtable.com/v0",
        parameters["base"],
        parameters["table"].replace(" ", "%20")
        ]
    api_key = parameters["api_key"]
    url = "/".join(url) + "?api_key=" + api_key
    return url

def main() :
    parameters = {
        "api_key" : "API_KEY",
        "base" : "BASE_CODE",
        "table" : "TABLE NAME"
    }
    api = auth(parameters)


if __name__ == "__main__":
    main()

from django.shortcuts import render
from .models import CountryModel
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

# Create your views here.

# Creating an API that returns countryList

class CountryAll(APIView):
    def get(self, request, format=None):
        countries = {}
        cont = {}
        finalRes = {}
        conRes = {}
        finals = {}


        try:
            req = requests.get("https://countriesnow.space/api/v0.1/countries")
            req_continent = requests.get("https://restcountries.com/v3.1/all")
            
            # getting the countries and continent
            res_countries = req.json() #Countries and Cities
            res_continent = req_continent.json() #Countries and continents
            
            if res_countries["error"] != True:
                countries = res_countries["data"]
                cont = res_continent
                print(len(countries))
                # Looping through the countries to merge with continent
                for i in range(len(countries)):
                    finalRes[i] = countries[i]["country"]

                    # print(countries[i]["country"])
                    for j in range(len(res_continent)):
                        # print(res_continent[j]["name"]["common"])
                    #     conRes[j] = cont[j]["name"]["common"]
                        if res_continent[j]["name"]["common"].lower() == countries[i]["country"].lower():
                            print("ok")
                            finals = {
                                "continent": res_continent[j]["continents"],
                                "country": countries["data"][i]["country"],
                                "cities": countries["data"][i]["cities"]
                            }
                            # return Response({"finals":finals,"cont":cont[0]["continents"], "status":200})
        except Exception as e:
            countries = {"status":f"{e}"}


        return Response({"final":finals,"cont":cont[0]["continents"], "status":200})
        # return Response({"final":finalRes,"data":countries["data"][0]["country"],"cont":cont[0]["continents"], "status":200})
        # return Response({"cont":cont[0]["continents"], "status":200})


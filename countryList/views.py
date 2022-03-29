from typing import final
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
        countries = {} #capture countries
        cont = {} #capture continents
        finals = {} #first level results
        result = [] #results


        try:
            req = requests.get("https://countriesnow.space/api/v0.1/countries")
            req_continent = requests.get("https://restcountries.com/v3.1/all")
            lat_long = requests.get("https://countriesnow.space/api/v0.1/countries/positions")
            
            # getting the countries and continent
            res_countries = req.json() #Countries and Cities
            res_continent = req_continent.json() #Countries and continents
            lat_long = lat_long.json() # Returns countries and latitude/longitude details
            count_id = 0

            
            if res_countries["error"] != True:
                countries = res_countries["data"]
                cont = res_continent
                print(len(countries))
                # Looping through the countries to merge with continent
                for i in range(len(countries)):
                    # print(countries[i]["country"], count_id)
                    for j in range(len(res_continent)):
                        if cont[j]["name"]["common"].lower() == countries[i]["country"].lower():
                            for k in range(len(lat_long["data"])):
                                if countries[i]["country"] == lat_long["data"][k]["name"]:

                                    # print(cont[j]["name"]["common"].lower(), "  ", countries[i]["country"].lower(), " ",  cont[j]["continents"])
                                    count_id+=1


                                    loca_continent = {} 
                                    # loca_continent[cont[j]["continents"]] = 
                                    finals = {
                                        "id": f"{count_id}",
                                        "continent": " ".join(cont[j]["continents"]),
                                        "country": countries[i]["country"],
                                        "cities": countries[i]["cities"],
                                        "long": lat_long["data"][k]["long"],
                                        "lat": lat_long["data"][k]["lat"]
                                    }
                                    result.append(finals)

        except Exception as e:
            result = {"status":f"{e}"}
            return Response({"res":result, "status":status.HTTP_502_BAD_GATEWAY})

        
        return Response({"res":result, "status":status.HTTP_200_OK})
        # return Response({"final":finalRes,"data":countries["data"][0]["country"],"cont":cont[0]["continents"], "status":200})
        # return Response({"cont":cont[0]["continents"], "status":200})


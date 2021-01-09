from django.shortcuts import render
import pickle
# Create your views here.
with open('vehicle_price_model.pickle', 'rb') as handle:
    vehicle_price_model = pickle.load(handle)


def price_suggestion(price_model, makemodel,year,milage):
    coefficients = price_model[makemodel]
    return((year-2000)*coefficients[0] + milage*coefficients[1]+coefficients[2])

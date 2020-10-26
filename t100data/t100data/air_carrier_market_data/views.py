# views
import pdb
from django.views.generic import ListView
from django.db.models import Max, Sum

from . models import MarketData

class MarketDataList(ListView):
    model = MarketData

# The top 5 airports in terms of: Total passengers by origin
class Top5AirportsPaxByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_pax=Sum('passengers')) \
                        .order_by('-total_pax')[0:5]
    template_name="rankorder_list_origin.html"

# The top 5 airports in terms of: Total freight by origin
class Top5AirportsFrxByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_frx=Sum('freight')) \
                        .order_by('-total_frx')[0:5]
    template_name="rankorder_list_origin_frx.html"

# The top 5 airports in terms of: Total freight by destination	
class Top5AirportsFrxByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_frx=Sum('freight')) \
                                 .order_by('-total_frx')[0:5]
    template_name="rankorder_list_destination_frx.html"

	
# The top 5 airports in terms of: Total passengers by destination
class Top5AirportsPaxByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_pax=Sum('passengers')) \
                                 .order_by('-total_pax')[0:5]
    template_name="rankorder_list_destination.html"

# The top 5 airports in terms of: Total Mail by destination
class Top5AirportsMaxByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_max=Sum('mail')) \
                                 .order_by('-total_max')[0:5]
    template_name="rankorder_list_destination_max.html"

# the top 5 airports in terms of: Total Mail by Origin
class Top5AirportsMaxByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_max=Sum('mail')) \
                        .order_by('-total_max')[0:5]
    template_name="rankorder_list_origin_max.html"
	
# The top 5 airports in terms of: Total Distance by destination
class Top5AirportsDaxByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_dax=Sum('distance')) \
                        .order_by('-total_dax')[0:5]
    template_name="rankorder_list_origin_dax.html"

# the top 5 airports in terms of: Total Mail by destination
class Top5AirportsDaxByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_dax=Sum('distance')) \
                                 .order_by('-total_dax')[0:5]
    template_name="rankorder_list_destination_dax.html"

# This airport reported the longest distance by month?
class TopDistanceByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_distance_month.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_distance=Max('distance')) \
                .order_by('-total_distance')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

# airport that reported the most passengers by month

class TopPassengersByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_passengers_month.html"

    def get_queryset(self):

        month_list2 = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_passengers=Max('passengers')) \
                .order_by('-total_passengers')[0:1]
            
         # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list2
		
# This airline reported the most freight by month

class TopFreight(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_freight.html"

    def get_queryset(self):

        month_list3 = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name') \
                .annotate(total_freight=Max('freight')) \
                .order_by('-total_freight')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list3	

# Airline that reported the most passengers

class TopPassengers(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_passengers.html"

    def get_queryset(self):

        month_list4 = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name') \
                .annotate(total_passengerstotal=Max('passengers')) \
                .order_by('-total_passengerstotal')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list4

# This airkine reported the most mail

class TopMail(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_mail.html"

    def get_queryset(self):

        month_list5 = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name') \
                .annotate(total_mailtotal=Max('mail')) \
                .order_by('-total_mailstotal')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list5		
		
# This airline reported the longest flight

class TopDistance(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_distance.html"

    def get_queryset(self):

        month_list6 = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name') \
                .annotate(total_distancetotal=Max('distance')) \
                .order_by('-total_distancetotal')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list6

#Rank order passengers carried, by month, for these airlines	

class TopPassengersSpecificAirlines(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_passengersspecificairlines.html"

    def get_queryset(self):

        month_list7 = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name') \
                .annotate(total_passengersspecificairlines=Max('passengers')) \
				airport_list.filter(carrier_name='American Airlines',carrier_name='Alaska Airlines',carrier_name='Delta Airlines',carrier_name='United Airlines',carrier_name='Southwest Airlines')
                .order_by('-total_passengersspecificairlines')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list7
		
#Find the average number of passengers for flights into:

class AvgPassengersSpecificAirlines(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_avgpassengersspecificairlines.html"

    def get_queryset(self):

        month_list8 = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name') \
                .annotate(total_avgpassengersspecificairlines=avg('passengers')) \
				airport_list.filter(dest_city_name='Los Angeles',dest_city_name='San Francisco',dest_city_name='Dallas-Fort Worth',dest_city_name='Atlanta',dest_city_name='Chicago')
                .order_by('-total_avgpassengersspecificairlines')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list8
		
#Find the average volume of freight for flights from:

class AvgFreightFrom(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_avgfreightfrom.html"

    def get_queryset(self):

        month_list9 = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name') \
                .annotate(total_avgfreightsfrom=avg('freight')) \
				airport_list.filter(dest_city_name='Miami',dest_city_name='Memphis',dest_city_name='New York JFK',dest_city_name='Anchorage',dest_city_name='Louisville')
                .order_by('-total_avgfreightsfrom')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list9
		
# This city pairs represent the most freight carried for the longest distance

class CityPairFromLongest(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_citypairfromlongest.html"

    def get_queryset(self):

        month_list10 = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name') \
                .annotate(total_longestfreightsfrom=max('freight'))
                .order_by('-total_longestfreightsfrom')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list10
		
# This city pairs represent the most mail carried for the shortest distance

class CityPairFromShortest(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_citypairfromshortest.html"

    def get_queryset(self):

        month_list11 = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name') \
                .annotate(total_shortestmailfrom=min('mail'))
                .order_by('-total_shortestmailfrom')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list11
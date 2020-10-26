#urls.py
from django.urls import path
from.views import MarketDataList, \
                    Top5AirportsPaxByOrigin, \
                    Top5AirportsPaxByDestination, \
                    TopDistanceByMonth, \
					Top5AirportsFrxByOrigin, \
					Top5AirportsFrxByDestination, \
					Top5AirportsMaxByDestination, \
					Top5AirportsMaxByOrigin, \
					Top5AirportsDaxByDestination, \
					Top5AirportsDaxByOrigin, \
					TopPassengersByMonth, \
					TopFreight, \
					TopPassengers, \
					TopMail, \
					TopDistance, \
					TopPassengersSpecificAirlines, \
					AvgPassengersSpecificdestinations, \
					AvgFreightFrom, \
					CityPairFromLongest, \
					CityPairFromShortest


urlpatterns = [
    path('list/', MarketDataList.as_view(), name="list"),
    path('top5paxorigin/', 
        Top5AirportsPaxByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Origin Airport"}
        ),
        name="top5paxorigin"),
    path('top5paxdestination/',  
        Top5AirportsPaxByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Destination Airport"}
        ), 
        name="top5paxdestination"),
	path('top5frxdestination/',  
        Top5AirportsFrxByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Freight by Destination Airport"}
        ), 
        name="top5frxdestination"),
	path('top5frxorigin/',  
        Top5AirportsFrxByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Freight by Origin Airport"}
        ), 
        name="top5frxorigin"),
	path('top5maxorigin/',  
        Top5AirportsMaxByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Mail by Origin Airport"}
        ), 
        name="top5maxorigin"),
	path('top5maxdestination/',  
        Top5AirportsMaxByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Mail by Destination Airport"}
        ), 
        name="top5maxdestination"),
	path('top5daxorigin/', 
        Top5AirportsDaxByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Distance by Origin Airport"}
        ),
        name="top5daxorigin"),
	path('top5daxdestination/',  
        Top5AirportsDaxByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Distance by Destination Airport"}
        ), 
        name="top5daxdestination"),
    path('topdistance_month/',  
        TopDistanceByMonth.as_view(
            extra_context={'title': "Top Distance by Month"}
        ), 
        name="topdistance_month"),
	path('toppassengers_month/',  
        TopPassengersByMonth.as_view(
            extra_context={'title': "Top Passengers by Month"}
        ), 
        name="toppassengers_month"),
	path('topfreight/',  
        TopFreight.as_view(
            extra_context={'title': "Top Freight"}
        ), 
        name="topfreight"),
	path('toppassengers/',  
        TopPassengers.as_view(
            extra_context={'title': "Top Passengers"}
        ), 
        name="toppassengers"),		
	path('topmail/',  
        TopMail.as_view(
            extra_context={'title': "Top Mail"}
        ), 
        name="topmail"),
	path('topdistance/',  
        TopDistance.as_view(
            extra_context={'title': "Top Distance"}
        ), 
        name="topdistance"),
	path('toppassengersspecificairlines/',  
        TopPassengersSpecificAirlines.as_view(
            extra_context={'title': "Top Passengers Specific Airlines"}
        ), 
        name="toppassengersspecificairlines"),
	path('avgpassengersspecificdestinations/',  
        AvgPassengersSpecificdestinations.as_view(
            extra_context={'title': "Avg Passengers Specific Destinations"}
        ), 
        name="avgpassengersspecificdestinations"),
	path('citypairfromlongest/',  
        CityPairFromLongest.as_view(
            extra_context={'title': "Max Freight From Location"}
        ), 
        name="citypairfromlongest"),
	path('citypairfromshortest/',  
        CityPairFromShortest.as_view(
            extra_context={'title': "Min Mail From Location"}
        ), 
        name="citypairfromshortest"),
	
]
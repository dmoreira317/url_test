from django.shortcuts import render

# Create your views here.
import requests
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from timeit import default_timer as timer

class MeasureResponseViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['GET'])
    def measure_response(self, request):
        """
        Measure the response time and status code of a specified domain or IP.
        Valid syntax: http://your_domain/api/measure/?dominio=www.transparentcdn.com
        or http://your_domain/api/measure/?ip=8.8.8.8

        Parameters:
        - dominio (str, optional): The domain to measure the response time for.
        - ip (str, optional): The IP address to make the request to instead of resolving the domain.

        Returns:
        A JSON response containing the measured response time (in milliseconds) and the status code.

        Example response:
        {
            "status": 301,
            "time": "150ms"
        }
        """
        try:
            domain = request.GET.get('dominio')
            ip = request.GET.get('ip')

            url = f"https://{ip}/" if ip else f"http://{domain}/"

            if not domain and not ip:
                raise ValueError("url not valid or empty.")

            start_time = timer()
            response = requests.get(url)
            end_time = timer()

            response_time = round((end_time - start_time) * 1000)

            data = {
                'status': response.status_code,
                'time': f"{response_time}ms"
            }
            return Response(data)
        except Exception as e:
            return Response({
                "error": "No url could be retrieved, please send a valid one with this format: 'http://localhost:8000/api/measure/?dominio=www.transparentcdn.com'",
                "detail": str(e),
            })

from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.views import APIView
from .models import CountryModel
from .serializers import CountrySerializer

class CoutryCreateListView(APIView):
    def get(self, *args, **kwargs):
        gs = CountryModel.objects.all()
        serializers = CountrySerializer(gs, many=True)
        return Response(serializers.data)

    def post(self, *args, **kwargs):
        body = self.request.data
        serializer = CountrySerializer(data=body)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)



class RetriaveDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            data = CountryModel.objects.get(pk = pk)
        except Exception as e:
            return Response('not found!')
        serializer = CountrySerializer(data)
        return Response(serializer.data)


    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            data = CountryModel.objects.get(pk=pk)
        except Exception as e:
            return Response('not found')
        data.delete()
        return Response('delete')

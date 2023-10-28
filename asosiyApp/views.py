from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


from .models import *
from .serializer import *

class QoshiqchilarApi(APIView):
    def get(self, request):
        qoshiqchilar = Qoshiqchi.objects.all()
        serializer = QoshiqchiSerializer(qoshiqchilar, many=True)
        return Response(serializer.data)

    def post(self, request):
        qoshiqchi = request.data
        serializer = QoshiqchiSerializer(data=qoshiqchi)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QoshiqchiApi(APIView):
    def get(self, request, pk):
        qoshiqchi = Qoshiqchi.objects.get(id=pk)
        serializer = QoshiqchiSerializer(qoshiqchi)
        return Response(serializer.data)

    def put(self, request, pk):
        yangi = request.data
        eski = Qoshiqchi.objects.get(id=pk)
        serializer = QoshiqchiSerializer(eski, data=yangi)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbomlarApi(APIView):
    def get(self, request):
        albomlar = Albom.objects.all()
        serializer = AlbomSerializer(albomlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        albom = request.data
        serializer = AlbomSerializer(data=albom)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class AlbomApi(APIView):
    def get(self, request, pk):
        albom = Albom.objects.get(id=pk)
        serializer = AlbomSerializer(albom)
        return Response(serializer.data)

    def put(self, request, pk):
        yangi = request.data
        eski = Albom.objects.get(id=pk)
        serializer = AlbomSerializer(eski, data=yangi)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        albom = Albom.objects.get(id=pk)
        albom.delete()
        return Response({"success": "true"})


class QoshiqlarApi(APIView):
    def get(self, request):
        qoshiqlar = Qoshiq.objects.all()
        serializer = QoshiqSerializer(qoshiqlar, many=True)
        return Response(serializer.data)
    def post(self, request):
        qoshiq = request.data
        serializer = QoshiqSerializer(data=qoshiq)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


#---------------------------------------ModelViewSets---------------------------------------------


#IZOH MODEL VIEWSET ---------------------------------------
class IzohModelViewSet(ModelViewSet):
    queryset = Izoh.objects.all()
    serializer_class = IzohSerializer


#ALBOM MODEL VIEWSET-----------------------------------------
class AlbomModelViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer

    @action(detail=True,  methods=["GET", "POST"])
    def comments(self, request, pk):
        albom = self.get_object()
        if request.method == "POST":
            comment = request.data
            serializer = IzohSerializer(data=comment)
            if serializer.is_valid():
                serializer.save(
                    albom=albom
                )
                return Response(serializer.data)
            return Response(serializer.errors)
        izohlar = Izoh.objects.filter(albom=albom)
        serializer = IzohSerializer(izohlar, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def musics(self, request, pk):
        albom = self.get_object()
        qoshiq = Qoshiq.objects.filter(albom=albom)
        serializer = QoshiqSerializer(qoshiq, many=True)
        return Response(serializer.data)



#QO'SHIQ MODEL VIEWSET-----------------------------------------------
class QoshiqModelViewSet(ModelViewSet):
    queryset = Qoshiq.objects.all()
    serializer_class = QoshiqSerializer


#QO'SHIQCHILAR MODEL VIEWSET-------------------------------------------
class QoshiqchilarModelViewSet(ModelViewSet):
    queryset = Qoshiqchi.objects.all()
    serializer_class = QoshiqchiSerializer

    @action(detail=True, methods=["GET", "POST"])
    def albums(self, request, pk):
        qoshiqchi = self.get_object()
        print(f'Albom topildi {qoshiqchi}')
        albom = Albom.objects.filter(qoshiqchi=qoshiqchi)
        serializer = AlbomSerializer(albom, many=True)
        return Response(serializer.data)


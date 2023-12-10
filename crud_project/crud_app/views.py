from .models import Candidatedirectory
from .serializers import  CandidatedirectorySerializer,Candidatedirectory_serial
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class CRUD():
    @api_view(['POST'])
    def create_candidate(request):
        try:
            serializer=Candidatedirectory_serial(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"msg":"successfully created","status":status.HTTP_201_CREATED})
            
            return Response({"msg":"failed to create", "status":status.HTTP_400_BAD_REQUEST})
        except Exception as e:
            return Response({"error":"error : {}".format(e)})

    @api_view(['GET'])
    def get_candidate(self,id):
        try:
            if id==0:
                mydata = Candidatedirectory.objects.all().order_by('-id')
                serializer=CandidatedirectorySerializer(mydata,many=True)
                
                return Response({'status':'true','code':200,"data":serializer.data})

            else:
                mydata=Candidatedirectory.objects.get(id=id)
                serial=CandidatedirectorySerializer(mydata)
                data={"result":serial.data}
                return Response({'status':'true','code':200,"data":data})
        except Exception as e:
            return Response({'status':'false','code':400,"msg":"id exists"})

    @api_view(['POST'])
    def update_candidate(request,id):
        try:
            data=request.data
            mydata=Candidatedirectory.objects.get(id=id)
            if mydata:
                serial=Candidatedirectory_serial(mydata,data=data)
                if serial.is_valid(raise_exception=True):
                    serial.save()
                    return Response({"msg":"successfully updated","status":status.HTTP_201_CREATED})
                return Response({"msg":"failed to update", "status":status.HTTP_400_BAD_REQUEST})
        except Exception as e:
            return Response({"error":"error : {}".format(e)})
    
    @api_view(['DELETE'])
    def delete_candidate(request,id):
        try:
            if id:
                mydata=Candidatedirectory.objects.get(id=id)
                mydata.delete()
                return Response({'status':'true','code':200})
        except Exception as e:
            return Response({"error":"error : {}".format(e)})

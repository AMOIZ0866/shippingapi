import random
from django.db.models import Q
from rest_framework import status, views
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import User, PhoneOTP, Dispatches, Pickups, Deliveries
from api.serializers import CreateUserSerializer, DispatchSerializer, DeliveriesSerializer, PickupSerializer, \
    SimpleDispatchSerializer


class RegisterUser(APIView):
    # post request to register the new user
    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone')
        serializers = CreateUserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            # otp verification of the user
            otp = send_otp(phone)
            PhoneOTP.objects.create(
                phone=phone,
                otp=otp,
            )
            print(otp)
            return Response({
                "data": serializers.data,
                "status": status.HTTP_201_CREATED,
                'detail': 'OTP has been sent to the Phone Number'})
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


def send_otp(phone):
    return str(random.randint(00000, 11111))


class ValidateOTP(APIView):
    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone', False)
        otp_sent = request.data.get('otp', False)
        # verify the presence of phone and otp
        if phone and otp_sent:
            # verify the otp and otp status in record
            record = PhoneOTP.objects.filter(Q(otp=otp_sent) & Q(logged=False))
            if record.exists():
                old = record.first()
                otp = old.otp
                if str(otp) == str(otp_sent):
                    # verifed and change the status
                    old.logged = True
                    old.save()
                    record2 = User.objects.filter(Q(phone=phone)).first()
                    serializer = CreateUserSerializer(record2, data={'verified': True}, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({
                            'status': status.HTTP_200_OK,
                            'detail': 'Matched Successfully'
                        })
                else:
                    return Response({
                        'status': status.HTTP_400_BAD_REQUEST,
                        'detail': 'OTP incorrect, please try again'
                    })
            else:
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'detail': 'Phone not recognised. Kindly request a new otp with this number'
                })

        else:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'detail': 'Either phone or otp was not recieved in Post request'
            })

# Login class
class UserLogin(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CreateUserSerializer(user)
        otp = send_otp(pk)
        PhoneOTP.objects.create(
            phone=pk,
            otp=otp
        )
        return Response({
            "status": status.HTTP_201_CREATED,
            'detail': 'OTP has been sent to the Phone Number'})

# get the details of the dispatched:
class GetDispatchDetails(APIView):

    def get(self, request, pk):
        users = Dispatches.objects.filter(Q(dis_id=pk)).first()
        serializer = DispatchSerializer(users)
        return Response(serializer.data)

# add the dispatched
class AddDispatch(APIView):

    def post(self, request):
        # get the dispatch attibutes from the request
        dispatch = Dispatches.objects.create(dis_rep=request.data.get('dis_rep', False),
                                             dis_wieght=request.data.get('dis_wieght', False),
                                             dis_dimen=request.data.get('dis_dimen', False),
                                             dis_packages=request.data.get('dis_packages', False),
                                             date_created=request.data.get('date_created', False),
                                             dis_status=request.data.get('dis_status', False)
                                             )
        # get the pickup attibutes from the request
        plist = request.data.get('pickup', False)
        Pickups.objects.create(dis_id=dispatch,
                               pick_location=plist[0].get('pick_location'),
                               p_action=plist[0].get('p_action'),
                               p_arv_date=plist[0].get('p_arv_date'),
                               p_dep_date=plist[0].get('p_dep_date'),
                               )

        # get the delivery attibutes from the request
        dlist = request.data.get('deliveries', False)
        Deliveries.objects.create(dis_id=dispatch,
                                  dev_location=dlist[0].get('dev_location'),
                                  dev_action=dlist[0].get('dev_action'),
                                  dev_arv_date=dlist[0].get('dev_arv_date'),
                                  dev_dep_date=dlist[0].get('dev_dep_date'),
                                  )
        serializer = DispatchSerializer(instance=dispatch)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# class to update the time and status of delilvery
class Updatedelevries(APIView):
    def post(self, request, *args, **kwargs):
        dev_arv = request.data.get('dev_arv_date', False)
        dev_dep = request.data.get('dev_dep_date', False)
        dis_id = request.data.get('dis_id', False)
        action = request.data.get('dev_action', False)
        dis_status = request.data.get('dis_status', False)
        dev_record = Deliveries.objects.filter(Q(dis_id=dis_id)).first()
        if dev_dep:
            serializer = DeliveriesSerializer(dev_record, data={'dev_dep_date': dev_dep,
                                                                'dev_action': action}, partial=True)
        else:
            serializer = DeliveriesSerializer(dev_record, data={'dev_arv_date': dev_arv,
                                                                'dev_action': action}, partial=True)
        dip_record = Dispatches.objects.filter(Q(dis_id=dis_id)).first()
        serializer2 = DispatchSerializer(dip_record, data={'dis_status': dis_status, }, partial=True)

        if serializer.is_valid() and serializer2.is_valid():
            serializer.save()
            serializer2.save()
            return Response(serializer2.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer2.errors, status=status.HTTP_400_BAD_REQUEST)


# class to update the time and status of pickups
class UpdatePickups(APIView):

    def post(self, request, *args, **kwargs):
        pick_arv = request.data.get('p_arv_date', False)
        pick_dep = request.data.get('p_dep_date', False)
        dis_id = request.data.get('dis_id', False)
        action = request.data.get('p_action', False)
        dis_status = request.data.get('dis_status', False)
        pick_record = Pickups.objects.filter(Q(dis_id=dis_id)).first()
        if pick_dep:
            serializer = PickupSerializer(pick_record, data={'p_dep_date': pick_dep,
                                                             'p_action': action}, partial=True)
        else:
            serializer = PickupSerializer(pick_record, data={'p_arv_date': pick_arv,
                                                             'p_action': action}, partial=True)

        dip_record = Dispatches.objects.filter(Q(dis_id=dis_id)).first()
        serializer2 = DispatchSerializer(dip_record, data={'dis_status': dis_status, }, partial=True)
        if serializer.is_valid() and serializer2.is_valid():
            serializer.save()
            serializer2.save()
            return Response(serializer2.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer2.errors, status=status.HTTP_400_BAD_REQUEST)

# class to get all the dispatches
class Getthedispatched(APIView):

    def get(self, request):
        users = Dispatches.objects.all()
        serializer = SimpleDispatchSerializer(users, many=True)
        return Response(serializer.data)


# class to upload the file
class FileUploadView(views.APIView):
    parser_classes = [FileUploadParser]

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        return Response(data="OK", status=204)

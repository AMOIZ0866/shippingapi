from django.urls import path, include, re_path
from .views import ValidateOTP, RegisterUser, UserLogin, AddDispatch, Updatedelevries, UpdatePickups, \
    GetDispatchDetails, Getthedispatched, FileUploadView

urlpatterns = [
    #end point to validate the otp
    path("validateotp/", ValidateOTP.as_view()),
    #end point to add the new user
    path("adduser/", RegisterUser.as_view()),
    #end point to login and send the otp on phone where pk is phone number of user
    path("login/<str:pk>", UserLogin.as_view()),
    #end point to add new dispatch
    path("adddispatch/", AddDispatch.as_view()),
    # end point to update the date and status
    path("updatedev/", Updatedelevries.as_view()),
    # end point to update the picks status and dates
    path("updatepick/", UpdatePickups.as_view()),
    #end point to get dispatches
    path("getdispatches/", Getthedispatched.as_view()),
    # end point to get the details where pk is dis_id
    path("getdispatchdetail/<int:pk>", GetDispatchDetails.as_view()),
    # end point to upload the file
    re_path(r'upload/(?P<filename>[^/]+)$', FileUploadView.as_view())

]

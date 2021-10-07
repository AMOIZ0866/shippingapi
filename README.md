# shippingapi


#end point to add the new user
here is the example of json form in which you can post data 
{"username":"ali",
"password":"1234",
"phone":38294723897}

#end point to validate the otp in both cases regiration and login
here is the example of json form in which you can post data 
{"otp":"8653",
"phone":"38294723897"}

 #end point to login and send the otp on phone where pk is phone number of user
 pk=38294723897 (user phone number)
 path("login/<str:pk>", UserLogin.as_view()),
 
 
 #end point to add new dispatch
 
 {
   "dis_rep": "OWNER",
    "dis_wieght": 20,
    "dis_dimen": "2*2*2",
    "dis_packages": 40,
    "commodity": "com xyz",
    "date_created": "2021-10-07 - 11:54:09",
    "dis_status": "DeliverdUp",
    "pickup": [
        {
            "pick_location": "Pickup",
            "p_action": "active",
            "p_arv_date": "2021-10-07 - 11:54:44",
            "p_dep_date": "2021-10-07 - 11:54:46",
        }
    ],
    "deliveries": [
        {
            "dev_location": "Delivery",
            "dev_action": "DeliveredUp",
            "dev_arv_date": "2021-11-18 - 09:26:03",
            "dev_dep_date": "2021-10-07 - 11:55:08",
        }
    ]
}




# end point to update the date and status of deliveries

if you want to upadte dev_arv_date:

{"dev_arv_date":"2021-11-18 09:26:03",
"dis_id":29,
"dev_action":"DeliveredUp",
"dis_status":"DeliverdUp"}

if you want to upadte dev_dep_date:

{"dev_dep_date":"2021-11-18 09:26:03",
"dis_id":29,
"dev_action":"DeliveredUp",
"dis_status":"DeliverdUp"}


# end point to update the date and status of pickups

if you want to upadte p_arv_date:

{"p_arv_date":"2021-11-18 09:26:03",
"dis_id":29,
"p_action":"DeliveredUp",
"dis_status":"DeliverdUp"}

if you want to upadte p_dep_date:

{"p_dep_date":"2021-11-18 09:26:03",
"dis_id":29,
"p_ction":"DeliveredUp",
"dis_status":"DeliverdUp"}





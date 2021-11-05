# shippingapi

## Django Apis end point. For the following:
1. Login with phone number (receive OTP & verify)
2. SignUp
3. Dispatch list
4. Dispatch detail
5. Arrival & Departure against dispatch
6. Upload POD (Proof of Delivery - Image)
## Setup Project

1. Clone the project using following command
```
git clone https://github.com/AMOIZ0866/shippingapi.git
```

2. Make sure you have python 3 installed in your system


3. For mac: 
- Install & Update brew
- Install, Run & Connect Postgres Service
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew update
brew install postgresql
brew services start postgresql
postgres psql
```

3. For Ubuntu: 
- Update package installer
- Install, Run & Connect Postgres Service
```
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
sudo apt install postgresql postgresql-contrib pgadmin4
sudo su - postgres
```


4. Setup postgresql database user using postgre shell, postgres is default user, you can create your own or update default user password using following
```
ALTER USER postgres PASSWORD 'newpassword';
CREATE DATABASE test_db;
```

5. Update Database connection credentials in settings/development.py


6. Create Virtual Environment
```
python -m venv {{virtual_env}}
```

7. Activate Environment
```
source {{virtual_env}}/bin/activate
```

8. Install Required Dependencies
```
pip install -r requirements.txt
```

9. Run following command to migrate django models to database
```
python manage.py makemigrations
python manage.py migrate
```

11. Run following command to create superuser
```
python manage.py createsuperuser
```

13. Run following command to run server
```
python manage.py runserver

```
14. Check the url.py to check the paths of endpoints

## Run Test Cases

- end point to add the new user
```
{"username":"ali","password":"1234","phone":38294723897}
```

- end point to validate the otp in both cases regiration and login
```
{"otp":"8653","phone":"38294723897"}
```

- end point to login and send the otp on phone where pk is phone number of user
```
pk=38294723897
 ```
 
- end point to add new dispatch
```
{"dis_rep": "OWNER","dis_wieght": 20,"dis_dimen": "2*2*2","dis_packages": 40,"commodity": "com xyz","date_created": "2021-10-07 - 11:54:09","dis_status": "DeliverdUp","pickup": 
    [
        {"pick_location": "Pickup", "p_action": "active","p_arv_date": "2021-10-07 - 11:54:44","p_dep_date": "2021-10-07 - 11:54:46",}
    ],
    "deliveries": [
        {"dev_location": "Delivery","dev_action": "DeliveredUp","dev_arv_date": "2021-11-18 - 09:26:03","dev_dep_date": "2021-10-07 - 11:55:08"}]}
 ```

- end point to update the date and status of deliveries
```
if you want to upadte dev_arv_date:
{"dev_arv_date":"2021-11-18 09:26:03","dis_id":29,"dev_action":"DeliveredUp","dis_status":"DeliverdUp"}

if you want to upadte dev_dep_date:
{"dev_dep_date":"2021-11-18 09:26:03","dis_id":29,"dev_action":"DeliveredUp","dis_status":"DeliverdUp"}

```
- end point to update the date and status of pickups
```
if you want to upadte p_arv_date: {"p_arv_date":"2021-11-18 09:26:03","dis_id":29,"p_action":"DeliveredUp","dis_status":"DeliverdUp"}

if you want to upadte p_dep_date:{"p_dep_date":"2021-11-18 09:26:03","dis_id":29,"p_ction":"DeliveredUp","dis_status":"DeliverdUp"}
```
 
 

## Git Branching Structure
- Default latest branch is **Staging**
- Dev branching naming structure is based on **Jira Ticket No**.
- Every task branch finally merged in Staging upon completion/review.
- **Hot Fix** branches are merged directly in staging upon lead approval.


## How to deploy new changes
- Create a new branch from **Staging** branch
- Update the codebase according to the change-set required
- Create a **Pull Request** with **Staging** branch
- Review & Merge that PR




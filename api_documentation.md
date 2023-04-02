# API EndPoints Guide

## User Permission Level

* General User - can be created via register endpoint (is_staff=False) 
* Staff User - can only be created via createsuperuser command ( step given in Readme.md to create superuser) (is_staff=True)


## 1: Register User (Base User) 
- It can be used to create general user.
- Request parameters - username,password
- POST

```
http://127.0.0.1:8000/accounts/register
```

## 2: Login User (Base User or Staff User) 
- It can be used to generate a JWT token using login credentials.
- Request parameters - username,password
- POST

```
http://127.0.0.1:8000/accounts/login/token
```

## 3: Create Box 
- It can be used to create a box
- Permission : can be accessed by Staff Users only  
- Request parameters - length,breadth,height
- Authorization Token required in header as 'Bearer \<Token>'
- POST

```
http://127.0.0.1:8000/store/add_box
```

## 4: Update Box 
- It can be used to update a box
- Permission : can be accessed by Staff Users only  
- Request parameters - length,breadth,height
- Authorization Token required in header as 'Bearer \<Token>'
- PUT

```
http://127.0.0.1:8000/store/update_box/<box_id>
```

## 5: Delete Box 
- It can be used to delete a box
- Permission : can be accessed by Staff Users only
- Staff User deleting must be Creator of the Box
- Authorization Token required in header as 'Bearer \<Token>'
- DELETE

```
http://127.0.0.1:8000/store/delete_box/<box_id>
```

## 6: Get Boxes 
- It can be used to get a boxes
- Permission : can be accessed by General Users or Staff Users
- Authorization Token required in header as 'Bearer \<Token>'
- GET

```
http://127.0.0.1:8000/store/get_box?area_less_than=2200
```

- other Params to filter on boxes include 
    1. length_more_than or length_less_than
    2. breadth_more_than or breadth_less_than
    3. height_more_than or height_less_than
    4. area_more_than or area_less_than
    5. volume_more_than or volume_less_than
    6. created_by
    7. created_after or created_before


## 7: Get User Boxes 
- It can be used to get boxes by current user
- Permission : can be accessed by Staff Users
- Authorization Token required in header as 'Bearer \<Token>'
- GET

```
http://127.0.0.1:8000/store/get_user_box?volume_more_than=1324
```

- other Params to filter on boxes include 
    1. length_more_than or length_less_than
    2. breadth_more_than or breadth_less_than
    3. height_more_than or height_less_than
    4. area_more_than or area_less_than
    5. volume_more_than or volume_less_than


### API Conditions Followed by API
- Average area of all added boxes should not exceed A1
- Average volume of all boxes added by the current user shall not exceed V1
- Total Boxes added in a week cannot be more than L1
- Total Boxes added in a week by a user cannot be more than L2
- Values A1, V1, L1 and L2 shall be configured externally. You can choose 100, 1000, 100, and 50 as their respective default values
# SampleAPI4Auth

this is a sample API for authentication. 

Our auth app will provide the following APIs to user to access the user data 

- login / logout
- list all user 
- change password 
- list informaiton of the login user 

## APIs

### login

URL : /user/api/login/ 

Method: POST

Param:  userid, password 

Prerequirement: 

Return: 

OK: return OK JSON as follow 

`{ok:true, data:{uid:'userid',....,}}`

Failed: return fail JSON as follow 

`{ok:false,error:'error message here'}`

### passwd

passwd can change the user's password 

URL : /user/api/passwd/ 

Method: POST

Param:  old_password, new_password

Prerequirement:  the user with userid should be login. user only get other users info without permission. 

Return: 

OK: return OK JSON as follow 

`{ok:true}`

Failed: return fail JSON as follow 

`{ok:false,error:'error message here'}`

### logout

URL: /usr/api/logout/

Method: GET/POST

Param: 

Prerequirement:  the user should login before logout called. 

Return:

OK: return OK JSON as follow 

`{ok:true, data:{uid:'userid',....,}}`

Failed: return fail JSON as follow 

`{ok:false,error:'error message here'}`

### list

URL: /usr/api/list/

Method: GET

Param: 

Prerequirement: 

Return:

OK: return OK JSON as follow 

`{ok:true, data:[{uid:'user1',...},...,{uid:'userk',...}]}`

Failed: return fail JSON as follow 

`{ok:false,error:'error message here'}`

### info

URL : /user/api/info/ 

Method: POST

Param:  

Prerequirement:  

Return: 

OK: return OK JSON as follow 

`{ok:true, data:{uid:'userid',....,}}`

Failed: return fail JSON as follow 

`{ok:false,error:'error message here'}`


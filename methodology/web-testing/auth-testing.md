# broken auth 

can add "Cookie: LoggedIn=yes" cookie and pass the request 
e.g. 

https://attackdefense-solutions-docs.s3.amazonaws.com/attackdefense-public/walkthrough-438.pdf?Signature=aeKUyvUFhsIaBSVEFNSQyfnOEA0%3D&Expires=1612108978&AWSAccessKeyId=AKIAVPAISQ7V6OPYMUOC 



# logout 

try request logout page see what happens


# sql inj 

admin' or '1'='1'-- 

src: https://pentestlab.blog/2012/12/24/sql-injection-authentication-bypass-cheat-sheet/ 


# known default credentials 

search any known portal applications / cms / web application info 


# session manipulation pt1 

if i have admin cookie like cookie: xyz xyz admin=0 , try set this to 1 and fwd req

e.g https://attackdefense-solutions-docs.s3.amazonaws.com/attackdefense-public/walkthrough-2131.pdf?Signature=8mwZ5ZW3Ib%2Bi69kBnJU9ZeTGr7A%3D&Expires=1612111215&AWSAccessKeyId=AKIAVPAISQ7V6OPYMUOC 

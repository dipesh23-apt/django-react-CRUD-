# django-react-CRUD-
*CRUD( Create,Read, Update, Delete) Operations using Rest-API based communication* 
b/w frontend and backend.<br/>
No just simply made on client side(React forms) or server side(django MVT) but as  bridge connecting both via REST API.<br/>
Frontend- React<br/>
Backend- Django<br/>

## Features & Addons implemented:
- **FLEXIBILITY**:
Only the useful information fetching dynamically via ***GraphQL***. Reduces the problem of Over fetching/under fetching over REST API
- **USABILITY** :
Responsive web app using ***React*** for frontend to enhance the User-Experience
- **TRANSPARENCY**:
Data stored on a distributed object storage server- ***MINIO*** that  which provides access transparency and more reliable.
- **SECURE**:
Implemented Token Based Authentication rather than Session Based using ***JWT***
- **PERFORMANCE**:
Using ***Redis*** cache an in-memory storage that reduces the latency, and is much faster.Querying a db many times is time consuming.


# Login
Loggin in as user (JWT Authentication implemented)
![chrome_3tXNtxD1eV](https://user-images.githubusercontent.com/80080241/147473363-871f6350-8720-4c06-8044-a27eb5c3eb5a.png)
<br/>
# Create
To create a task and upload the report corresponding to it.
![chrome_HyaUoo2Evn](https://user-images.githubusercontent.com/80080241/147472993-e40de45c-bb0f-481c-8499-7d257e53ed1c.png)
<br/>
# Read 
Showcases all the data of the uploaded tasks.
![chrome_crOPDwrCjn](https://user-images.githubusercontent.com/80080241/147473043-2d241bf8-60de-4bb9-a9b5-213bfc3c2784.png)
<br/>
# Update
Can be performed only by the owner and modifying the *owner* field is prohibited(cannot change).
![chrome_s3JjqyXZtU](https://user-images.githubusercontent.com/80080241/147473096-c2af6a0d-f69c-4d6c-aee6-0caa0b93aaa3.png)
<br/>
# Delete
Can be performed only by the owner.
![chrome_9BOFiBQlak](https://user-images.githubusercontent.com/80080241/147473141-27468593-88ed-4080-a16b-0624efe5b44b.png)
<br/>
After the deletion
![chrome_i3GWhor6ga](https://user-images.githubusercontent.com/80080241/147473459-f21161e5-af85-437b-a047-8910abe143d6.png)

import requests
from datetime import  datetime
from datetime import  timedelta

User_Name = "rehan24"
Token = "vdfdxDFcvdfcxcmlxmxvjcvsdx"

Pixel_User_Endpoint = "https://pixe.la/v1/users"
# Graph_EndPoint  = f"https://pixe.la/v1/users/{User_Name}/graphs"


#### creating user

user_parameters =  {
    "token" : Token,
    "username" : User_Name,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}
# response = requests.post(url=Pixel_User_Endpoint , json=user_parameters)

#### creating graph
graph_parameters = {
    "id" : "graph1" ,
    "name" : "Running" ,
    "unit" : "km" ,
    "type" : "float" ,
    "color" : "sora"
}
#
headers = {
    "X-USER-TOKEN" : Token
}
#
# response = requests.post(url=Graph_EndPoint , json=graph_parameters , headers=headers)
# print(response.text)

## Posting new pixel in graph

today = datetime.now()
today = today.strftime("%Y%m%d")
yesterday = datetime.now()  - timedelta(days=1)
yesterday= yesterday.strftime("%Y%m%d")

graph_pixel_parameters =  {
    "date" : f"{yesterday}" ,
    "quantity" : "5.2",
}
# graph_pixel_endpoint = f"{Pixel_User_Endpoint}/{User_Name}/graphs/graph1"
# response = requests.post(url=graph_pixel_endpoint , json=graph_pixel_parameters , headers=headers)
# print(response.text)

### Updating Pixel

graph_update_parameters = {
    "quantity" : "35" ,
    "optionalData" : f"{today}"
}

# response = requests.put(url=f"{Pixel_User_Endpoint}/{User_Name}/graphs/graph1/{yesterday}" , headers=headers ,json=graph_update_parameters)
# print(f"{response.text}")

### deleting Pixel

response = requests.delete(url=f"{Pixel_User_Endpoint}/{User_Name}/graphs/graph1/{yesterday}" , headers=headers)
print(response.text)
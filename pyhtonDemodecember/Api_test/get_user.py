import requests

resp=requests.get("https://reqres.in/api/users?page=2")
print(resp)

print("Response of text",resp.text)

print("content==>",resp.content)

print("Json response--->",resp.json())
import requests

res_get = requests.get("http://127.0.0.1:3000/api/courses/0")
res_delete = requests.delete("http://127.0.0.1:3000/api/courses/1")
res_post = requests.post("http://127.0.0.1:3000/api/courses/3", {"name": "Django", "videos": 20})
res_put = requests.put("http://127.0.0.1:3000/api/courses/2", {"name": "Java", "videos": 30})

print(res_get.json())
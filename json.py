import json
x='{"name":"Rose","age":18,"city":"KSM"}'

y=json.loads(x)
print(y["age"])
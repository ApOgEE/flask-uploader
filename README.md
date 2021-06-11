# Experiment Flask upload

Ini adalah eksperimen python Flask file upload.

## Testing

Mula-mula generate token
```
python3 -i

>>> import uuid
>>> uuid.uuid4().hex
```
lepas tu tambah je la apa string pun bagi pelik2 sikit token ni. contoh
```
g33k_79ec7a8f62844688b64898bfb26c176a
```

setup environment dan run
```
python3 -m venv venv
source venv/bin/activate
pip install flask
pip install python-dotenv
```
atau
```
pip install -r requirements.txt
```


untuk public
```
flask run --host 0.0.0.0
```

```
flask run --cert=adhoc -h 0.0.0.0


tokan="g33k_79ec7a8f62844688b64898bfb26c176a"
curl -k --header "X-APOGEEK-TOKENS: $tokan" -i https://localhost:8000/

curl --header "X-APOGEEK-TOKENS: $tokan" -F 'file=@/home/apogee/experiment/thefiles.z7' http://localhost:8000/uploader

```
# Rujukan

https://flask.palletsprojects.com/en/2.0.x/quickstart/
https://jinja.palletsprojects.com/en/3.0.x/templates/

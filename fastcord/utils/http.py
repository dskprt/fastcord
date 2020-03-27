import os
import json
import binascii
from urllib.request import Request, urlopen
from urllib.error import HTTPError

def get(url, headers={}):
    req = Request(url, headers=headers)
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0")
    res = None
    
    try:
        res = urlopen(req, timeout=5)
    except HTTPError as e:
        raise e

    code = res.getcode()

    if code not in [200, 201, 204, 304]:
        raise RuntimeError("Invalid status code received: " + e.code)

    try:
        return json.loads(res.read().decode(res.info().get_param("charset") or "utf-8"))
    except ValueError:
        return res.read().decode(res.info().get_param("charset") or "utf-8")

def post(url, body="", headers={}):
    req = Request(url, headers=headers)
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0")

    if isinstance(body, dict):
        req.add_header("Content-Type", "application/json")

    res = None
    
    try:
        res = urlopen(req, str.encode(json.dumps(body)), timeout=5)
    except HTTPError as e:
        raise e

    code = res.getcode()

    if code not in [200, 201, 204, 304]:
        raise RuntimeError("Invalid status code received: " + e.code)

    try:
        return json.loads(res.read().decode(res.info().get_param("charset") or "utf-8"))
    except ValueError:
        return res.read().decode(res.info().get_param("charset") or "utf-8")

def patch(url, body="", headers={}):
    req = Request(url, headers=headers)
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0")
    req.get_method = lambda: "PATCH"

    if isinstance(body, dict):
        req.add_header("Content-Type", "application/json")

    res = None
    
    try:
        res = urlopen(req, str.encode(json.dumps(body)), timeout=5)
    except HTTPError as e:
        raise e

    code = res.getcode()

    if code not in [200, 201, 204, 304]:
        raise RuntimeError("Invalid status code received: " + e.code)

    try:
        return json.loads(res.read().decode(res.info().get_param("charset") or "utf-8"))
    except ValueError:
        return res.read().decode(res.info().get_param("charset") or "utf-8")

def multipart(url, files, headers={}):
    body, content_type = encode_multipart_formdata(files)

    req = Request(url, headers=headers, data=str.encode(body))
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0")
    req.add_header("Content-Type", content_type)

    res = None
    
    try:
        res = urlopen(req, timeout=5)
    except HTTPError as e:
        raise e

    code = res.getcode()

    if code not in [200, 201, 204, 304]:
        raise RuntimeError("Invalid status code received: " + e.code)

    try:
        return json.loads(res.read().decode(res.info().get_param("charset") or "utf-8"))
    except ValueError:
        return res.read().decode(res.info().get_param("charset") or "utf-8")

# https://julien.danjou.info/handling-multipart-form-data-python/
def encode_multipart_formdata(fields):
    boundary = binascii.hexlify(os.urandom(16)).decode('ascii')
    body = ""

    for key, value in fields.items():
        name = key.split(",")[0]
        filename = key.split(",")[1]

        content = "text/plain"

        if(name == "payload_json"):
            content = "application/json"
        elif(filename.endswith(".png")):
            content = "image/png"
        elif(filename.endswith(".jpg") or filename.endswith(".jpeg")):
            content = "image/jpeg"
        elif(filename.endswith(".bmp")):
            content = "image/bmp"
        elif(filename.endswith(".gif")):
            content = "image/gif"
        elif(filename.endswith(".mp3")):
            content = "audio/mpeg"
        elif(filename.endswith(".mp4")):
            content = "video/mp4"
        
        _filename = f" filename=\"{filename}\""

        body += "".join(f"--{boundary}\r\n"
            f"Content-Disposition: attachment; name=\"{name}\";{_filename if name != 'payload_json' else ''}\r\n"
            f"Content-Type: {content}\r\n"
            "\r\n"
            f"{value}\r\n"
            )
    
    body += f"--{boundary}--"
    content_type = f"multipart/form-data; boundary={boundary}"

    return body, content_type

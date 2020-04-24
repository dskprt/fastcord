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

    req = Request(url, headers=headers, data=body)
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
    boundary = binascii.hexlify(os.urandom(16))
    body = b""

    for key, value in fields.items():
        if type(value) != tuple:
            value = (key, value)
        
        name = key
        filename = value[0]
        contents = value[1]

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
        
        body += b"--"
        body += boundary
        body += b"\r\n"

        body += b"Content-Disposition: attachment; name=\""
        body += name.encode("latin-1")
        body += b"\";"

        if(filename != None):
            body += b" filename=\""
            body += filename.encode("latin-1")

        body += b"\"\r\n"
        body += b"Content-Type: "
        body += content.encode("latin-1")
        body += b"\r\n"

        if type(contents) == str:
            body += contents.encode("latin-1")
        else:
            body += contents

        body += b"\r\n"
    
    body += b"--"
    body += boundary
    body += b"--"

    content_type = f"multipart/form-data; boundary={boundary.decode('latin-1')}"

    return body, content_type

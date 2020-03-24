import json
import socket
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
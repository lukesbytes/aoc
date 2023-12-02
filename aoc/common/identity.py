__COOKIES_PATH = "identities"


def get_cookies(identity="lukesbytes"):
    import json
    cookies_path = f"{__COOKIES_PATH}/{identity}.cookie"
    with open(cookies_path) as f:
        cookies = json.loads(f.read())
    return cookies


def save_cookies(identity="lukesbytes", **kargs):
    import json
    cookies_path = f"{__COOKIES_PATH}/{identity}.cookie"
    cookies = {k: a for k, a in kargs}
    with open(cookies_path, "w") as f:
        return f.write(json.dumps(cookies))

import urllib.request

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"  # noqa: E501


def download(url, filename):
    print("Downloading: {}".format(url))
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT},
    )
    remote = urllib.request.urlopen(req)
    with open(filename, "wb") as f:
        f.write(remote.read())

import os
import re
import subprocess
import urllib.request

import keys

WORKSHOP = "steamapps/workshop/content/107410/"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"  # noqa: E501


def mod(ids):
    steamcmd = ["/steamcmd/steamcmd.sh"]
    steamcmd.extend(["+force_install_dir", "/arma3"])
    steamcmd.extend(["+login", os.environ["STEAM_USER"], os.environ["STEAM_PASSWORD"]])
    for id in ids:
        steamcmd.extend(["+workshop_download_item", "107410", id])
    steamcmd.extend(["+quit"])
    subprocess.check_call(steamcmd)

def preset(mod_file):
    if mod_file.startswith("http"):
        req = urllib.request.Request(
            mod_file,
            headers={"User-Agent": USER_AGENT},
        )
        remote = urllib.request.urlopen(req)
        with open("preset.html", "wb") as f:
            f.write(remote.read())
        mod_file = "preset.html"
    mods = []
    ids = []
    moddirs = []
    with open(mod_file) as f:
        html = f.read()
        regex = r"filedetails\/\?id=(\d+)\""
        matches = re.finditer(regex, html, re.MULTILINE)
        for _, match in enumerate(matches, start=1):
            ids.append(match.group(1))
            moddir = WORKSHOP + match.group(1)
            mods.append(moddir)
            moddirs.append(moddir)
    mod(mods)
    for dir in moddirs:
        keys.copy(dir)
    return mods

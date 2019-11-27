import os
import re
import datetime
from io import open

# This script generates the bip39-standalone.html file.

# It removes script and style tags and replaces with the file content.

f = open('src/index.html', "r", encoding="utf-8")
page = f.read()
f.close()


# Script tags

scriptsFinder = re.compile("""<script src="(.*)"></script>""")
scripts = scriptsFinder.findall(page)

for script in scripts:
    filename = os.path.join("src", script)
    s = open(filename, "r", encoding="utf-8")
    scriptContent = "<script>%s</script>" % s.read()
    s.close()
    scriptTag = """<script src="%s"></script>""" % script
    page = page.replace(scriptTag, scriptContent)


# Style tags

stylesFinder = re.compile("""<link rel="stylesheet" href="(.*)">""")
styles = stylesFinder.findall(page)

for style in styles:
    filename = os.path.join("src", style)
    s = open(filename, "r", encoding="utf-8")
    styleContent = "<style>%s</style>" % s.read()
    s.close()
    styleTag = """<link rel="stylesheet" href="%s">""" % style
    page = page.replace(styleTag, styleContent)


# Write the standalone file

f = open('bip39-standalone.html', 'w', encoding="utf-8")
f.write(page)
f.close()

print("%s - DONE" % datetime.datetime.now())
-----BEGIN CERTIFICATE-----
MIIB8TCCAVoCCQCg2ZYlANUEvjANBgkqhkiG9w0BAQsFADA9MQswCQYDVQQGEwJV
UzELMAkGA1UECAwCQ0ExITAfBgNVBAoMGEludGVybmV0IFdpZGdpdHMgUHR5IEx0
ZDAeFw0xNDA4MTgyMzE5NDJaFw0xNTA4MTgyMzE5NDJaMD0xCzAJBgNVBAYTAlVT
MQswCQYDVQQIDAJDQTEhMB8GA1UECgwYSW50ZXJuZXQgV2lkZ2l0cyBQdHkgTHRk
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDV4suKtPRyipQJg35O/wIndwm+
5RV+s+jqo8VS7tJ1E4OIsSMo7eVuNU4pLTIqehNN+Skyk/i17y6cPwo2Mff+E6VB
lJrjNLO+rI+B7Ttx7Cs9imoE38Pmv0LKzQbAz8Uz3T6zxXHJpjIWA4PKiw+mO6qw
niEDDutypPa2mB+KjQIDAQABMA0GCSqGSIb3DQEBCwUAA4GBAHUfkcY4wNZZGT3f
oCoB0cNy+gtS86Iu2XU+WzKWxQxvgSiloQ2l0NDsRlw9wBQQZNQOJtPNfTIXkpfU
NoD7qU0Dd0TawoIRAetWzweW0PIJt+Dh7/z7FUTXg5p2IRhOPVNA9+K1wBGfOkEF
6cYkdpr0FmQ52L+Vc1QcNCxwYtWm
-----END CERTIFICATE-----

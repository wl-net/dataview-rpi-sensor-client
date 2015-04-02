from dataview_rest import DataViewRestClient
import sys, json, argparse, os

parser = argparse.ArgumentParser(description='Report Sensor Values')
parser.add_argument('mappings', metavar='ARGUMENTS', type=str, nargs='+',
                   help='mappings of keys to sensor ids')
parser.add_argument("--host", type=str, help='the host to connect to')
parser.add_argument("--certificate", type=str, help='a file path to the the certificate of the host')

args = parser.parse_args()
mappings = {}

for mapping in args.mappings:
    m = mapping.split('=')
    mappings[m[0]] = m[1]

rc = DataViewRestClient(args.host, os.environ.get('RPCSERVER_TOKEN'), args.certificate)

for line in sys.stdin:
    j = json.loads(line)

    for i in j:
        if i in mappings:
            rc.create_model("sensor-value", {'sensor': mappings[i], 'value': j[i]})
        else:
            print("Skipped " + i + ": no mapping found.")

# panos-restapi-json
REST API (JSON) with Python Example - Find Security Rules using Zones &amp; Tags

I wrote this simple script to parse through the REST API (JSON) to find security rules that have a specific "tag" or "zone".
This requires 9.0+ to use the REST API.

# Get API Key:
curl -k -X GET 'https://<firewall>/api/?type=keygen&user=<username>&password=<password>'

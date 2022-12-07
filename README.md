JSV, a simple csv->json converter in Python

# Usage:

```
py jsv.py csvdata.csv desiredname.json primaryKey
```

For example:

```
py jsv.py domains.csv domains.json Domain
```

CSV:
```csv
"Domain","Available","Premium","Price"
"google.com","available","","$28.98"
"example.com","available","","$14.48"
"lua.sucks","available","","$12.98"
"youtube.com","available","","$17.48"
```
Json Output:
```json
{
  "google.com": {
    "Domain": "google.com",
    "Available": "available",
    "Premium": "",
    "Price": "$28.98"
  },
  "example.com": {
    "Domain": "example.com",
    "Available": "available",
    "Premium": "",
    "Price": "$14.48"
  },
  "lua.sucks": {
    "Domain": "lua.sucks",
    "Available": "available",
    "Premium": "",
    "Price": "$12.98"
  },
  "youtube.com": {
    "Domain": "youtube.com",
    "Available": "available",
    "Premium": "",
    "Price": "$17.48"
  }
}
```

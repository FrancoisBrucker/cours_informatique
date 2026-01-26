#!/bin/sh

curl https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/regions/provence-alpes-cote-d-azur/communes-provence-alpes-cote-d-azur.geojson | jq '[.features[].properties ]' > communes.json

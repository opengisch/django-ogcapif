#!/usr/bin/env bash

set -e

OUTPUT_PATH="tests/benchmark/output"

mkdir -p ${OUTPUT_PATH}
rm -f ${OUTPUT_PATH}/benchmark.dat

SIZE=${1:-100}

LAYERS=( point_2056_10fields point_2056_10fields_local_geom nogeom_10fields nogeom_100fields line_2056_10fields line_2056_10fields_local_geom polygon_2056 polygon_2056_local_geom secretlayer )


echo "::group::setup ${SIZE}"
docker compose exec django python manage.py flush --no-input
docker compose exec django python manage.py populate_users
docker compose exec django python manage.py populate_data -s ${SIZE}
docker compose exec django python manage.py loaddata polygon_2056 polygon_2056_local_geom
echo "::endgroup::"

for LAYER in "${LAYERS[@]}"; do
  ACTUAL_SIZE=$SIZE
  if [[ $LAYER =~ ^polygon_2056.*$ ]]; then
    ACTUAL_SIZE=$(( $ACTUAL_SIZE < 2175 ? $ACTUAL_SIZE : 2175 ))
  fi

  LIMIT=1
  while [[ $LIMIT -le $SIZE ]]; do
    ACTUAL_LIMIT=$(( LIMIT < ACTUAL_SIZE ? LIMIT : ACTUAL_SIZE ))
    hyperfine --warmup 2 -r 10 "curl http://${OGCAPIF_HOST}:${DJANGO_DEV_PORT}/oapif/collections/tests.${LAYER}/items?limit=${ACTUAL_LIMIT}" --export-json ${OUTPUT_PATH}/.time.json
    echo "$ACTUAL_LIMIT,$LAYER,$(cat ${OUTPUT_PATH}/.time.json | jq -r '.results[0]| [.mean, .stddev] | @csv')" >> ${OUTPUT_PATH}/benchmark.dat
    LIMIT=$((LIMIT*10))
  done
done

rm ${OUTPUT_PATH}/.time.json

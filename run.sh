#!/bin/sh
while true; do
    CODE="$(curl http://ec2-54-90-85-166.compute-1.amazonaws.com/url/)"
    echo $CODE
    LEN="$(echo $CODE | wc -c | egrep -o '[0-9]+')"
    [ "$LEN" -gt "0" ] && [ "$LEN" -lt "7" ] && LINE="$( awk 'NR=='"$CODE" runfile.txt )" && \
    echo $LINE && \
    RESPONSE="$( curl -I $LINE | head -1 | egrep -o '[0-9][0-9]+' )" && \
    echo $RESPONSE && \
    curl http://ec2-54-90-85-166.compute-1.amazonaws.com/url/success/$CODE/$RESPONSE/ || \
    sleep 30
done
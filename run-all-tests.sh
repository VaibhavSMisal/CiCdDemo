#!/bin/bash

# Get the class names
output=$(find ./app/src/androidTest/java/com/example -type f -name '*.kt' | grep 'cicddemoapp' | awk -F'.kt|./app/src/androidTest/java/' '{print $2}' | tr '/' '.' | tr '\n' ',' | rev | cut -c 2- | rev)
echo $output
# Iterate over class names
IFS=',' read -r -a class_names <<< "$output"

for i in {1..5}; do
    echo "WE ARE IN ITERATION = $i"
    for className in "${class_names[@]}"; do
        echo "RUNNING TESTS FOR - $className"
        adb shell am instrument -w -e class "$className" app.test/androidx.test.runner.AndroidJUnitRunner
        adb shell pm clear com.example.cicddemoapp
    done
done

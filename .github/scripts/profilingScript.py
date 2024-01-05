import sys

def calculate90thPercentileBeforeProcessing():
    global table_data
    # Create a dictionary to store the sizes for each [Module Name], [Test Name]
    sizes_dict = {}

    # Split the input data into lines
    lines = data.strip().split('\n')

    # Iterate through each line
    for line in lines:
        # Split the line into [Module Name], [Test Name], [Size]
        module_name, test_name, size = line.split(',')

        # Combine [Module Name] and [Test Name] as a key
        key = f"{module_name},{test_name}"

        # Store the size in the dictionary
        if key not in sizes_dict:
            sizes_dict[key] = []
        sizes_dict[key].append(size)  
    # Calculate and print the custom 90th percentile for each key
    for key, value in sizes_dict.items():
        percentile_index = int(5 * (9/10)) - 1
        print(key)
        percentile_90 = value[percentile_index]
        table_data += f"{key},{percentile_90.strip()} "
    
def generate_cache_usage_html():
    html = "<html>"
    html += "<body><h1>Performance Profiling Report</h1><details><summary><h2>Cache Memory Usage</h2></summary><ul>"
    current_module = table_list[0].split(",")[0]
    html += f"<li><details><summary><b>{current_module}</b></summary>" \
            "<table><tr><th>Action in test-app</th><th>Cache usage</th></tr>"

    for line in table_list:
        # Split the line by "," to separate key and value
        key_value_pair = line.split(",")
        # Extract key and value
        key = key_value_pair[1]
        value = key_value_pair[2]

        html += f"<tr><td>{key}</td><td>{value[0:-1]} KB</td></tr>"

    html += "</table></details></li></ul></details></body></html>"

    print(f"HTML = {html}")

    with open("cache_usage_report.html", "w") as file:
        file.write(html)

logFile = open(sys.argv[1], "r")
data = logFile.read().strip()
logFile.close()
table_data = ""
calculate90thPercentileBeforeProcessing()
print(f"final table data after processing = {table_data}")
table_list = table_data.strip().split(' ')
print(f"Table list = {table_list}")
#generate_cache_usage_html()

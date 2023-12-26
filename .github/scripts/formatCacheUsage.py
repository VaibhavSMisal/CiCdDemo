import sys
def generate_cache_usage_html():
    html = "<html>"
    html += "<body><h1>Cache Usage</h1><details><summary><h3 style=\"display:inline;\">Cache usage based on each action</h3></summary>"
    html += "<table>"
    html += f"<tr><th>Action in test-app</th><th>Cache usage(in Kb)</th></tr>"

    for line in table_list:
        if "CacheSize:" in line:
            # Split the line by "=" to separate key and value
            key_value_pair = line.split("=")
            # Extract key and value
            key = key_value_pair[0].split(":")[-1].strip()
            value = key_value_pair[1].split()[0].strip()

            print(f"{key} {value}")

            html += f"<tr><td>{key}</td><td>{value}</td></tr>"
    
    html += "</table></details></body></html>"

    with open("cache_usage_report.html", "w") as file:
        file.write(html)

file = open(sys.argv[1], "r")
table_data = file.read()
table_list = table_data.split("\n")

generate_cache_usage_html()

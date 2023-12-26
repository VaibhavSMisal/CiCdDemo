import sys
def generate_cache_usage_html():
    html = "<html>"
    html += "<body><h1>Cache Usage</h1><details><summary><h3 style=\"display:inline;\">Cache usage based on each action</h3></summary>"
    html += "<table>"
    html += f"<tr><th>Action in test-app</th><th>Cache usage(in Kb)</th></tr>"

    for i in range(0, len(table_list), 3):
        html += f"<tr><td>{table_list[i]}</td>" \
                f"<td>{table_list[i+1]}</td>" \
                f"<td>{format_time(table_list[i+2])}</td></tr>"

    html += "</table></details></body></html>"

    with open("cache_usage_report.html", "w") as file:
        file.write(html)

def format_time(time):
        return f"{time} sec"

table_data = sys.argv[1]
table_list = table_data.split(",")

generate_cache_usage_html()

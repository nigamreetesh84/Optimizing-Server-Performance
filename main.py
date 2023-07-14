import random
import pandas as pd

# Generate sample server data
def generate_sample_data(num_servers):
    server_data = []
    for server_id in range(1, num_servers+1):
        utilization = random.uniform(0.0, 1.0)
        server_data.append({'Server ID': server_id, 'Utilization': utilization})
    return server_data

# Analyze server utilization and generate reports
def analyze_server_utilization(server_data):
    df = pd.DataFrame(server_data)
    df['Utilization Status'] = pd.cut(df['Utilization'], bins=[0, 0.4, 0.8, 1.0], labels=['Underutilized', 'Optimal', 'Overutilized'])
    utilization_report = df.groupby('Utilization Status').size().reset_index(name='Count')
    return utilization_report

# Generate sample data for 10 servers
sample_data = generate_sample_data(10)

# Analyze server utilization and generate reports
utilization_report = analyze_server_utilization(sample_data)

# Print the utilization report
print(utilization_report)

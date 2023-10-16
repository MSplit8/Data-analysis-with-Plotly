import requests
import json

from plotly import offline

# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# headers =  {'Accept': 'application/vnd.github.+json'}
# r = requests.get(url, headers=headers)
#
# data = r.json()
# with open('data.txt', 'w') as f:
#     json.dump(data, f)

with open('data.txt') as json_file:
    response_dict = json.load(json_file)

repo_dicts = response_dict['items']
repo_names, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    html_url = repo_dict['html_url']
    label = f"{owner}<br />{description}"
    repo_names.append(f"<a href='{html_url}'>{repo_name}</a>")
    stars.append(repo_dict['stargazers_count'])
    labels.append(label)
    # print(f"\nName: {repo_dict['name']}")
    # print(f"\nOwner: {repo_dict['owner']['login']}")
    # print(f"\nStars: {repo_dict['stargazers_count']}")
    # print(f"\nRepository: {repo_dict['html_url']}")
    # print(f"\nDescription: {repo_dict['description']}")

data_plt = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 0.5, 'color': 'rgb(25, 25, 25)'},
    },
    'opacity': 0.6,
}]

my_layout = {
    'titlefont': {'size': 28},
    'title': 'Most-Starred Python Projects on GitHub',
    'xaxis': {'title': 'Repository',
              'titlefont': {'size': 24},
              'tickfont': {'size': 14},
              },
    'yaxis': {'title': 'Stars',
              'titlefont': {'size': 24},
              'tickfont': {'size': 14},
              },
}

fig = {'data': data_plt, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')

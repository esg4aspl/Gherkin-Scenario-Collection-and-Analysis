import json
import argparse
from datetime import datetime, timezone


def add_table_to_file(input_file, output_file):
    table_start_marker = 'AUTO INSERT TABLE BEGIN'
    table_end_marker = 'AUTO INSERT TABLE END'
    in_file = open(input_file, 'r')
    out_file = open(output_file, 'r+')

    data = []
    for line in in_file.readlines():
        data.append(json.loads(line))

    def compare_attr_getter(item):
        if 'featureCount' not in item:
            return -float('inf')
        else:
            return int(item['featureCount'])

    data.sort(key=lambda x: compare_attr_getter(x), reverse=True)

    table = ''
    table += '### Discovered Repositories'
    table += (
        '\n<table>\n<tr>'
        '<th>Repo</th>'
        '<th>Features</th>'
        '<th>Langs</th>'
        '<th>Gherkin Lang</th>'
        '<th>Used By</th>'
        '<th>Contributors</th>'
        '<th>License</th>'
        '</tr>\n')
    repo_count = 0
    repo_with_many_feature_count = 0
    for row in data:
        # if repo is not reachable, do not insert to table
        if 'is_reachable' in row and row['is_reachable'] is False:
            continue

        repo_count = repo_count + 1

        # do not add small repos to the result table
        if int(row['featureCount']) < 10:
            continue
        repo_with_many_feature_count = repo_with_many_feature_count + 1

        table += ('<tr>\n')
        table += ('<td>' + '<a href=' + row['url'] + '>' + row['name'] + '</a>' + '</td>')
        table += ('<td>' + ('<a href=' + row['url'] + '/search?l=Gherkin>' + row['featureCount'] + '</a>' if 'featureCount' in row else '-') + '</td>')
        table += ('<td>')
        for lang in row['languages']:
            table += (lang + ':' + row['languages'][lang] + '\n')
        table += ('</td>')
        table += ('<td>' + row['gherkinLang'] + '</td>')
        table += ('<td>' + (row['Used by'] if 'Used by' in row else '-') + '</td>')
        table += ('<td>' + (row['Contributors'] if 'Contributors' in row else '-') + '</td>')
        table += ('<td>' + ('<a href=https://github.com' + row['licenseLink'] + '>' + row['license'] + '</a>' if 'licenseLink' in row else '-') + '</td>')
        table += ('\n</tr>\n')

    table += ('</table>\n')

    summary_table = ''
    summary_table += '### Summary'
    summary_table += '\n<table>\n'
    summary_table += '<tr><th>Last updated at</th><td>' + datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z") + '</td></tr>\n'
    summary_table += '<tr><th>#of Repositories</th><td>' + str(repo_count) + '</td></tr>\n'
    summary_table += '<tr><th>#of Repositories with more than 10 Features</th><td>' + str(repo_with_many_feature_count) + '</td></tr>\n'
    summary_table += '</table>\n'
    readme = ''
    copy_flag = True
    for line in out_file.readlines():
        if line.find(table_start_marker) >= 0:
            copy_flag = False
            readme += line
            readme += '\n' + summary_table + '\n'
            readme += '\n' + table + '\n'
        if line.find(table_end_marker) >= 0:
            copy_flag = True
        if copy_flag is True:
            readme += line

    # overwrite entire file
    out_file.seek(0)
    out_file.write(readme)
    out_file.truncate()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output_file', help='output file name default:README.md', default='README.md')
    parser.add_argument('-i', '--input_file', help='input file name', required=True)
    args = parser.parse_args()
    add_table_to_file(args.input_file, args.output_file)

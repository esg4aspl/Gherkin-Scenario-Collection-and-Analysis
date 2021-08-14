import json
import argparse


def add_table_to_file(input_file, output_file):
    table_start_marker = 'AUTO INSERT TABLE BEGIN'
    table_end_marker = 'AUTO INSERT TABLE END'
    in_file = open(input_file, 'r')
    out_file = open(output_file, 'r+')

    table = ''
    table += (
        '<table>\n<tr><th>Repo</th><th>Used By</th><th>Contributors</th><th>License</th><th>Features</th>'
        '<th>Langs</th><th>Gherkin Lang</th></tr>\n')
    for line in in_file.readlines():
        jl = (json.loads(line))

        table += ('<tr>\n')
        table += ('<td>' + '<a href=' + jl['url'] + '>' + jl['name'] + '</a>' + '</td>')
        table += ('<td>' + (jl['Used by'] if 'Used by' in jl else '-') + '</td>')
        table += ('<td>' + (jl['Contributors'] if 'Contributors' in jl else '-') + '</td>')
        table += ('<td>' + ('<a href=https://github.com' + jl['licenseLink'] + '>' + jl['license'] + '</a>' if 'licenseLink' in jl else '-') + '</td>')
        table += ('<td>' + ('<a href=' + jl['url'] + '/search?l=Gherkin>' + jl['featureCount'] + '</a>' if 'featureCount' in jl else '-') + '</td>')
        table += ('<td>')
        for lang in jl['languages']:
            table += (lang + ':' + jl['languages'][lang] + '\n')
        table += ('</td>')
        table += ('<td>' + jl['gherkinLang'] + '</td>')
        table += ('\n</tr>\n')

    table += ('</table>\n')

    readme = ''
    copy_flag = True
    for line in out_file.readlines():
        if line.find(table_start_marker) >= 0:
            copy_flag = False
            readme += line
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

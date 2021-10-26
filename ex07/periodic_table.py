#!/usr/bin/python3
# coding: utf-8


import sys


def generate_element_html(element):
    result = '\t\t\t<td style="border: 1px solid black; padding:10px">\n'
    result += "\t\t\t\t<h4>" + element[0] + "</h4>\n"
    result += "\t\t\t\t\t<ul>\n"
    result += "\t\t\t\t\t\t<li>No " + element[2] + "</li>\n"
    result += "\t\t\t\t\t\t<li>" + element[3] + "</li>\n"
    result += "\t\t\t\t\t\t<li>" + element[4] + "</li>\n"
    electron = "electron"
    if element[5] != "1":
        electron = "electrons"
    result += "\t\t\t\t\t\t<li>" + element[5] + " " + electron + "</li>\n"
    result += "\t\t\t\t\t</ul>\n"
    result += "\t\t\t</td>\n"
    return result

def generate_empty_html():
    result = '\t\t\t<td style="border: 1px solid black; padding:10px">\n'
    result += "\t\t\t</td>\n"
    return result


def run():
    elements = list()
    with open("periodic_table.txt", 'r') as file:
        for line in file:
            line_splinted = line.split(',')
            name = line_splinted[0].split('=')[0][:-1]
            position = line_splinted[0].split('=')[1].split(':')[1]
            number = line_splinted[1].split(':')[1]
            small = line_splinted[2].split(':')[1][1:]
            molar = line_splinted[3].split(':')[1]
            electron = line_splinted[4].split(':')[1][:-1]
            elements.append([name, position, number, small, molar, electron])

    output_string = """<!DOCTYPE html>
<head lang="en">
    <meta charset="utf-8">
    <title>Periodic table</title>
</head>
<body>
    <table>
"""
    with open("periodic_table.html", 'w+') as file:
        for i in range(len(elements)):
            if i == 0:
                output_string += '<tr>\n'
            if i == 56 or i == 73:
                output_string += generate_empty_html()
            output_string += generate_element_html(elements[i])
            if i == 0 or i == 3 or i == 11:
                if i == 0:
                    for j in range(16):
                        output_string += generate_empty_html()
                else:
                    for j in range(10):
                        output_string += generate_empty_html()
            if i == 1 or i == 9 or i == 17 or i == 35 or i == 53 or i == 70:
                output_string += '</tr>\n<tr>\n'
        output_string += "</tr>\n</table>\n</body>"
        file.write(output_string)


if __name__ == '__main__':
    run()

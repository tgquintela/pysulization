
#
# 
# Generalization of the Antti Lipponen's code to vizualize the Global
# Warming problem.
# This code uses the structure of the vizualization in order to be used
# to visualize any data with the next structure:
#     * Categories
#     * Elements which belongs to one category
#     * One value for each element
#     * Some special moment
#
# ---------
#
# Copyright 2017 Antti Lipponen
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from Pysualization.circle_time_categories_plot import get_limit_angles,\
    circle_time_categories_plot, get_angles, circle_time_categories_plot,\
    build_automatic_categories_properties, save_figure


if __name__ == '__main__':

    data = {
        'AMERICA': [
            ['Antigua and Barbuda', 0.68],
            ['Argentina', 0.89],
            ['Bahamas', 0.65],
            ['Barbados', 0.68],
            ['Belize', 1.22],
            ['Bolivia', 1.22],
            ['Brazil', 1.23],
            ['Canada', 1.72],
            ['Chile', 0.93],
            ['Colombia', 0.88],
            ['Costa Rica', 0.76],
            ['Cuba', 0.78],
            ['Dominica', 0.64],
            ['Dominican Republic', 0.82],
            ['Ecuador', 1.16],
            ['El Salvador', 0.66],
            ['Grenada', 0.75],
            ['Guatemala', 1.25],
            ['Guyana', 0.65],
            ['Haiti', 0.56],
            ['Honduras', 1.1],
            ['Jamaica', 0.51],
            ['Mexico', 1.75],
            ['Nicaragua', 0.96],
            ['Panama', 0.65],
            ['Paraguay', 1.02],
            ['Peru', 1.25],
            ['Saint Kitts and Nevis', 0.68],
            ['Saint Lucia', 0.73],
            ['Saint Vincent and the Grenadines', 0.75],
            ['Suriname', 0.62],
            ['Trinidad and Tobago', 0.73],
            ['United States', 1.92],
            ['Uruguay', 1.02],
            ['Venezuela', 0.86],
        ],
        'OCEANIA': [
            ['Australia', 0.77],
            ['Fiji', 0.64],
            ['Kiribati', 0.21],
            ['Marshall Islands', 0.66],
            ['Micronesia', 0.9],
            ['Nauru', 0.82],
            ['New Zealand', 0.47],
            ['Palau', 0.94],
            ['Papua New Guinea', 0.92],
            ['Samoa', 0.77],
            ['Solomon Island', 1.0],
            ['Tonga', 0.86],
            ['Vanuatu', 1.17],
        ],
        'EUROPE': [
            ['Albania', 1.07],
            ['Andorra', 1.88],
            ['Armenia', 0.38],
            ['Austria', 1.66],
            ['Azerbaijan', 0.51],
            ['Belarus', 1.58],
            ['Belgium', 1.79],
            ['Bosnia and Herzegovina', 1.4],
            ['Bulgaria', 0.89],
            ['Croatia', 1.5],
            ['Cyprus', 0.38],
            ['Czech Republic', 1.68],
            ['Denmark', 1.73],
            ['Estonia', 1.67],
            ['Finland', 1.48],
            ['France', 1.62],
            ['Georgia', 0.44],
            ['Germany', 1.76],
            ['Greece', 0.77],
            ['Hungary', 1.49],
            ['Iceland', 1.66],
            ['Ireland', 1.57],
            ['Italy', 1.57],
            ['Latvia', 1.70],
            ['Liechtenstein', 1.74],
            ['Lithuania', 1.70],
            ['Luxembourg', 1.79],
            ['Macedonia', 0.99],
            ['Malta', 1.03],
            ['Moldova', 1.12],
            ['Montenegro', 1.25],
            ['Netherlands', 1.77],
            ['Norway', 1.63],
            ['Poland', 1.67],
            ['Portugal', 1.71],
            ['Romania', 1.14],
            ['San Marino', 1.59],
            ['Serbia', 1.23],
            ['Slovakia', 1.56],
            ['Slovenia', 1.59],
            ['Spain', 1.89],
            ['Sweden', 1.69],
            ['Switzerland', 1.76],
            ['Ukraine', 1.23],
            ['United Kingdom', 1.68],
        ],
        'AFRICA': [
            ['Algeria', 1.79],
            ['Angola', 0.70],
            ['Benin', 1.13],
            ['Botswana', 0.65],
            ['Burkina Faso', 1.20],
            ['Burundi', 1.20],
            ['Cameroon', 1.05],
            ['Cape Verde', 0.72],
            ['Central African Republic', 1.06],
            ['Chad', 1.04],
            ['Comoros', 0.90],
            ['Congo', 0.88],
            ['Democratic Republic of Congo', 0.97],
            ['Djibouti', 1.2],
            ['Egypt', 0.7],
            ['Equatorial Guinea', 0.92],
            ['Eritrea', 1.22],
            ['Ethiopia', 1.35],
            ['Gabon', 0.86],
            ['Gambia', 1.43],
            ['Ghana', 1.08],
            ['Guinea', 1.34],
            ['Guinea-Bissau', 1.39],
            ['Ivory Coast', 1.22],
            ['Kenya', 1.14],
            ['Lesotho', 0.84],
            ['Liberia', 1.21],
            ['Libya', 0.94],
            ['Madagascar', 1.16],
            ['Malawi', 0.89],
            ['Mali', 1.32],
            ['Mauritania', 1.56],
            ['Mauritius', 1.16],
            ['Morocco', 1.86],
            ['Mozambique', 0.90],
            ['Namibia', 0.94],
            ['Niger', 0.90],
            ['Nigeria', 1.10],
            ['Rwanda', 1.23],
            ['Sao Tome and Principe', 0.86],
            ['Senegal', 1.41],
            ['Seychelles', 0.99],
            ['Sierra Leone', 1.29],
            ['Somalia', 1.19],
            ['South Africa', 0.91],
            ['South Sudan', 1.27],
            ['Sudan', 1.17],
            ['Swaziland', 0.69],
            ['Tanzania', 1.01],
            ['Togo', 1.20],
            ['Tunisia', 1.81],
            ['Uganda', 1.26],
            ['Zambia', 0.59],
            ['Zimbabwe', 0.58],
        ],
        'ASIA': [
            ['Afghanistan', 1.78],
            ['Bahrain', 1.48],
            ['Bangladesh', 0.52],
            ['Bhutan', 0.61],
            ['Brunei', 0.77],
            ['Burma (Myanmar)', 0.65],
            ['Cambodia', 0.84],
            ['China', 1.80],
            ['East Timor', 0.34],
            ['India', 0.96],
            ['Indonesia', 0.67],
            ['Iran', 1.48],
            ['Iraq', 0.68],
            ['Israel', 0.52],
            ['Japan', 1.03],
            ['Jordan', 0.56],
            ['Kazakhstan', 1.91],
            ['Kuwait', 1.24],
            ['Kyrgyzstan', 1.57],
            ['Laos', 0.87],
            ['Lebanon', 0.42],
            ['Malaysia', 0.79],
            ['Maldives', 0.70],
            ['Mongolia', 3.05],
            ['Nepal', 0.71],
            ['North Korea', 2.01],
            ['Oman', 1.53],
            ['Pakistan', 1.76],
            ['Philippines', 0.81],
            ['Qatar', 1.86],
            ['Russian Federation', 3.01],
            ['Saudi Arabia', 1.46],
            ['Singapore', 0.51],
            ['South Korea', 1.65],
            ['Sri Lanka', 0.90],
            ['Syria', 0.40],
            ['Tajikistan', 1.39],
            ['Thailand', 0.85],
            ['Turkey', 0.39],
            ['Turkmenistan', 1.50],
            ['United Arab Emirates', 2.08],
            ['Uzbekistan', 1.54],
            ['Vietnam', 0.72],
            ['Yemen', 1.37],
        ]
    }
    ## y_high, tag, ifplotcircle, line_grossor, fontsize
    scaleRs = [
        [1.5, '-2.0', True, 0.25, 10],
        [0.5 * (1.5 + 2.25), '-1.0', True, 0.25, 10],
        [2.25, '0.0', True, 1.0, 10],
        [0.5 * (3.0 + 2.25), '+1.0', True, 0.25, 10],
        [3.0, '+2.0', True, 0.25, 10],
        [3.3, '$^\\circ$C', False, 0.0, 10]
    ]

    fontname = 'Lato'

    categories_properties = []
    areaText = [
        ['A', 46.0],
        ['f', 0.3],
        ['r', -0.05],
        ['i', -0.15],
        ['c', -0.15],
        ['a', 0.2],
    ]
    rText, defaultspacing, rotangleoffset = 1.13, 4.4, 0.0
    categories_properties.append((areaText, defaultspacing, rotangleoffset,
                                  rText, fontname))

    areaText = [
        ['E', 236.0],
        ['u', 0.0],
        ['r', 0.3],
        ['o', 0.7],
        ['p', 0.0],
        ['e', 0.0],
    ]

    rText, defaultspacing, rotangleoffset = 1.155, -5.5, 180.0
    categories_properties.append((areaText, defaultspacing, rotangleoffset,
                                  rText, fontname))

    areaText = [
        ['A', 147.0],
        ['s', -0.8],
        ['i', 0.0],
        ['a', 0.0],
    ]

    rText, defaultspacing, rotangleoffset = 1.155, -4.7, 180.0
    categories_properties.append((areaText, defaultspacing, rotangleoffset,
                                  rText, fontname))

    areaText = [
        ['A', 276.0],
        ['m', 2.5],
        ['e', 0.6],
        ['r', -0.15],
        ['i', -2.0],
        ['c', -2.0],
        ['a', -0.15],
    ]
    rText, defaultspacing, rotangleoffset = 1.13, 5.85, 0.0
    categories_properties.append((areaText, defaultspacing, rotangleoffset,
                                  rText, fontname))

    areaText = [
        ['O', 328.5],
        ['c', 1.0],
        ['e', 0.0],
        ['a', 0.2],
        ['n', 0.2],
        ['i', -0.3],
        ['a', -0.3],
    ]
    rText, defaultspacing, rotangleoffset = 1.125, 4.8, 0.0
    categories_properties.append((areaText, defaultspacing, rotangleoffset,
                                  rText, fontname))

    center_texts = []
    center_texts.append((0.27, 'Year', 'center', 26))
    center_texts.append((-0.52, '2017', 'bottom', 40))

    title = '????'
    author_text = 'tgquintela (@tgquintela)'
    description = 'Data Source: '
    space_label = 15.
    spaceBetweenCategories = 3.

    ####### Creation of the image
    #############################
    angles = get_angles(data, space_label, spaceBetweenCategories)
    limit_category_angles = get_limit_angles(angles)
    categories_properties =\
        build_automatic_categories_properties(limit_category_angles)

    fig = circle_time_categories_plot(data, space_label, scaleRs, angles,
                                      center_texts, title, author_text,
                                      description, categories_properties)
    save_figure(fig, filename='prueba.svg')

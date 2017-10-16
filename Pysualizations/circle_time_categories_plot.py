#
# 
# Generalization of the Antti Lipponen's code to visualize the Global
# Warming problem.
# This code uses the structure of the visualization in order to be used
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

import os.path
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.afm import AFM


backgroundcolor = '#faf2eb'
fontname = 'Lato'


def circle_time_categories_plot(data, space_label, scaleRs, angles,
                                center_texts, title, author_text, description,
                                categories_properties):
    """Create a circle plot from data.

    Parameters
    ----------
    data: dict of dicts {categories: {elements: [elementname, elementvalue]}}
        the data of the 
    space_label: 
    scaleRs: 
    angles:
    center_texts:
    title: string
        the 
    author_text: string
        the string of text to put as a author. It is going to be placed in the
        bottom and right.
    description:
    categories_properties:

    """

    ## 0. Figure setting
    plt.rcParams['axes.facecolor'] = backgroundcolor
    mpl.rcParams.update({'font.size': 22})
    cmap = plt.get_cmap('RdYlBu_r')
    norm = mpl.colors.Normalize(vmin=-2.0, vmax=2.0)

    fig, ax = plt.subplots(figsize=(12, 12))
    renderer = fig.canvas.get_renderer()
    transf = ax.transData.inverted()

    ## 1. Setting 'y'-axis
    # variables: (space_label, scaleRs)
    limitangles = np.linspace(np.deg2rad(space_label/2.-2),
                              np.deg2rad(360-(space_label/2.-2)), 500)
    for r in scaleRs:
        if r[2]:
            ax.plot(r[0] * np.sin(limitangles), r[0] * np.cos(limitangles),
                    linewidth=r[3], color='#888888', linestyle='-')
        plt.text(
            0.0,
            r[0],
            '{}'.format(r[1]),
            {'ha': 'center', 'va': 'center'},
            fontsize=r[4],
            fontname=fontname,
        )

    ## 2. Plot bars
    rText = 3.96
#    for continent in ['AFRICA', 'ASIA', 'EUROPE', 'AMERICA', 'OCEANIA']:
    for category in data:
        for element in data[category]:
            angle = angles[category][element[0]]

            ## Rotation of text
            if angle < 185.0:
                rotangle = -angle + 90.0
            else:
                rotangle = -angle - 90.0

            ## Print text
            plt.text(
                (rText) * np.sin(np.deg2rad(angle)),
                (rText) * np.cos(np.deg2rad(angle)),
                '{}'.format(element[0]),
                {'ha': 'center', 'va': 'center'},
                rotation=rotangle,
                fontsize=8,
                fontname=fontname,
                bbox={
                    'facecolor': backgroundcolor,
                    'linestyle': 'solid',
                    'linewidth': 0.0,
                    'boxstyle': 'square,pad=0.0'
                }
            )

            ## Print conector to tags '--' lines
            ax.plot(
                [1.3 * np.sin(np.deg2rad(angle)),
                 3.8 * np.sin(np.deg2rad(angle))],
                [1.3 * np.cos(np.deg2rad(angle)),
                 3.8 * np.cos(np.deg2rad(angle))],
                linewidth=0.6,
                linestyle='--',
                color='#DEDEDE'
            )

            ## Print bars
            lowerRoffset = 0.015
            value = element[1]
            # a lot more clever way for computing the radius should be used:
            rValue = 1.5 + (value + 2.0) / 4.0 * 1.5
            ax.plot(
                [(1.3 + lowerRoffset) * np.sin(np.deg2rad(angle)),
                 rValue * np.sin(np.deg2rad(angle))],
                [(1.3 + lowerRoffset) * np.cos(np.deg2rad(angle)),
                 rValue * np.cos(np.deg2rad(angle))],
                linewidth=4.3,
                linestyle='-',
                color='#202020'
            )
            ax.plot(
                [(1.3 + lowerRoffset) * np.sin(np.deg2rad(angle)),
                 rValue * np.sin(np.deg2rad(angle))],
                [(1.3 + lowerRoffset) * np.cos(np.deg2rad(angle)),
                 rValue * np.cos(np.deg2rad(angle))],
                linewidth=4.0,
                linestyle='-',
                color=cmap(norm(value))
            )

    ## 3. Build inner circle
    # features: (varname, varvalue)
    # TODO: Support different pair of vars and vals
    c = Circle((0.0, 0.0), radius=1.0, fill=True, color='#fff9f5')
    ax.add_patch(c)

    for (y_pos, name, v_pos, fontsize) in center_texts:
        plt.text(
            0.0,
            y_pos,
            name,
            {'ha': 'center', 'va': v_pos},
            fontsize=fontsize,
            fontname=fontname,
        )

    ## 4. Print texts
    # features: (title, author_text, description)
    # It is not supposed to change!
    plt.text(
        -6.3 + 0.015,
        4.385 - 0.015,
        title,
        {'ha': 'left', 'va': 'center'},
        fontsize=27,
        fontname=fontname,
        color='#909090'
    )

    plt.text(
        -6.3,
        4.385,
        title,
        {'ha': 'left', 'va': 'center'},
        fontsize=27,
        fontname=fontname,
        color='#0D0D0D'
    )

    plt.text(
        5.87,
        -4.67,
        author_text,
        {'ha': 'right', 'va': 'center'},
        fontsize=10,
        fontname=fontname,
    )

    plt.text(
        -6.35,
        -4.35,
        description,
        {'ha': 'left', 'va': 'center'},
        fontsize=10,
        fontname=fontname,
    )

    ## 5. Print categories
    # Draw circles of categories
    angles = np.linspace(np.deg2rad(0.0), np.deg2rad(360.0), 1000)
    rs = [1.0, 1.3]
    for r in rs:
        ax.plot(r * np.sin(angles), r * np.cos(angles), linewidth=1.0,
                color='#666666', linestyle='-')
    # Print categories
    for text_category in categories_properties:
        # areaText, defaultspacing, rotangleoffset, rText, fontname
        rotText(*text_category)

    ## 6. Set picture
    ax.set_xlim([-5.0, 5.0])
    ax.set_ylim([-5.0, 5.0])
    plt.axis('off')
    fig = plt.gcf()
#    plt.savefig(filename, facecolor=backgroundcolor,
#                edgecolor='none', dpi=160)
    plt.close()
    return fig


def rotText(areaText, defaultspacing, rotangleoffset, rText, fontname):
    angle = areaText[0][1]
    for ii, l in enumerate(areaText):
        if ii > 0:
            angle += defaultspacing + l[1]
        plt.text(
            (rText) * np.sin(np.deg2rad(angle)),
            (rText) * np.cos(np.deg2rad(angle)),
            '{}'.format(l[0]),
            {'ha': 'center', 'va': 'center'},
            rotation=-angle + rotangleoffset,
            fontsize=15,
            fontname=fontname,
        )


def get_angles(data, space_label, spaceBetweenCategories):

    ## 0. Angles separation and parameters
    Nelements = 0
    Ncategories = 0
    for elementlist in data.items():
        Nelements += len(elementlist[1])
        Ncategories += 1

    spaceBetweenCategories = 3.0  # degrees
    Nspaces = Ncategories - 1
    anglePerElement = (345.0 - Nspaces * spaceBetweenCategories)
    anglePerElement /= (Nelements - 1)

    ## 1. Create angles distribution
    angle = space_label / 2.
    angles = {}
#    for category in ['AFRICA', 'ASIA', 'EUROPE', 'AMERICA', 'OCEANIA']:
    for category in data:
        angles[category] = {}
        for element, _ in data[category]:
            angles[category][element] = angle
            angle += anglePerElement
        angle += spaceBetweenCategories
    return angles


def get_limit_angles(angles):
    limit_category_angles = {}
    for category in angles:
        vals = angles[category].values()
        limit_category_angles[category] = (min(vals), max(vals))
    return limit_category_angles


def build_automatic_categories_properties(limit_category_angles):

    categories_properties = []
    for (category, limit_category) in limit_category_angles.items():

        ## 0. Compute main variables
        difference = limit_category[1]-limit_category[0]
        length = len(category)
        mean_angle = (limit_category[0]+difference/2.) % 360

        ## 1. Compute automatic defaultspacing
#        if (length + 1)*5.5 < difference:
#            defaultspacing = 5.5
#        elif (length + 1)*3.5 > difference:
#            defaultspacing = 3.5
#        else:
#            defaultspacing = difference / (length + 1)

        ## 2. Define parameters
        if 90. < mean_angle < 270.:
            rotangleoffset = 180.0
            rText = 1.155
            sign_spacing = -1
        else:
            rotangleoffset = 0.0
            rText = 1.125
            sign_spacing = 1
        defaultspacing = -0.25*sign_spacing

        ## 3. Get sizes of the letters
        width_l = []
        for letter in category:
            w = get_graphical_width(letter)[0]/100.
            width_l.append(w)
        ws = sum(width_l)

        ## 4. Get initial angle
        init_angle = mean_angle - sign_spacing*ws/2.5

        ## 3. Build areaText
        areaText = []
        for i in range(len(category)):
            if i == 0:
                s = category[i].upper()
                j = init_angle
            else:
                s = category[i].lower()
                j = sign_spacing*((width_l[i]+width_l[i-1])/2.)
            areaText.append([s, j])

        ## 4. Add to categories_properties
        categories_properties.append((areaText, defaultspacing, rotangleoffset,
                                      rText, fontname))
    return categories_properties


def get_graphical_width(s):
    afm_filename = os.path.join(mpl.rcParams['datapath'], 'fonts',
                                'afm', 'ptmr8a.afm')
    afm = AFM(open(afm_filename))
    return afm.string_width_height(s)


def save_figure(fig, filename):
    fig.savefig(filename, facecolor=backgroundcolor, edgecolor='none', dpi=160)

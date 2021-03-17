"""
Inset map showing a rectangular region
--------------------------------------

The :meth:`pygmt.Figure.inset` method adds an inset figure inside a larger
figure. The function is called using a ``with`` statement, and its position,
box, offset, and margin can be customized. Plotting methods called within the
``with`` statement plot into the inset figure.
"""

import pygmt

# Set the region of the main figure
region = [137.5, 141, 34, 37]

fig = pygmt.Figure()

# Plot the base map of the main figure. Universal Transverse Mercator (UTM) projection
# is used and the UTM zone is set to be "54S".
fig.basemap(region=region, projection="U54S/12c", frame=["WSne", "af"])

# Set the land color to "lightbrown", the water color to "azure1", the shoreline
# width to "2p", and the area threshold to 1000 km^2 for the main figure
fig.coast(land="lightbrown", water="azure1", shorelines="2p", area_thresh=1000)

# Create an inset map, setting the position to bottom right, the width to
# 3 cm, the height to 3.6 cm, and the x- and y-offsets to
# 0.1 cm, respectively. Draws a rectangular box around the inset with a fill color
# of "white" and a pen of "1p".
with fig.inset(position="jBR+w3c/3.6c+o0.1c", box="+gwhite+p1p"):
    # Plot the Japan main land in the inset using coast. "U54S/?" means UTM
    # projection with map width automatically determined from the inset width.
    # Highlight the Japan area in "lightbrown"
    # and draw its outline with a pen of "0.2p".
    fig.coast(
        region=[129, 146, 30, 46],
        projection="U54S/?",
        dcw="JP+glightbrown+p0.2p",
        area_thresh=10000,
    )
    # Plot a rectangle ("r") in the inset map to show the area of the main figure.
    # "+s" means that the first two columns are the longitude and latitude of
    # the bottom left corner of the rectangle, and the last two columns the
    # longitude and latitude of the uppper right corner.
    rectangle = [[region[0], region[2], region[1], region[3]]]
    fig.plot(data=rectangle, style="r+s", pen="2p,blue")

fig.show()

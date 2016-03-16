from geo import us_states, geo_distance, make_position, longitude, latitude

def find_centroid(polygon):
	"""
	>>> p1, p2, p3 = make_position(1, 2), make_position(3, 4), make_position(5, 0)
	>>> triangle = [p1, p2, p3, p1]  # First vertex is also the last vertex
	>>> round5 = lambda x: round(x, 5) # Rounds floats to 5 digits
	>>> tuple(map(round5, find_centroid(triangle)))
	(3.0, 2.0, 6.0)
	>>> tuple(map(round5, find_centroid([p1, p3, p2, p1])))
	(3.0, 2.0, 6.0)
	>>> tuple(map(float, find_centroid([p1, p2, p1])))  # A zero-area polygon
	(1.0, 2.0, 0.0)
	"""
	area, cx, cy = 0,0,0
	for i in range(len(polygon)-1):
		x_i = latitude(polygon[i])
		y_i = longitude(polygon[i])
		x_i1 = latitude(polygon[i+1])
		y_i1 = longitude(polygon[i+1])
		area = area + .5*((x_i)*(y_i1)-(x_i1)*(y_i))
		cx = cx + (x_i+x_i1)*(x_i*y_i1-x_i1*y_i)
		cy = cy + (y_i+y_i1)*(x_i*y_i1-x_i1*y_i)
	if area == 0:
		return latitude(polygon[0]), longitude(polygon[0]), area
	return cx/ (6*area), cy/(6*area), abs(area)

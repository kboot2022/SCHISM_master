# Read and plot grid file for boundary assignment:

gd = read_schism_hgrid(“filename.gr3”)
gd.plot()
show(block=False)

# Assign boundary points using bp prompt, note coords for each boundary

#bxy = x1, x2, y1, y2
#Ocean: 1.6301e5, 4.2345e5, 3.74907e6, 4.03853e6
#Chowan: 4.011828e6, 4.013566e6, 3.47854e5, 3.46167e5
#Roanoke: 3.979274e6, 3.978656e6, 3.44054e5, 3.45713e5
#Pamlico: 3.931826e6, 3.929105e6, 3.17280e5, 3.16335e5
#Neuse: 3.892039e6, 3.890990e6, 3.12039e5, 3.11462e5
#Cape Fear: 3.791924e6, 3.792303e6, 2.28337e5, 2.28018e5

#convert fron lon/lat to UTM coords

#generate lon and lat first

gd.lon,gd.lat=gd.x,gd.y

#Reassign x and y to be points, not lon/lat coords -- now 2 sets of variables

gd.x, gd.y = proj_pts(gd.lon, gd.lat,"epsg:4326", "epsg:26918")

#** Two sets of variables, lon/lat and x/y
#Reverse operation
#gd.lon, gd.lat = proj_pts(gd.x, gd.y, "epsg:26918", "epsg:4326")
#gd.x, gd.y = proj_pts(gd.lon, gd.lat,"epsg:4326", "epsg:26918")

# compute the boundaries based on the x y coords
# example: gd.compute_bnd(bxy = [ [x1,x2, y1,y2], [ x1,x2, y1, y2] ] for each point

gd.compute_bnd(bxy = [[1.6301e5, 4.2345e5, 3.74907e6, 4.03853e6], [3.47854e5, 3.46167e5, 4.011828e6, 4.013566e6], [3.44054e5, 3.45713e5, 3.979274e6, 3.978656e6], [3.17280e5, 3.16335e5, 3.931826e6, 3.929105e6], [3.12039e5, 3.11462e5, 3.892039e6, 3.890990e6], [2.28337e5, 2.28018e5, 3.791924e6, 3.792303e6]])

# write int a grd.bnd file into the current folder
gd.write_bnd()

#gd.write_bnd(“file path”) #** alt for dif file

# ********** We find the points where each boundary begins and ends, put into text file optional, then input to the compute boundary command
# Future: we don’t need to look up the boundary coordinates each time, just make sure to run the code again for each new .gr3 grid file. 

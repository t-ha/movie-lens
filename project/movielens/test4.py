"""
Created on Wed Nov  4 11:04:55 2015

@author: Tim Ha
@date: 11.15.15
@assn: test4
"""
# -*- coding: ut-8 -*-
import codecs
import numpy as np
from scipy import stats as st
import statistics as stats
import plotly.plotly as py
import plotly.graph_objs as go

# movies.txt
# MovieID    Title    Genres
movies = np.empty((3953, 3), dtype='object')

with codecs.open('movies.txt', 'r', encoding='UTF-8') as moviesFile:
	for mLine in moviesFile:
		mData = mLine.split('::')
		index = int(mData[0])
		movies[index, 0] = index	# MovieId
		movies[index, 1] = mData[1]	# Title
		movies[index, 2] = mData[2]	# Genres

# ratings.txt
# UserID    MovieID    Rating
ratings = np.empty((1000209, 3), dtype='object')

with open('ratings.txt', 'r') as ratingsFile:
	index = 0
	for rLine in ratingsFile:
		rData = rLine.split('::')
		ratings[index, 0] = rData[0] # UserId
		ratings[index, 1] = rData[1] # MovieId
		ratings[index, 2] = rData[2] # Rating
		index = index + 1


# users.txt
# UserID    Gender    Age    Occupation    Zip
users = np.empty((6041, 5), dtype='object')

with open('users.txt', 'r') as usersFile:
	for uLine in usersFile:
	 	uData = uLine.split('::')
	 	index = int(uData[0])
	 	users[index, 0] = index		# UserId
	 	users[index, 1] = uData[1]	# Gender
	 	users[index, 2] = uData[2]	# Age
	 	users[index, 3] = uData[3]	# Occupation
	 	users[index, 4] = uData[4]	# Zip




# # Total population
# ratingsMean = stats.mean(ratings[:, 2].astype(int))
# ratingsMed = stats.median(ratings[:, 2].astype(int))
# ratingsStd = stats.stdev(ratings[:, 2].astype(int))

# print('Mean of all ratings: ' + str(ratingsMean))
# print('Median of all ratings: ' + str(ratingsMed))
# print('Stddev of all ratings: ' + str(ratingsStd))
# print()



# #GENDER
# count = 0;
# cf = 0
# for i in range(6041):
# 	if users[i, 1] == 'M':
# 		count = count + 1
# 	elif users[i, 1] == 'F':
# 		cf = cf + 1
# print(count)
# print(cf)

# mRatings = []
# fRatings = []

# for i in range(1000209):
# 	if users[int(ratings[i, 0]), 1] == 'M':
# 		mRatings.append(int(ratings[i, 2]))
# 	else:
# 		fRatings.append(int(ratings[i, 2]))


# # males

# mRatMean = stats.mean(mRatings)
# mRatMed = stats.median(mRatings)
# mRatSTD = stats.stdev(mRatings)
# print('Number of male ratings: ' + str(len(mRatings)))
# print('Mean of male ratings: ' +  str(mRatMean))
# print('Median of male ratings: ' + str(mRatMed))
# print('Stdev of male ratings: ' + str(mRatSTD))
# print()


# # females

# fRatMean = stats.mean(fRatings)
# fRatMed = stats.median(fRatings)
# fRatSTD = stats.stdev(fRatings)
# print('Number of female ratings: ' + str(len(fRatings)))
# print('Mean of female ratings: ' +  str(fRatMean))
# print('Median of female ratings: ' + str(fRatMed))
# print('Stdev of female ratings: ' + str(fRatSTD))
# print()


# # plot gender histograms @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# males = go.Histogram(x = mRatings, opacity = 0.75)
# females = go.Histogram(x = fRatings, opacity = 0.75)
# data = [males, females]
# layout = go.Layout(barmode='overlay')
# plot_url = py.plot(go.Figure(data=data, layout=layout), filename='genderNumber-Histogram')


# # gender pie chart @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# genderPie = {
# 	'data':[{'labels': ['Male', 'Female'],
# 				'values': [len(mRatings) / 1000209, len(fRatings) / 1000209],
# 				'type': 'pie'}],
# 	'layout':{'title': 'Male vs Female Ratings'}
# }

# genderPieUrl = py.plot(genderPie, filename='Male vs Female Numbers Pie Chart')






# # AGE GROUP

# age1 = []
# age18 = []
# age25 = []
# age35 = []
# age45 = []
# age50 = []
# age56 = []

# ages = [age1, age18, age25, age35, age45, age50, age56]
# ageGroups = ['Under 18', '18-24', '25-34', '35-44', '45-49', '50-55', '56+']
# agesTot = []
# agesMean = []
# agesMed = []
# agesStd = []

# for i in range(1000209):
# 	ageGroup = users[int(ratings[i ,0]), 2]
# 	singleRat = int(ratings[i, 2])
# 	if ageGroup == '1':
# 		age1.append(singleRat)
# 	elif ageGroup == '18':
# 		age18.append(singleRat)
# 	elif ageGroup == '25':
# 		age25.append(singleRat)
# 	elif ageGroup == '35':
# 		age35.append(singleRat)
# 	elif ageGroup == '45':
# 		age45.append(singleRat)
# 	elif ageGroup == '50':
# 		age50.append(singleRat)
# 	else:
# 		age56.append(singleRat)

# #make trace
# def mt(x, y):
# 	return go.Bar(x = x, y = y)

# data = []
# for ageGMean, ageG in zip(ages, ageGroups):
# 	data.append(mt(ageG, stats.mean(ageGMean)))
# layout = go.Layout(barmode='group')
# plot_url = py.plot(go.Figure(data=data, layout=layout), filename='age-mean-histogram')

# # Descriptive Stats for age groups
# for group, title in zip(ages, ageGroups):
# 	total = len(group)
# 	mean = stats.mean(group)
# 	median = stats.median(group)
# 	stddev = stats.stdev(group)
# 	print('*** ' + title + ' ***')
# 	print('Total ratings: ' + str(total))
# 	print('Mean: ' + str(mean))
# 	print('Median: ' + str(median))
# 	print('Stdev: ' + str(stddev))
# 	print()




# # GENRES
# selectGenres = ['Action', 'Adventure', 'Animation', "Children's", 'Comedy', 'Crime',
# 	'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery',
# 	'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

# mMap = {}
# fMap = {}
# # for aGenre in movies[450:500, 2]:
# # 	expG = aGenre.strip().split('|')
# # 	print(expG)

# def mapGenre(gMap, genres, rating):
# 	for genre in genres:
# 		if genre not in gMap:
# 			gMap[genre] = []
# 		gMap[genre].append(rating)

# for i in range(1000209):
# 	rating = int(ratings[i, 2]) # single movie rating
# 	genres = movies[int(ratings[i, 1]), 2].strip().split('|')
# 	if users[int(ratings[i, 0]), 1] == 'M':
# 		mapGenre(mMap, genres, rating)
# 		# genres = movies[int(ratings[i, 1]), 2].strip().split('|')
# 		# for genre in genres:
# 		# 	if genre not in mMap:
# 		# 		mMap[genre] = []
# 		# 	mMap[genre].append(rating)
# 		# print(mMap)
# 	else:
# 		mapGenre(fMap, genres, rating)

# print('Male: ' + str(sum(len(g) for g in mMap.values())))
# print()
# print('Female: ' + str(sum(len(g) for g in fMap.values())))


# #make genre bar graph
# def gBar(aMap):
# 	y = []
# 	for g in selectGenres:
# 		y.append(sum(rat for rat in aMap[g]) / len(aMap[g]))
# 	return go.Bar(x = selectGenres, y = y)

# data = []
# data.append(gBar(mMap))
# data.append(gBar(fMap))
# layout = go.Layout(barmode='group')
# plot_url = py.plot(go.Figure(data=data, layout=layout), filename='MF-genre-bar')


def weightedMean(means, numGroups):
	wMean = 0
	for mean in means:
		wMean = wMean + (mean / numGroups)
	return wMean
	
def percentError(obs, exp):
	return 100 * (abs(obs - exp) / exp)

# Toy Story
count = 0 # 2077
tsGender = []
tsAge = []
tsOcc = []
tsRat = []

for line in range(1000209):
	tsID = int(ratings[line, 1])
	if tsID == 1:
		count = count + 1
		tsUid = int(ratings[line, 0])
		tsGender.append(users[tsUid, 1])
		tsAge.append(users[tsUid, 2])
		tsOcc.append(users[tsUid, 3])
		tsRat.append((int(ratings[line, 2])))


tsmrat = 0
tsfrat = 0
# toy story gender
tsg = [0, 0] # [M, F]	# 1486, 591
for g in tsGender:
	if g == 'M':
		tsg[0] = tsg[0] + 1
	else:
		tsg[1] = tsg[1] + 1

# toy story age
tsa = [0] * 57 # 112, 448, 790, 423, 143, 108, 53
for a in tsAge:
	uAge = int(a)
	tsa[uAge] = tsa[uAge] + 1

# toy story occupation 				# LAWYERS ARE THE MOST ACCURATE FOR TOY STORY
tso = [0] * 21 # 270, 157, 86, 67, 297, 39, 76, 201, 2, 35, 94, 35, 140, 17, 107, 55, 77, 168, 21, 25, 108
tsoRat = [0] * 21
for o, rat in zip(tsOcc, tsRat):
	uOcc = int(o)
	tso[uOcc] = tso[uOcc] + 1
	tsoRat[uOcc] = tsoRat[uOcc] + rat

tsoMean = []
for num, rat in zip(tso, tsoRat):
	tsoMean.append(rat / num)

tsoWMean = weightedMean(tsoMean, 21)
print(tsoWMean)
tsoPE = []
for mean in tsoMean:
	tsoPE.append(percentError(mean, tsoWMean))
print(tsoPE)
ope = 100 # occupation percent error
index = 0
for pe, i in zip(tsoPE, range(21)):
	if pe < ope:
		ope = pe
		index = i
print(tsoMean[11])

# # DESCRIPTIVE STATS FOR OCCUPATION
# oNumRat = [0] * 21
# oRat = [0] * 21
# oMeanRat = [0] * 21
# for i in range(1000209):
# 	rating = int(ratings[i, 2])
# 	occ = int(users[int(ratings[i, 0]), 3])
# 	oNumRat[occ] = oNumRat[occ] + 1
# 	oRat[occ] = oRat[occ] + rating

# for i in range(21):
# 	oMeanRat[i] = oRat[i] / oNumRat[i]

# print(oNumRat)
# print(oRat)
# print(oMeanRat)





# # Genre vs Occupation
# gomap = {}
# countmap = {}
# totalavgmap = {} # map of weighted(by occcupation) average ratings of genres
# avgmap = {} # map of average ratings of genres per occupation
# indexmap = {} # map of genre to index(occupation) of most accurate
# pemap = {} # percent error map

# def mapOccGenre(gMap, countmap, genres, rating, occ):
# 	for genre in genres:
# 		if genre not in gMap:
# 			gMap[genre] = [0] * 21
# 			countmap[genre] = [0] * 21
# 			totalavgmap[genre] = 0
# 			avgmap[genre] = [0] * 21
# 			indexmap[genre] = 0
# 			pemap[genre] = [0] * 21
# 		gMap[genre][occ] = gMap[genre][occ] + rating
# 		countmap[genre][occ] = countmap[genre][occ] + 1

# # map: genres -> [ratings per occupation by index]
# for i in range(1000209):
# 	rating = int(ratings[i, 2]) # single movie rating
# 	genres = movies[int(ratings[i, 1]), 2].strip().split('|')
# 	occ = int(users[int(ratings[i, 0]), 3])
# 	mapOccGenre(gomap, countmap, genres, rating, occ)


# for genre in gomap:
# 	for i in range(21):
# 		avgmap[genre][i] = gomap[genre][i] / countmap[genre][i]

# # map of weighted(by occcupation) average ratings of genres
# for genre in avgmap:
# 	for i in range(21):
# 		totalavgmap[genre] = totalavgmap[genre] + ((1 / 21) * avgmap[genre][i])

# # percent error
# for genre in avgmap:
# 	for i in range(21):
# 		pemap[genre][i] = percentError(avgmap[genre][i], totalavgmap[genre])


# for genre in pemap:
# 	ope = 100
# 	index = 0
# 	for pe, i in zip(pemap[genre], range(21)):
# 		if pe < ope:
# 			ope = pe
# 			index = i
# 			indexmap[genre] = index

# print(countmap)


# maleFemaleTTest = st.stats.ttest_ind(mRatings, fRatings, equal_var=False)
# ageGroupAnova = st.stats.f_oneway(age1, age18, age25, age35, age45, age50, age56)


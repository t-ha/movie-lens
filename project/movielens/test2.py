"""
Created on Wed Nov  4 11:04:55 2015

@author: Tim Ha
@date: 11.04.15
@assn: test2
"""
# -*- coding: ut-8 -*-
import codecs

# movies.txt
movieIDs = []
movieTitles = []
movieGenres = []

with codecs.open('movies.txt', 'r', encoding='UTF-8') as moviesFile:
	for mLine in moviesFile:
		mData = mLine.split('::')
		movieIDs.append(mData[0])
		movieTitles.append(mData[1])
		movieGenres.append(mData[2])


# ratings.txt
ratingsUserID = []
ratingsMovieID = []
ratings = []

with open('ratings.txt', 'r') as ratingsFile:
	for rLine in ratingsFile:
		rData = rLine.split('::')
		ratingsUserID.append(rData[0])
		ratingsMovieID.append(rData[1])
		ratings.append(rData[2])


# users.txt
userID = []
userGender = []
userAge = []
userOcc = []
userZip = []

with open('users.txt', 'r') as usersFile:
	for uLine in usersFile:
	 	uData = uLine.split('::')
	 	userID.append(uData[0])
	 	userGender.append(uData[1])
	 	userAge.append(uData[2])
	 	userOcc.append(uData[3])
	 	userZip.append(uData[4])

totalDrama = 0; # total ratings of drama films
mDrama = 0; # total ratings males gave for drama films
fDrama = 0;
numM = 0; # total number of ratinga males gave for drama films
numF = 0;
numTot = 0; # total number of ratings given for drama films
numOfRatings = len(ratingsMovieID) # 1,000,209

# MAP MovieID -> UserID & Ratings
mID2uID = {}



# avg rating males and females gave for Drama films
for genre, mID in zip(movieGenres, movieIDs):
	if 'Drama' in genre:
		for i in range(numOfRatings):
		# if 'Drama' in genre:
			if mID == ratingsMovieID[i]:
				dramaRat = int(ratings[i])
				totalDrama += dramaRat
				numTot += 1
				if userGender[int(ratingsUserID[i]) - 1] == 'M':
					numM += 1
					mDrama += dramaRat
				else:
					numF += 1
					fDrama += dramaRat


avgMaleRat = mDrama / numM
avgFemaleRat = fDrama / numF
avgDramaRat = totalDrama / numTot
print('Male')
print('# of ratings given: ' + str(numM))
print('Average rating: ' + str(avgMaleRat))
print()
print('Female')
print('# of ratings given: ' + str(numF))
print('Average rating: ' + str(avgFemaleRat))
print()
print('Total')
print('# of ratings given: ' + str(numTot))
print('Average rating: ' + str(avgDramaRat))









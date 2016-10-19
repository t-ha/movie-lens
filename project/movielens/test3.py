"""
Created on Wed Nov  4 11:04:55 2015

@author: Tim Ha
@date: 11.12.15
@assn: test3
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

numOfRatings = len(ratingsMovieID) # 1,000,209

mRat = [0, 0]
fRat = [0, 0]
totalRat = 0

for rating, rUserID in zip(ratings, ratingsUserID):
	totalRat = totalRat + int(rating)
	if userGender[int(rUserID) - 1] is 'M':
		mRat[0] = mRat[0] + 1
		mRat[1] = mRat[1] + int(rating)
	else:
		fRat[0] = fRat[0] + 1
		fRat[1] = fRat[1] + int(rating)

print('Total number of male ratings: ' + str(mRat[0]))
print('Average male rating: ' + str(mRat[1] / mRat[0]))
print('Total number of female ratings: ' + str(fRat[0]))
print('Average female rating: ' + str(fRat[1] / fRat[0]))






# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 11:04:55 2015

@author: Tim Ha
@date: 11.04.15
@assn: test1
"""
# -*- coding: ut-8 -*-
import codecs

movieIDs = []
movieTitles = []
movieGenres = []

moviesFile = codecs.open('movies.txt', 'r', encoding='UTF-8')
readMovies = moviesFile.readlines()
for mLine in readMovies:
   mData = mLine.split('::')
   movieIDs.append(mData[0])
   movieTitles.append(mData[1])
   movieGenres.append(mData[2])
moviesFile.close()

ratingsUserID = []
ratingsMovieID = []
ratings = []

ratingsFile = open('ratings.txt', 'r')
readRatings = ratingsFile.readlines()
#for rLine in readRatings:
#    rData = rLine.split('::')
#    print(rData)
ratingsFile.close()
    
usersFile = open('users.txt', 'r')
readUsers = usersFile.readlines()
# for uLine in readUsers:
#    uData = uLine.split('::')
#    print(uData)
usersFile.close()

gender = [' ']
for uLine in readUsers:
	uData = uLine.split('::')
	gender.append(uData[1])

numRatings = 1000209
numMRat = 0
numFRat = 0
mTotalRating = 0
fTotalRating = 0

for rLine in readRatings:
	rData = rLine.split('::')
	userID = int(rData[0])
	userRating = int(rData[2])
	sex = gender[userID]
	if sex == 'M':
		numMRat += 1
		mTotalRating += userRating
	else:
		numFRat += 1
		fTotalRating += userRating

avgMaleRating = mTotalRating / numMRat
avgFemaleRating = fTotalRating / numFRat
percentMaleRating = (numMRat / numRatings) * 100

print('Male: ' + str(avgMaleRating))
print('Female: ' + str(avgFemaleRating))
print('Total number of male ratings: ' + str(numMRat))
print('Total number of female ratings: ' + str(numFRat))
print('Percent male ratings: ' + str(percentMaleRating))








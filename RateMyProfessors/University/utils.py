from . models import UniReview
from Lecturer.models import LecturerReview


def calcUniRating(uni=None, lec=None):
         if uni:
                  # get each star rating count on curr uni
                  starCount = getStarsCount(uni, None)
         if lec:
                  # get each star rating count on curr lec
                  starCount = getStarsCount(None, lec)  
         # get total star count on curr uni
         total = getStarSum(starCount)
         rating = 'N/A'
         if total > 0:        
                  # calculate curr uni rating and return with butifl format
                  rating = (5*starCount['s5'] + 4*starCount['s4'] + 3*starCount['s3'] + 2*starCount['s2'] + 1*starCount['s1']) / (total)
                  rating = "{:.1f}".format(rating)
         
         return rating



# returns dict of each star count of uni
def getStarsCount(uni=None, lec=None):
         if uni:
                  s1 = UniReview.objects.filter(university=uni, score=1).count()
                  s2 = UniReview.objects.filter(university=uni, score=2).count()
                  s3 = UniReview.objects.filter(university=uni, score=3).count()
                  s4 = UniReview.objects.filter(university=uni, score=4).count()
                  s5 = UniReview.objects.filter(university=uni, score=5).count()
         if lec:
                  s1 = LecturerReview.objects.filter(lecturer=lec, score=1).count()
                  s2 = LecturerReview.objects.filter(lecturer=lec, score=2).count()
                  s3 = LecturerReview.objects.filter(lecturer=lec, score=3).count()
                  s4 = LecturerReview.objects.filter(lecturer=lec, score=4).count()
                  s5 = LecturerReview.objects.filter(lecturer=lec, score=5).count()

         starCount = {
                  's1': s1 or 0,
                  's2': s2 or 0,
                  's3': s3 or 0,
                  's4': s4 or 0,
                  's5': s5 or 0,
         }

         return starCount


# takes dict of each star count and returns sum of them
def getStarSum(starCount):
         values = starCount.values()
         total = sum(values)
         return total


def getStarsPercentage(uni=None, lec=None):
         if uni:
                  starsCount = getStarsCount(uni, None)
         if lec:
                  starsCount = getStarsCount(None, lec)
         starSum = getStarSum(starsCount)

         starsPercentage = {}

         # calculate each star percentage
         # e.g   1star - 20% , 2star - 40% ...
         if starSum > 0:
                  for key, value in starsCount.items():
                           starsPercentage[key] = round(value * 100 / starSum)
         else:
                  for key, value in starsCount.items():
                           starsPercentage[key] = 0
         
         return starsPercentage



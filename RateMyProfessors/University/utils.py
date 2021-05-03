from . models import UniReview


def calcUniRating(uni):
         # get each star rating count on curr uni
         starCount = getStarsCount(uni)
         # get total star count on curr uni
         total = getStarSum(starCount)
         rating = 'N/A'
         if total > 0:        
                  # calculate curr uni rating and return with butifl format
                  rating = (5*starCount['s5'] + 4*starCount['s4'] + 3*starCount['s3'] + 2*starCount['s2'] + 1*starCount['s1']) / (total)
                  rating = "{:.1f}".format(rating)
         
         return rating



# returns dict of each star count of uni
def getStarsCount(uni):
         s1 = UniReview.objects.filter(university=uni, score=1).count()
         s2 = UniReview.objects.filter(university=uni, score=2).count()
         s3 = UniReview.objects.filter(university=uni, score=3).count()
         s4 = UniReview.objects.filter(university=uni, score=4).count()
         s5 = UniReview.objects.filter(university=uni, score=5).count()

         starCount = {
                  's1': s1,
                  's2': s2,
                  's3': s3,
                  's4': s4,
                  's5': s5,
         }

         return starCount


# takes dict of each star count and returns sum of them
def getStarSum(starCount):
         values = starCount.values()
         total = sum(values)
         return total


def getStarsPercentage(uni):
         starsCount = getStarsCount(uni)
         starSum = getStarSum(starsCount)

         starsPercentage = {}

         # calculate each star percentage
         # e.g   1star - 20% , 2star - 40% ...
         for key, value in starsCount.items():
                  starsPercentage[key] = round(value * 100 / starSum)
         
         return starsPercentage



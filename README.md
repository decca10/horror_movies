# A lot of us like good horror movies...

I have a friend named Kari who is always looking for a new, good horror movie to watch.  I completely agree with her, I am always looking too.  But what constitutes good?  Well, there is an entire community of horror fans who spend alot of time answering that question.  Where can I find them?  On reddit of course!
I decided to look at two large reddit communities for movie discussions: [All Things Horror](https://www.reddit.com/r/horror/) and [Horror Movies ONLY!](https://www.reddit.com/r/HorrorMoviesONLY/).  

Now Kari is a little tired of people just ragging on movies and directors.  She wants to find a new horror movie to watch but she doesn't want to spend alot of time scrolling through comment after comment of negative reviews.  Kari is looking for a movie to watch, not to review herself.  So I want to refer her to either All Things Horror or Horror Movies ONLY to increase her chances of finding a movie she wants to watch.  

I will perform a sentiment analysis on both sites to see which site has more positive comments.  This will reduce the chances of Kari visiting a site and having to scroll through a lot of negative comments about films, because those will only give her a list of movies she doesn't want to see.  So I will be using sentiment analysis to find which site is more positive to indicate a "good" horror movie.

Then I will run two models to predict which forum a post came from.


Notes on Testing:
- Since we are looking to give Kari the right reddit group for her to get her horror news, I would assume that HorrorMoviesONLY will be a better indicator of good horror movies.  Therefore this is the dictionary I will use is:   

    1 = HorrorMoviesONLY   
    0 = All Things Horror, ie. r/horror       
    
- I will also combine all data into a single database to be tested on. 

# Table of Contents
- [1_API](http://localhost:8889/lab/tree/1_API.ipynb)
- [2_EDA](http://localhost:8889/lab/tree/2_EDA.ipynb)
- [3a_Sentiment_Models](http://localhost:8889/lab/tree/3a_Sentiment_Models.ipynb)
- [3b_Forum_Models](http://localhost:8889/lab/tree/3b_Forum_Models.ipynb)
- [4_Insights](http://localhost:8889/lab/tree/4_Insights.ipynb)
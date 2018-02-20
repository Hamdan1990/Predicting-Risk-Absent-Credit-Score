# Predicting Borrower Risk using Lending Club’s loan data Augmented with Alternative Data

 The current US system of lending is not very good at assessing
the risk of borrowers. It relies on a singular value known as a credit
score which is biased against people who have had one late
payment or people with no credit history. To cover the uncertainty
of borrower risk, lenders set a relatively high interest rate. This
leads to people having to pay for high interest loans even though
they aren’t risky enough. The goal of this paper is to challenge
Lending Club's approach by assessing borrower risk without taking
a look at credit score. Outside datasets and APIs are used to
augment existing dataset. Through the process of trial and error, a
model with new attributes was found that show a better probability
of predicting risk than Lending Club’s models.
Keywords—lending club; loan; risk; borrower; default

## INTRODUCTION

The current US system of lending has some flaws. Mainly,
it is not very good at assessing the risk of borrowers (look at
the 2008 recession for example). Most major banks in the US
rely regularly on a singular value to assess the risk of a
borrower, known as a credit score. A credit score is a number
assigned to a person based on their ability to make payments
on previous credit cards, loans, mortgages etc. Though that
may seem like a decent indicator of risk, it has been
notoriously erroneous in actually predicting the chances of
default for a borrower, since it is extremely biased against poor
people who have had one late payment or people with no credit
history at all [1]. Banks, knowing that credit scores are bad
indicators (while still using them), will then set a relatively
high interest rate to cover the uncertainty of borrower risk. This
leads to people having to pay for high interest loans even
though they aren’t risky enough to deserve that high interest.
Lending club [2] provides public access to data on their loans
with attributes such as customer income, credit score, state,
credit card utilization, home ownership etc. as well as
information about the loan (loan amount, term, and whether
paid back or defaulted). The dataset categorizes the risk of each
borrower by their credit score and sets interest rates for them
appropriately.
 Our goal is to challenge Lending Club's approach by
assessing borrower risk without taking a look at credit score.
We will be using outside datasets and APIs to augment our
existing dataset. For example, we will be pulling in Zillow to
analyze average house prices for a zip code, consumer price
index to measure cost of goods at the time of borrowing,
unemployment rates from the US bureau of Labor Statistics,
population density by county from US Census bureau and any
other datasets we can get our hands on. Through this process of
trial and error, we hope to find attributes about a borrower that
predict better borrower risk, which can be used to give out
better, low-interest loans to those who actually deserve it the
most.

## RELATED WORK

There has been lot of work done on Lending club loan data
such as "Predicting borrowers chance of defaulting on credit
loans" [3], "Predicting Probability of Loan Default" [4] and
"Peer Lending Risk Predictor" [5]. They have applied machine
learning to improve loan default prediction. The authors have
compared the performance of various models such as Random
Forest, Naïve Bayes and SVM’s. The more recent “Predicting
default risk of Lending Club Loans” [6] has added in census
data, with info like regional median income, to train models on
a more holistic set of features. We are taking this approach one
step further by augmenting our current data set with outside
data such as Zillow’s average home price index, consumer
price index at the time of borrowing and unemployment rates
from the US bureau of Labor Statistics. Through this approach,
we hope to show the true risk of a borrower without using
credit score as an indicator of risk.

## INTELECTUAL MERIT

In the age of information, there are troves of data being
collected about the United States and its people every single
day. The difficulty in this project is to be able to discern the
data that have the ability to predict borrower risk, which means
that our group had to spend as much time on reading about the
causes for loan default as we did reading on analyzing the data.
A purely computer science approach would not have factored
in the nuances of the lending industry and the factors that
impact it.

## BROADER IMPACT
The United States is one of the best countries to borrow
money from, even if the methodology of using credit score is
no the optimal method to do so. That is because, in
comparison, other countries have no method at all for
calculating borrower risk. Countries like Brazil can charge 
upwards of 70% (Brazil Bank Lending Rates, 2017) as interest
rates for personal and business loans due to the inability to
properly access credit risk. Our model is extensible to work in
any country since it does not rely on a specifically calculated
credit score but rather data available to the public in almost
every country such as home prices, treasury bill rates,
unemployment rates etc. Since this model can use this public
data to access borrower risk, banks can dramatically reduce
uncertainty premium of loan interest rates and provide more
accessible funds to people.

## CHALLENGES

The main challenge that we faced is in finding datasets that
are detailed and free. Several of the datasets that we originally
thought we could use were in fact either premium datasets or
not as detailed as we would have liked (for e.g. annual data vs.
country level data). Since we couldn’t find several of the
datasets we hypothesized would exponentially increase the
quality of predicting borrower risk (for e.g. county crime data),
we had to rework our premise from being that we can predict
“true risk” to the premise that we can improve the current risk
prediction models.

Furthermore, due to the Equal Credit Opportunity Act of
1974 (Fair Lending n.d.), all underwriting models in the
United States have to be able to dictate the top 3 reasons why a
loan was rejected/approved. This allows for the government to
validate that a loan was not rejected on the premises of race,
age, ethnicity, sex, sexual orientation etc. Though this law is
great for consumers, it does inhibit the ability for modern
underwriting systems based on Neural Networks, Random
Forests, Clustering Algorithms etc to be used as underwriting
systems since it is extremely difficult to be able to dictate the
features that led to a loan being labeled as being charged-off in
the future vs. not. This limitation dramatically decreases the
types of machine-learning techniques we can use to build
underwriting models. 

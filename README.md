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

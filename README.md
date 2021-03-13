# Election Analysis

### Overview of Election Audit
A Colorado Board of Elections employee requested support with the following tasks in order to complete the election audit of a recent local congressional election:

1. Calculate the total number of votes cast.
2. Get a complete list of the votes each candidate received.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.


### Election Audit Results
For this election:

- A total of 369,711 votes were casted for this congressional election.

- The votes were casted in three main counties and the total number of votes and percentage per county was as follows:
{insert image}

To get to this result, a dictionary for the counties was established. Then a loop was established to get the county from the dictiionary in order to retrieve the vote count for each. After this, the percentage of votes was calculated for each county and then the instruction to print the county results was established.

This section of the code was set as follows:
{insert image}

- The county that had the largest number of votes was Denver.

The code used to retrieve this information first wrote an if statement to determine the winning county and get its vote county. The code was set as follows:

{insert image}

This piece of code establishes that if votes are higher in the winning county count then the winning county count will be defined by the number of votes and the winning county will be defined by the county name.

- As for the candidates. the breakdown of the number of votes and the percentage of the total votes resulted as follows:
{insert image}

- The winner of the election was Diana DeGette who received 73.8% of the vote and 272,892 votes.

{insert image}

### Election Audit Summary



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

<img width="204" alt="Screen Shot 2021-03-12 at 9 41 45 PM" src="https://user-images.githubusercontent.com/78698456/111016909-65aebb00-837e-11eb-9f34-da31c518e8d3.png">

To get to this result, a dictionary for the counties was established. Then a loop was established to get the county from the dictiionary in order to retrieve the vote count for each. After this, the percentage of votes was calculated for each county and then the instruction to print the county results was established. The code resulted as follows:

<img width="574" alt="Screen Shot 2021-03-12 at 9 48 35 PM" src="https://user-images.githubusercontent.com/78698456/111016903-5e87ad00-837e-11eb-873f-f3ae48f3d7ce.png">

- The county that had the largest number of votes was Denver.

This information was retrieved through an if statement to determine the winning county and get its vote county. The code resulted as follows:

<img width="610" alt="Screen Shot 2021-03-12 at 9 54 31 PM" src="https://user-images.githubusercontent.com/78698456/111016905-60ea0700-837e-11eb-902f-3fe935994a86.png">

This piece of code establishes that if votes are higher in the county voter count then the winning county count will be defined by the number of votes and the winning county will be defined by the county name.

- As for the candidates, the breakdown of the number of votes and the percentage of the total votes resulted as follows:

<img width="360" alt="Screen Shot 2021-03-12 at 9 56 06 PM" src="https://user-images.githubusercontent.com/78698456/111016907-634c6100-837e-11eb-9f71-bb3b3e6a9c97.png">

- The winner of the election was Diana DeGette who received 73.8% of the vote and 272,892 votes.

<img width="231" alt="Screen Shot 2021-03-12 at 9 59 12 PM" src="https://user-images.githubusercontent.com/78698456/111016986-db1a8b80-837e-11eb-9555-7056d0510ca7.png">


### Election Audit Summary



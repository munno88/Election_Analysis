# Election Analysis Audit 

## Overview of Project amd prupose 

overview of Project The Election commission has requested additional data to complete the audit which they reqire 

1. The voter turout for each county.
2. The Percentage of Votes from each county out of the total count.
3. The county with the highest turnout (Election winner).

and we completed there requirement using or skill and codes and formatting.



## Results

To get the result first i add dependencies and import csv file then i add variabe to load file from path and add variable to save path as Election_analysis.txt and create path to load the file we initialize county list using candidate_options that will hold the names of the counties, also i intitialize dictionary using candidate_votes dictonary using following code image. i intialize empty string like winning_candidate and winning_count, i use for loop and if statement and finally create txt file and we got this result as follow one is from terminal and other one is from txt file we created using code. 



Result from Terminal

![Election_Results_from_Terminal](https://user-images.githubusercontent.com/103727169/175794412-e77d8f1b-5638-40a2-b7d6-4965c6eb2152.png)

Result from txt file

![Election_results_file_created](https://user-images.githubusercontent.com/103727169/175794419-0628aedd-9dbe-4129-89b7-7e2d2630da56.png)

load file and initialize candidate and dictionary

![file_to_load](https://user-images.githubusercontent.com/103727169/175794504-2f1ce1b7-bf5a-4dfd-860b-c9d5e5cf1129.png)



the total votes for this Election were 369,711. and out of this all county Denver had the highest votes 306,055. in percentage were 82.8% but other county Jefferson got 10.5% and votes were 38,855, also Arapahoe county were lowest 6.7% votes 24,801. out of this winner county were Denver. and winner candidate Diana DeGette vote count were 272,892 with winning Percentage were 73.8%





### Summary

summary in my point of view there are several other way we can explores this election audit and but most two point i can say are following.

   1. in this election audit we did not have many candidate or county, Multiple candidates & counties can be added to the list to include larger datasets. Using the following function in the program allows it to append additional data.

   ![candidate](https://user-images.githubusercontent.com/103727169/175794425-d4aeb900-dccd-49a7-803e-3b3d3bb0677d.png)


   2. we got the result for county and candidate but we can also include city and there candidate using variable ad winning count and winning percentage.

   ![winning](https://user-images.githubusercontent.com/103727169/175794429-ffc7d843-68d7-46b1-a611-7ef1784009ef.png)


   overall in this election analysis they can use for bigger set of data mean more candidate and more city. and this will be useful to get those kind of result doing fewer changes in code.


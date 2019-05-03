# CSCI 4502
## Team Members
Stephen Kay, Rachel Mamich, Levi Nickerson, Brandon Rajkowski

## Project Description
The aim of this project was to define and use different data-mining techniques in order to potentially be able to better stratify the ever changing and volatile stock market. Techniques used in this paper include neural networks, k-means, clustering, correlation co-efficient analysis, frequent pattern mining, and decision trees. However, before any of this was performed the data was cleaned in an appropriate manner to allow for easy data access and for clean interpretation of results. Key results from this project include being able to accurately correlate similar companies performances, being able to cluster appropriate portfolios together, and the neural-net created slightly out performed the random guess rate of 50\%. Overall, the results in this paper further contribute to the study of data-mining techniques and their overall application to stock market analysis.

## Questions Sought
* What stocks are commonly bought and sold together for a profit? 
* Are there patterns in stocks prior to stock values crashing or skyrocketing?
* Are there any predictable patterns that can be exploited for profit?
* Are there pairs of stocks whose prices typically trend in the same or opposite directions?

## Applications
* Neural network or Bayes Classifier can be applied after market close to predict if next day market close price will be higher / lower
* Build a day trade portfolio for the next day
* Buy short term options contracts


## Video Link
https://youtu.be/-J7mcpYVk-I

## Neural Net
### Packages
* MathNet.Numerics:
    ```
    PM> Install-Package MathNet.Numerics -Version 4.7.0
    ```
The easiest way to build and run the neural network code is to install Visual Studio (https://visualstudio.microsoft.com/vs/community/).  With Visual Studio installed, ensure that .NET Core/Framework packages are installed.  Then install the MathNet.Numerics package using the Nuget package manager and the command above.  To the run code, simply use the Visual Studio GUI and press the `Run` button.

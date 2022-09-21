# mission_to_mars

## Gathering Information
The purpose of this webpage and overall exercise was to build a locally hosted page that contained all the information we wanted to see together in one source that was easy to read and display. We also needed this page to be interactive and able to scrape updated information from the host sites were we collected the data. The webpage would become a place were we could showcase our data in a readable front-end.

## --App.py-- 
This module of our code was strictly designed to run flask and point to another module which would hold our webscraping instructions, this module also contains our mongo DB instructions so that whatever data we tell the module to scrape will have a location to hold said data.
The purpose of seperating out this code from the remaining code was so that it could be repurposed if needed to scrape data from other modules with only a few small changes. In our case we made a module called scraping and imported it back into this module. This has the effect of making app.py a re-usable tool for scraping web pages with only minor updates. Please view the code image below to see an example of this code.

![This is an image](https://github.com/Bren42/mission_to_mars/blob/main/resources/app_py.png)

## --Scraping.py--
This is the module where we specifically identify where we want to scrape data and specifically what data we want to scrape. This module of code is also designed to have the scraped data setup to return its information to the HTML index we built to display our outputs. In this module we built functions to collect the specific data that would become the webpage. So in the case of Mars news we built a function that would only scrape and return Mars news titles, functions for featured image, mars news, mars facts, and the hemisphere images were also built.

![This is an image](https://github.com/Bren42/mission_to_mars/blob/main/resources/scraping_py.png))

## --Index.html

This is the final code we built to showcase our data. This was designed to take all the data we collected on the backend and give it a readable and more accessible format. We needed to also add an easy way for anyone to update the page easily by creating a button that would redirect to the scraping code and go out to the pages to collect current news.
One of the key areas we wanted to check was to make sure that everything that went into this page would not only viewable for a desktop PC user but also for the myriad of mobile and portable devices such as smart phones and tablets. 
We made sure that the page was responsive to different devices by updating the HTML to have  "X-UA-Compatible" in our index.
![This is an image](https://github.com/Bren42/mission_to_mars/blob/main/resources/mobile%20responsive.png)

as you can see in this first image the console is set to view the page from a Samsung device, a S20 ultra. All page features and items show as expected. 
however to show this function is truly working look at what happens when we view the page from an Ipad:
![This is an image](https://github.com/Bren42/mission_to_mars/blob/main/resources/mobile%20responsive2.png)
after running these tests we could safely confirm our page will be readable by the vast majority of devices. 

--Bootstrap components--

We also wanted to go into the page and give it a couple unique items that would give it more appeal. As stated earlier we needed a button to refresh the scraped data. Initially this button is blue, but to keep in style with the red planet this was changed to a red button:

![This is an image](https://github.com/Bren42/mission_to_mars/blob/main/resources/Page_header.png)

When we scraped the data we brought in a table to show comparative mars datat to earth, we wanted to make sure the table was easy to read so we gave it a border:

![This is an image](https://github.com/Bren42/mission_to_mars/blob/main/resources/bordered%20table.png)

Finally we also wanted to make sure that the hemisphere images that we brought over would not only fit on the page, but also have clearly delineated seperations, so we gave them a thumbnail format to make them look more cleanly aligned with the page.

![This is an image](https://github.com/Bren42/mission_to_mars/blob/main/resources/thumbnail%20format.png)

Once all of this was completed we could run our page and view the data related to Mars and update the news headlines at any time.



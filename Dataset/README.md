Datasets

## Overview
This folder contains the details on the datasets used for training object detection model and recipe recommendation. 

## Object Detection Dataset
For object detection, dataset are composed of images of raw ingredients of a common part of Filipino cuisine. The image datasets used for this research were carefully picked and web-scraped from different web platforms such as Kaggle, OpenCv, RoboFlow, Adobe Stock, and others. The following platforms have different qualities in order for the model to broaden its scope of understanding for object detection. We have gathered 250 images per class which have 200 images for train data and 50 for test data.

Due to the size limitation of Github, you can access the dataset in this link:  https://drive.google.com/drive/folders/1za7pf2lYmIXsEnmrdjuxjylgfykX5OB8?usp=drive_link .

### Object Detection Dataset Details
- **Classes:**
<table border="1">
  <tr>
    <th>Label</th>
    <th>Class</th>
  </tr>
  <tr>
    <td>0</td>
    <td>Beef</td>
  </tr>
  <tr>
    <td>1</td>
    <td>Bitter-Gourd</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Bottle-Gourd</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Broccoli</td>
  </tr>
  <tr>
    <td>4</td>
    <td>Cabbage</td>
  </tr>
  <tr>
    <td>5</td>
    <td>Carrots</td>
  </tr>
  <tr>
    <td>6</td>
    <td>Cauliflower</td>
  </tr>
  <tr>
    <td>7</td>
    <td>Chicken</td>
  </tr>
  <tr>
    <td>8</td>
    <td>Egg</td>
  </tr>
  <tr>
    <td>9</td>
    <td>Eggplant</td>
  </tr>
  <tr>
    <td>10</td>
    <td>Galunggong</td>
  </tr>
  <tr>
    <td>11</td>
    <td>Garlic</td> <!-- Empty row for additional data -->
  </tr>
  <tr>
    <td>12</td>
    <td>Ginger</td> <!-- Empty row for additional data -->
  </tr>
  <tr>
    <td>13</td>
    <td>Milkfish</td> <!-- Empty row for additional data -->
  </tr>
  <tr>
    <td>14</td>
    <td>Onion</td> <!-- Empty row for additional data -->
  </tr>
  <tr>
    <td>15</td>
    <td>Papaya</td> <!-- Empty row for additional data -->
  </tr>
  <tr>
    <td>16</td>
    <td>Pork</td> <!-- Empty row for additional data -->
  </tr>
  <tr>
    <td>17</td>
    <td>Potato</td> <!-- Empty row for additional data -->
  </tr>
  <tr>
    <td>18</td>
    <td>Sayote</td> <!-- Empty row for additional data -->
  </tr>
  <tr>
    <td>19</td>
    <td>Tilapia</td> <!-- Empty row for additional data -->
  </tr>
  <tr>
    <td>20</td>
    <td>Tomato</td> <!-- Empty row for additional data -->
  </tr>
</table>

- **Dataset Size:** 9,634 images

- **Dataset Pre-processing:**
  - Resizing
  - Flipping
  - Shearing
  - Saturation
  - Brightness
  - Exposure

## Recipe Recommendation Dataset
The dataset used for the recipe recommendation system is outsourced from GitHub by Shaan Subbaiah [^1] on project, allrecipes-scraper. The outsourced dataset from this project comes from scraping allrecipes.com, a food-focused online social networking service.

### Recipe Recommendation Dataset Details
- **Features**
  - **name:** Recipe Name
  - **url:** The web address where the recipe can be originally found
  - **category:** The category of the recipe
  - **author:** The person who created the recipe.
  - **summary:** A brief overview of the recipe or item.
  - **rating:** The average rating given by users or reviewers.
  - **rating_count:** The number of ratings the recipe or item has received.
  - **review_count:** The number of reviews or comments submitted by users.
  - **ingredients:** The list of ingredients required for the recipe.
  - **directions:** The step-by-step instructions for preparing the recipe.
  - **prep:** The time required to prepare the ingredients before cooking.
  - **cook:** The time required to cook the recipe.
  - **total:** The total time required for the entire recipe, including preparation and cooking.
  - **servings:** The number of servings the recipe yields.
  - **yield:** The output produced by the recipe.
  - **calories:** The number of calories in the entire yield.
  - **carbohydrates_g:** The total amount of carbohydrates in the entire yield, measured in grams.
  - **sugars_g:** The total amount of sugars in the entire yield, measured in grams.
  - **fat_g:** The total amount of fat in the entire yield, measured in grams.
  - **saturated_fat_g:** The amount of saturated fat in the entire yield, measured in grams.
  - **cholesterol_mg:** The amount of cholesterol in the entire yield, measured in milligrams.
  - **protein_g:** The total amount of protein in the entire yield, measured in grams.
  - **dietary_fiber_g:** The amount of dietary fiber in the entire yield, measured in grams.
  - **sodium_mg:** The amount of sodium in the entire yield, measured in milligrams.
  - **calories_from_fat:** The number of calories from fat in the entire yield.
  - **calcium_mg:** The amount of calcium in the entire yield, measured in milligrams.
  - **iron_mg:** The amount of iron in the entire yield, measured in milligrams.
  - **magnesium_mg:** The amount of magnesium in the entire yield, measured in milligrams.
  - **potassium_mg:** The amount of potassium in the entire yield, measured in milligrams.
  - **zinc_mg:** The amount of zinc in the entire yield, measured in milligrams.
  - **phosphorus_mg:** The amount of phosphorus in the entire yield, measured in milligrams.
  - **vitamin_a_iu_IU:** The amount of vitamin A in the entire yield, measured in International Units (IU).
  - **niacin_equivalents_mg:** The amount of niacin equivalents in the entire yield, measured in milligrams.
  - **vitamin_b:** The types and amounts of vitamin B in the entire yield.

- **Dataset Size:** 35,516 recipes
- **Dataset Preprocessing**
  - Conversion of fractions in unicode format to decimal form for uniform presentation, data integrity, and normalization of data formats.
  - Modification of quantities based on user desired serving size
  - Extraction of crucial information from ingredients column to the another column which allows easier retrieval of core data for the recommendation system.

# References
[^1]: Shaansubbaiah, “Shaansubbaiah/allrecipes-scraper: 🥗 scrapy spider to scrape recipe and nutritional data from allrecipes.com,” GitHub, https://github.com/shaansubbaiah/allrecipes-scraper/tree/main



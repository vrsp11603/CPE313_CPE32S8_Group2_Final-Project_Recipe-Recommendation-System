![image](https://github.com/user-attachments/assets/7d56345a-d8af-4249-a74e-6744897f37f1)# Datasets

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
  - **name:**
  - **url:**
  - **category:**
  - **author:**
  - **summary:**
  - **rating:**
  - **rating_count:**
  - **review_count:**
  - **ingredients:**
  - **directions:**
  - **prep:**
  - **cook:**
  - **total:**
  - **servings:**
  - **yield:**
  - **calories:**
  - **carbohydrates_g:**
  - **sugars_g:**
  - **fat_g:**
  - **saturated_fat_g:**
  - **cholesterol_mg:**
  - **protein_g:**
  - **dietary_fiber_g:**
  - **sodium_mg:**
  - **calories_from_fat:**
  - **calcium_mg:**
  - **iron_mg:**
  - **magnesium_mg:**
  - **potassium_mg:**
  - **zinc_mg:**
  - **phosphorus_mg:**
  - **vitamin_a_iu_IU:**
  - **niacin_equivalents_mg:**
  - **vitamin_b:**



# References
[^1]: Shaansubbaiah, “Shaansubbaiah/allrecipes-scraper: 🥗 scrapy spider to scrape recipe and nutritional data from allrecipes.com,” GitHub, https://github.com/shaansubbaiah/allrecipes-scraper/tree/main



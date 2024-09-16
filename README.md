# Car Parts Sale
- This smal project is designed to manage and track the sales, ordered stock, and returns of car parts (oil, oil filter, and tyres) using Google Sheets for data storage. The application allows users to input sales data, calculate returns, and automatically update stock levels based on recent sales trends.Car Parts is a Python program which runs in the Code Institute mock terminal on Heroku.

![Am I responsive](/assets/images/am_i_responsive_screenshot.png)

[Here is the live version of the project](https://ui.dev/amiresponsive?url=https://car-parts-b60d5067a52f.herokuapp.com/)

[Here is a link to the google worksheet](https://docs.google.com/spreadsheets/d/1_wsutQEMeso8AFcV2-I9BJZfBTwSbN1P3jpc7tCIZ9w/edit?gid=654488592#gid=654488592)

## How it works
- The user must enter 3 nmbers of how many of each parts was sold.And program will count how many was returned and how many was ordered.
![front page](/assets/images/start-page.png)

## Spreadsheet before data entered

![Worksheet](/assets/images/worksheet_before_adding_data.png)

## Adding data
- Here user can add what ever data he/she heave.

![Add data](/assets/images/adding_data-image.png)

## After presing enter
- Image shows that all data was uploaded succesfully

![Data uploaded](/assets/images/uploaded_data.png)

## Worksheet after uploading data

- And here we can see taht data was uploaded to worksheet

![Worksheet after uploading](/assets/images/after_data_uploading_image.png)

## Features

- **Sales Data Entry**: Accepts sales input for car parts (oil, oil filters, and tires) via the command line.
- **Data Validation**: Validates that the entered data consists of three integers.
- **Google Sheets Integration**: Automatically stores data in Google Sheets for real-time tracking.
- **Inventory Management**: Calculates returned items based on sales data and tracks them.
- **Stock Ordering**: Automatically calculates new stock orders based on the last five sales, with a 10% buffer to ensure sufficient inventory.

## Technologies

- Python 3.x
- Google Sheets API
- Google Drive API
- `gspread` library for interacting with Google Sheets
- `google-auth` for managing API authentication

## Testing
- Was tested manualy on gitpod.By adding python3 run.py comand.
- Tested on Heroku.
- Added wrong type of data:letters,symbols and etc.

- Here image with wrong data.
![Data uploaded](/assets/images/invalid_data.png)

- Image after presing enter button

![Data uploaded](/assets/images/error_message.png)

## Deployment

- The project was deployed using Heroku.

    - Steps for deployment
        - Create a new Heroku app
        - Add Config Vars for CREDS(creds.json file content) and PORT(8000)
        - Set the buildbacks in order Pythong first and NodeJS second
        - Link the Heroku app to the repository
        - Click on Deploy

## Credits

- Code Institute for studying material
- Slack members for support and help.
- Tutor Kamil-ci provided with usfull links and motivation not to give up.







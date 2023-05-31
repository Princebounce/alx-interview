Star Wars Characters
This script fetches and prints the characters of a Star Wars movie using the Star Wars API.

Installation
Make sure you have Node.js installed on your machine. You can download it from nodejs.org.

Clone this repository to your local machine or download the script file.

Install the required dependencies by running the following command in your terminal:
```
$ npm install request
```

Usage
Run the script with the following command:

```
$ node 0-starwars_characters.js <movieId>
```

Replace <movieId> with the ID of the Star Wars movie you want to retrieve characters for. For example, to get characters for "Return of the Jedi," you would use:


```

$ node 0-starwars_characters.js 3
```

The script will fetch the movie data from the Star Wars API and display the character names in the same order as the "characters" list in the movie's endpoint.

API Rate Limiting
Please note that the Star Wars API has rate limiting. If you encounter any issues, such as receiving empty character data or being unable to fetch characters, it might be due to hitting the rate limit. In such cases, you can try again later or consider using your own API key if available.

Dependencies
request: A simplified HTTP client for making API requests in Node.js.

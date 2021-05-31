import React, { useState } from 'react';
import Autocomplete from '@material-ui/lab/Autocomplete'
import TextField from '@material-ui/core/TextField'
import { getAllSongs } from "./databasehandler"

// Initially load all songs from db on pageload.
// Get Array with json-objects out of response with Object.values()
let allSongs = Object.values(getAllSongs());

// function from https://www.codegrepper.com/code-examples/javascript/sort+an+array+of+dictionaries+elements+javascript
let compareObjects = (object1, object2, key) => {
  const obj1 = object1[key].toUpperCase()
  const obj2 = object2[key].toUpperCase()
  if (obj1 < obj2) {
    return -1
  }
  if (obj1 > obj2) {
    return 1
  }
  return 0
}

// sort "Song_title" alphabetically.
allSongs.sort((e1, e2) => {
  return compareObjects(e1, e2, 'Song_title')
})

function App() {
  // function state for selectedSong and suggestionResults; initially empty
  const [selectedSong, setSelectedSong] = useState({ Song_title: "" });
  const [suggestionResults, setSuggestionResults] = useState([{ Song_title: "", Artist: "" }, { Song_title: "", Artist: "" }, { Song_title: "", Artist: "" }]);

  // Search songinformations for given songTitle. Assumption: Songtitles per Artist are unique. 
  let searchSonginformation = (songTitle, myArray) => {
    for (var i = 0; i < myArray.length; i++) {
      if (myArray[i].Song_title === songTitle) {
        return myArray[i];
      }
    }
  }

  // check if arrays have common elements, return true if.
  let findCommonElement = (array1, array2) => {
    // Loop trough both arrays.
    for (let i = 0; i < array1.length; i++) {
      for (let j = 0; j < array2.length; j++) {
        // If elements matching, return true.
        if (array1[i] === array2[j]) {
          return true;
        }
      }
    }
    // If no match was found, return false.
    return false;
  }

  // genereate song suggestion based on given songinformations.
  let getSongSuggestions = (songInformations) => {
    let errorForEachSong = []
    // songInformation entity:
    // {Angry: 0.15, Fear: 0.08, genre: 0, Happy: 0, interpret: "['Uli']", …}

    // Loop trough all songs and calculate error for each song based on absolute difference.
    allSongs.forEach(function (song) {
      let sentimentError = 0
      // We don't want the same song or songs from different genre as suggestion. Thats why we give those songs high error values.
      if (song.Song_title === songInformations.Song_title || !findCommonElement(song.Song_genre, songInformations.Song_genre)) {
        sentimentError = 100000000000
        // This block sums up all errors (absolute differences) between given song and currently inspected song.
        // SentimentError will be saved in errorForEachSong-list.
      } else {
        sentimentError += Math.abs(song.Happy - songInformations.Happy)
        sentimentError += Math.abs(song.Angry - songInformations.Angry)
        sentimentError += Math.abs(song.Surprise - songInformations.Surprise)
        sentimentError += Math.abs(song.Sad - songInformations.Sad)
        sentimentError += Math.abs(song.Fear - songInformations.Fear)
      }
      errorForEachSong.push(sentimentError)
    });

    // The list returnSongs will now be filled with the 3 best fitting songs.
    let returnSuggestedSongs = []
    let inbdexOfSmallestError = 0
    let allSongs_tmp_copy = allSongs.slice(0, -1)
    // For-loop to detect the 3 best fitting songs.
    for (let index = 0; index < 3; index++) {
      inbdexOfSmallestError = errorForEachSong.indexOf(Math.min.apply(Math, errorForEachSong));
      returnSuggestedSongs.push(allSongs_tmp_copy.splice(inbdexOfSmallestError, 1)[0])
    }
    return returnSuggestedSongs
  }


  let generateSuggestion = () => {
    // get current song informations. Song_title contains title and interpret and only the title is necessary.
    let currentSongInformations = searchSonginformation(selectedSong.Song_title.split("  -  ")[0], allSongs)
    // get song suggestion based on current song informations.
    let songSuggestions = getSongSuggestions(currentSongInformations)
    // set song suggestion into suggestionResults-state.
    setSuggestionResults(songSuggestions)
  }

  // Display necessary inputfield and songsuggestionsresults on website:
  return (
    <div className="App" style={{ textAlign: "center" }}>
      <h1 style={{ textAlign: "center" }}>Songtiteleingabe:</h1>
      <Autocomplete
        id="combo-box-demo"
        limitTags={2}
        options={allSongs}
        maxSearchResults={10}
        getOptionLabel={(option) => option.Song_title + "  -  " + option.Artist}
        renderInput={(params) => <TextField {...params} label="Song" variant="outlined" />}
        inputProps={{ maxLength: 20 }}
        style={{
          width: 300,
          marginLeft: "auto",
          marginRight: "auto"
        }}
        onChange={(e) => { setSelectedSong({ Song_title: e.target.innerHTML }) }}
      />
      <button
        onClick={() => { generateSuggestion() }}
        style={{
          marginTop: 50,
          width: 300,
          marginLeft: "auto",
          marginRight: "auto",
          marginBottom: 50
        }}>
        {"Vorschlag generieren"}
      </button>
      <p style={{ textAlign: "center", fontWeight: "bold" }}>Songvorschlag:</p>
      <p style={{ textAlign: "center" }}>{suggestionResults[0].Song_title + "  -  " + suggestionResults[0].Artist}</p>
      <p style={{ textAlign: "center" }}>{suggestionResults[1].Song_title + "  -  " + suggestionResults[1].Artist}</p>
      <p style={{ textAlign: "center" }}>{suggestionResults[2].Song_title + "  -  " + suggestionResults[2].Artist}</p>
    </div>
  );
}

export default App;

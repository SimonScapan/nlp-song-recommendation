import React, { useState } from 'react';
import Autocomplete from '@material-ui/lab/Autocomplete'
import TextField from '@material-ui/core/TextField'
import './App.css';
import { getAllSongs } from "./databasehandler"

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


// Initially load all songs from db on pageload.
let allSongs = Object.values(getAllSongs());
  allSongs.sort((e1, e2) => {
  return compareObjects(e1, e2, 'song_title')
})

function App() {
  // function state for selectedSong and suggestes Songs
  const [selectedSong, setSelectedSong] = useState({ song_title: "" });
  const [suggestionResults, setSuggestionResults] = useState([{ song_title: "",artist:""}, { song_title: "",artist:""}, { song_title: "" ,artist:""}]);
  console.log(allSongs)
  // searchSonginformation for whole songinformation for given title. Assumption: Songtitles are unique. 
  let searchSonginformation = (nameKey, myArray) => {
    console.log("in searchSonginformation")
    console.log(nameKey)
    for (var i = 0; i < myArray.length; i++) {
      console.log(myArray[i].song_title == nameKey)
      console.log(myArray[i].song_title)
      if (myArray[i].song_title == nameKey) {
        return myArray[i];
      }
    }
  }

  // check if arrays have common elements.
  let findCommonElement = (array1, array2) => {
    // Loop trough both arrays
    for (let i = 0; i < array1.length; i++) {
      for (let j = 0; j < array2.length; j++) {
        // if elements matching, return true
        if (array1[i] === array2[j]) {
          return true;
        }
      }
    }
    // If not match was found, return false 
    return false;
  }

  // genereate song suggestion based on given songinformations
  let getSongSuggestions = (songInformations) => {
    let error = []
    // songInformation entity:
    // {angry: 0.15, fear: 0.08, genre: 0, happy: 0, interpret: "['Uli']", …}
    // Loop trough all songs and calculate error for each song based on absolute difference.
    allSongs.forEach(function (song) {
      console.log("in each")
      console.log(song)
      console.log(songInformations)
      let sentimentError = 0
      // We don't want the same song or songs from different genre as suggestion. Thats why we give those songs high error Values.
      if (song.song_title == songInformations.song_title || !findCommonElement(song.song_genre, songInformations.song_genre)) {
        sentimentError = 100000000000
        // This block sums up all errors (absolute differences) between given song and currently inspected song 
        // from all songs and saves this error as sentimentError into the error-list.
      } else {
        sentimentError += Math.abs(song.happy - songInformations.happy)
        sentimentError += Math.abs(song.angry - songInformations.angry)
        sentimentError += Math.abs(song.surprise - songInformations.surprise)
        sentimentError += Math.abs(song.sad - songInformations.sad)
        sentimentError += Math.abs(song.fear - songInformations.fear)
      }
      error.push(sentimentError)
    });

    // The list retunSongs will now be filled with 3 smallest error songs.
    let returnSongs = []
    let inbdexOfSmallestError = 0
    let allSongs_tmp_copy = allSongs.slice(0, -1)
    for (let index = 0; index < 3; index++) {
      inbdexOfSmallestError = error.indexOf(Math.min.apply(Math, error));
      returnSongs.push(allSongs_tmp_copy.splice(inbdexOfSmallestError, 1)[0])
    }
    return returnSongs
  }


  let generateSuggestion = () => {
    // get current song informations.
    console.log("selected Song:")
    console.log(selectedSong.song_title.split("  -  ")[0])
    let currentSongInformations = searchSonginformation(selectedSong.song_title.split("  -  ")[0], allSongs)
    // get song suggestion based on current song informations.
    let songSuggestions = getSongSuggestions(currentSongInformations)
    // set song suggestion into suggestionResults.
    setSuggestionResults(songSuggestions)
  }

  // Display necessary input on website.
  return (
    <div className="App" style={{ textAlign: "center" }}>
      <h1 style={{ textAlign: "center" }}>Songtiteleingabe:</h1>
      <Autocomplete
        id="combo-box-demo"
        options={allSongs}
        getOptionLabel={(option) => option.song_title+"  -  "+option.artist}
        renderInput={(params) => <TextField {...params} label="Song" variant="outlined" />}
        style={{
          width: 300,
          marginLeft: "auto",
          marginRight: "auto"
        }}
        onChange={(e) => { setSelectedSong({ song_title: e.target.innerHTML }) }}
      />
      <button
        onClick={() => { generateSuggestion() }}
        style={{
          marginTop:50,
          width: 300,
          marginLeft: "auto",
          marginRight: "auto",
          marginBottom:50
        }}>
        {"Vorschlag generieren"}
      </button>
      <p style={{ textAlign: "center", fontWeight: "bold"}}>Songvorschlag:</p>
      <p style={{ textAlign: "center" }}>{suggestionResults[0].song_title +"  -  "+suggestionResults[0].artist}</p>
      <p style={{ textAlign: "center" }}>{suggestionResults[1].song_title +"  -  "+suggestionResults[1].artist}</p>
      <p style={{ textAlign: "center" }}>{suggestionResults[2].song_title +"  -  "+suggestionResults[2].artist}</p>
    </div>
  );
}

export default App;

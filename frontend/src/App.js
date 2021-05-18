import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route, Link, Switch } from "react-router-dom";
import Autocomplete from '@material-ui/lab/Autocomplete'
import TextField from '@material-ui/core/TextField'
import './App.css';
import { getAllSongs } from "./databasehandler"


function App() {
  const [selectedSong, setSelectedSong] = useState("");
  const [suggestionResults, setSuggestionResults] = useState();
  let allSongs = Object.values(getAllSongs());
  console.log(allSongs)
  
  Array.min = function (array) {
    return Math.min.apply(Math, array);
  };

  let search = (nameKey, myArray) => {
    for (var i = 0; i < myArray.length; i++) {
      if (myArray[i].title === nameKey) {
        return myArray[i];
      }
    }
  }

  let getSongSuggestions = (songInformations) => {
    let erorr = []
    // index; Error
    // {"Happy": 0, "Angry": 0, "Surprise": 0, "Sad": 0, "Fear": 0}
    allSongs.forEach(function (song, index, error){
      let sentimentError = 0
      sentimentError += song.happy - songInformations.happy
      sentimentError += song.angry - songInformations.angry
      sentimentError += song.surprise - songInformations.surprise
      sentimentError += song.sad - songInformations.sad
      sentimentError += song.fear - songInformations.fear
      error.push(sentimentError)
    });
    let smallestError = erorr.min;
    var inbdexOfSmallestError = erorr.indexOf(smallestError);
    console.log("Songrecommondatino")
    console.log(allSongs[inbdexOfSmallestError])

  }

  let generateSuggestionDisplay = () => {
    let currentSongInformations = search(selectedSong, allSongs)
    let songSuggestions = getSongSuggestions(currentSongInformations)
    setSuggestionResults(<h1>{songSuggestions}</h1>)
    setSelectedSong("")
    console.log("generateSuffestion fetr")
  }

  console.log(suggestionResults)
  console.log(selectedSong)
  return (
    <div className="App">
      <h1>Songtiteleingabe:</h1>

      <Autocomplete
        id="combo-box-demo"
        options={allSongs}
        getOptionLabel={(option) => option.title}
        style={{ width: 300 }}
        renderInput={(params) => <TextField {...params} label="Combo box" variant="outlined" />}
        onChange={(e) => { setSelectedSong(e.target.innerHTML) }}
      />
      <button
        onClick={() => { generateSuggestionDisplay() }}>
        {"Vorschlag generieren"}
      </button>

      {suggestionResults}


    </div>
  );
}

export default App;

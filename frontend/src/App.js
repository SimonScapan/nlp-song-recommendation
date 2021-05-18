import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route, Link, Switch } from "react-router-dom";
import Autocomplete from '@material-ui/lab/Autocomplete'
import TextField from '@material-ui/core/TextField'
import './App.css';
import { getAllSongs } from "./databasehandler"


function App() {
  const [selectedSong, setSelectedSong] = useState("");
  const [suggestionResults, setSuggestionResults] = useState({title:""});
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
  var BreakException = {};
  let getSongSuggestions = (songInformations) => {
    console.log("im getSuggestions:")
    console.log(songInformations)
    let error = []
    // index; Error
    // {angry: 0.15, fear: 0.08, genre: 0, happy: 0, interpret: "['Uli']", …}
    console.log("start error calculation")
    allSongs.forEach(function (song){
      console.log("forEach")
      // console.log(error)
      // console.log(song.angry)
      // console.log(songInformations.angry)
      
      let sentimentError = 0
      sentimentError += song.happy - songInformations.happy
      sentimentError += song.angry - songInformations.angry
      sentimentError += song.surprise - songInformations.surprise
      sentimentError += song.sad - songInformations.sad
      sentimentError += song.fear - songInformations.fear
      error.push(sentimentError)
    });
    let smallestError = Math.min.apply(Math, error)
    var inbdexOfSmallestError = error.indexOf(smallestError);
  return allSongs[inbdexOfSmallestError]

  }

  let generateSuggestionDisplay = () => {
    let currentSongInformations = search(selectedSong, allSongs)
    let songSuggestions = getSongSuggestions(currentSongInformations)
    setSuggestionResults(songSuggestions)
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
      <p>Songvorschlag:</p>
      <p>{suggestionResults.title}</p>


    </div>
  );
}

export default App;

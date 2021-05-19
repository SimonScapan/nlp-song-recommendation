import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route, Link, Switch } from "react-router-dom";
import Autocomplete from '@material-ui/lab/Autocomplete'
import TextField from '@material-ui/core/TextField'
import './App.css';
import { getAllSongs } from "./databasehandler"

let allSongs = Object.values(getAllSongs());

function App() {
  const [selectedSong, setSelectedSong] = useState("");
  const [suggestionResults, setSuggestionResults] = useState([{ title: "" }, { title: "" }, { title: "" }]);
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
    
    allSongs.forEach(function (song) {
      // console.log(error)
      // console.log(song.angry)
      // console.log(songInformations.angry)


      let sentimentError = 0

      if (song.title == songInformations.title) {
        sentimentError = 100000000000
      } else {
        sentimentError += Math.abs(song.happy - songInformations.happy)
        sentimentError += Math.abs(song.angry - songInformations.angry)
        sentimentError += Math.abs(song.surprise - songInformations.surprise)
        sentimentError += Math.abs(song.sad - songInformations.sad)
        sentimentError += Math.abs(song.fear - songInformations.fear)
      }
      error.push(sentimentError)
    });
    console.log("Recommn fenidstiso")
    let returnSongs = []
    let inbdexOfSmallestError = 0
    for (let index = 0; index < 3; index++) {
      inbdexOfSmallestError = error.indexOf(Math.min.apply(Math, error));
      returnSongs.push(allSongs.splice(inbdexOfSmallestError, 1)[0])
    }

    return returnSongs

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
    <div className="App" style={{textAlign:"center"}}>
      <h1 style={{ textAlign: "center" }}>Songtiteleingabe:</h1>

      <Autocomplete
        id="combo-box-demo"
        options={allSongs}
        getOptionLabel={(option) => option.title}
        renderInput={(params) => <TextField {...params} label="Combo box" variant="outlined" />}
        style={{
          width: 300,
          marginLeft: "auto",
          marginRight: "auto"
         }}
        onChange={(e) => { setSelectedSong(e.target.innerHTML) }}
      />
      <button
        onClick={() => { generateSuggestionDisplay() }}
        style={{ marginLeft: "auto",
        marginRight: "auto" }}>
        {"Vorschlag generieren"}
      </button>
      <p style={{ textAlign: "center" }}>Songvorschlag:</p>
      <p style={{ textAlign: "center" }}>{suggestionResults[0].title}</p>
      <p style={{ textAlign: "center" }}>{suggestionResults[1].title}</p>
      <p style={{ textAlign: "center" }}>{suggestionResults[2].title}</p>


    </div>
  );
}

export default App;
